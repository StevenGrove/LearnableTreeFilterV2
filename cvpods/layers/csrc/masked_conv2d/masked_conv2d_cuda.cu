#include "masked_conv2d.h"
#include <ATen/ATen.h>
#include <ATen/cuda/CUDAContext.h>
#include <c10/cuda/CUDAGuard.h>
#include <THC/THCAtomics.cuh>
#include <cuda.h>
#include <torch/extension.h>
#include <vector>

#define CHECK_CUDA(x) \
  TORCH_CHECK(x.device().is_cuda(), #x " must be a CUDA tensor")
#define CHECK_CPU(x) \
  TORCH_CHECK(!x.device().is_cuda(), #x " must be a CPU tensor")
#define CHECK_CONTIGUOUS(x) \
  TORCH_CHECK(x.is_contiguous(), #x " must be contiguous")
#define CHECK_CUDA_INPUT(x) \
  CHECK_CUDA(x);            \
  CHECK_CONTIGUOUS(x)
#define CHECK_CPU_INPUT(x) \
  CHECK_CPU(x);            \
  CHECK_CONTIGUOUS(x)

#define THREADS_PER_BLOCK 512

#define CUDA_1D_KERNEL_LOOP(i, n)                              \
  for (int i = blockIdx.x * blockDim.x + threadIdx.x; i < (n); \
       i += blockDim.x * gridDim.x)

using at::Tensor;

inline int GET_BLOCKS(const int N) {
  int optimal_block_num = (N + THREADS_PER_BLOCK - 1) / THREADS_PER_BLOCK;
  int max_block_num = 4096;
  return min(optimal_block_num, max_block_num);
}

namespace cvpods {

void MaskedIm2colForwardCUDAKernelLauncher(const Tensor bottom_data,
                                           const Tensor mask_h_idx,
                                           const Tensor mask_w_idx,
                                           Tensor top_data, const int kernel_h,
                                           const int kernel_w, const int pad_h,
                                           const int pad_w);

void MaskedCol2imForwardCUDAKernelLauncher(const Tensor bottom_data,
                                           const Tensor mask_h_idx,
                                           const Tensor mask_w_idx,
                                           Tensor top_data, const int height,
                                           const int width, const int channels);

void masked_im2col_forward_cuda(const Tensor im, const Tensor mask_h_idx,
                                const Tensor mask_w_idx, Tensor col,
                                const int kernel_h, const int kernel_w,
                                const int pad_h, const int pad_w) {
  // im: (n, ic, h, w), kernel size (kh, kw)
  // kernel: (oc, ic * kh * kw), col: (kh * kw * ic, ow * oh)
  MaskedIm2colForwardCUDAKernelLauncher(im, mask_h_idx, mask_w_idx, col,
                                        kernel_h, kernel_w, pad_h, pad_w);
}

void masked_col2im_forward_cuda(const Tensor col, const Tensor mask_h_idx,
                                const Tensor mask_w_idx, Tensor im, int height,
                                int width, int channels) {
  // im: (n, ic, h, w), kernel size (kh, kw)
  // kernel: (oc, ic * kh * kh), col: (kh * kw * ic, ow * oh)
  MaskedCol2imForwardCUDAKernelLauncher(col, mask_h_idx, mask_w_idx, im, height,
                                        width, channels);
}

void masked_im2col_forward(const Tensor im, const Tensor mask_h_idx,
                           const Tensor mask_w_idx, Tensor col,
                           const int kernel_h, const int kernel_w,
                           const int pad_h, const int pad_w) {
  if (im.device().is_cuda()) {
    CHECK_CUDA_INPUT(im);
    CHECK_CUDA_INPUT(mask_h_idx);
    CHECK_CUDA_INPUT(mask_w_idx);
    CHECK_CUDA_INPUT(col);
    masked_im2col_forward_cuda(im, mask_h_idx, mask_w_idx, col, kernel_h,
                               kernel_w, pad_h, pad_w);
  } else {
    AT_ERROR("MaskConv is not implemented on CPU");
  }
}

void masked_col2im_forward(const Tensor col, const Tensor mask_h_idx,
                           const Tensor mask_w_idx, Tensor im, int height,
                           int width, int channels) {
  if (col.device().is_cuda()) {
    CHECK_CUDA_INPUT(col);
    CHECK_CUDA_INPUT(mask_h_idx);
    CHECK_CUDA_INPUT(mask_w_idx);
    CHECK_CUDA_INPUT(im);
    masked_col2im_forward_cuda(col, mask_h_idx, mask_w_idx, im, height, width,
                               channels);
  } else {
    AT_ERROR("MaskConv is not implemented on CPU");
  }
}

template <typename scalar_t>
__global__ void MaskedIm2colForward(const int n, const scalar_t *data_im,
                                    const int height, const int width,
                                    const int kernel_h, const int kernel_w,
                                    const int pad_h, const int pad_w,
                                    const int64_t *mask_h_idx,
                                    const int64_t *mask_w_idx,
                                    const int mask_cnt, scalar_t *data_col) {
  // mask_cnt * channels
  CUDA_1D_KERNEL_LOOP(index, n) {
    const int m_index = index % mask_cnt;
    const int h_col = mask_h_idx[m_index];
    const int w_col = mask_w_idx[m_index];
    const int c_im = index / mask_cnt;
    const int c_col = c_im * kernel_h * kernel_w;
    const int h_offset = h_col - pad_h;
    const int w_offset = w_col - pad_w;
    scalar_t *data_col_ptr = data_col + c_col * mask_cnt + m_index;
    for (int i = 0; i < kernel_h; ++i) {
      int h_im = h_offset + i;
      for (int j = 0; j < kernel_w; ++j) {
        int w_im = w_offset + j;
        if (h_im >= 0 && w_im >= 0 && h_im < height && w_im < width) {
          *data_col_ptr =
              (scalar_t)data_im[(c_im * height + h_im) * width + w_im];
        } else {
          *data_col_ptr = 0.0;
        }
        data_col_ptr += mask_cnt;
      }
    }
  }
}

template <typename scalar_t>
__global__ void MaskedCol2imForward(const int n, const scalar_t *data_col,
                                    const int height, const int width,
                                    const int channels,
                                    const int64_t *mask_h_idx,
                                    const int64_t *mask_w_idx,
                                    const int mask_cnt, scalar_t *data_im) {
  CUDA_1D_KERNEL_LOOP(index, n) {
    const int m_index = index % mask_cnt;
    const int h_im = mask_h_idx[m_index];
    const int w_im = mask_w_idx[m_index];
    const int c_im = index / mask_cnt;
    // compute the start and end of the output
    data_im[(c_im * height + h_im) * width + w_im] = data_col[index];
  }
}

void MaskedIm2colForwardCUDAKernelLauncher(const Tensor bottom_data,
                                           const Tensor mask_h_idx,
                                           const Tensor mask_w_idx,
                                           Tensor top_data, const int kernel_h,
                                           const int kernel_w, const int pad_h,
                                           const int pad_w) {
  int channels = bottom_data.size(1);
  int height = bottom_data.size(2);
  int width = bottom_data.size(3);
  int mask_cnt = mask_h_idx.size(0);
  int output_size = mask_cnt * channels;

  at::cuda::CUDAGuard device_guard(bottom_data.device());
  cudaStream_t stream = at::cuda::getCurrentCUDAStream();
  AT_DISPATCH_FLOATING_TYPES_AND_HALF(
      bottom_data.scalar_type(), "MaskedIm2colLaucherForward", ([&] {
        const scalar_t *bottom_data_ = bottom_data.data_ptr<scalar_t>();
        const int64_t *mask_h_idx_ = mask_h_idx.data_ptr<int64_t>();
        const int64_t *mask_w_idx_ = mask_w_idx.data_ptr<int64_t>();
        scalar_t *top_data_ = top_data.data_ptr<scalar_t>();
        MaskedIm2colForward<scalar_t>
            <<<GET_BLOCKS(output_size), THREADS_PER_BLOCK, 0, stream>>>(
                output_size, bottom_data_, height, width, kernel_h, kernel_w,
                pad_h, pad_w, mask_h_idx_, mask_w_idx_, mask_cnt, top_data_);
      }));
  AT_CUDA_CHECK(cudaGetLastError());
}

void MaskedCol2imForwardCUDAKernelLauncher(
    const Tensor bottom_data, const Tensor mask_h_idx, const Tensor mask_w_idx,
    Tensor top_data, const int height, const int width, const int channels) {
  int mask_cnt = mask_h_idx.size(0);
  int output_size = mask_cnt * channels;

  at::cuda::CUDAGuard device_guard(bottom_data.device());
  cudaStream_t stream = at::cuda::getCurrentCUDAStream();
  AT_DISPATCH_FLOATING_TYPES_AND_HALF(
      bottom_data.scalar_type(), "MaskedCol2imLaucherForward", ([&] {
        const scalar_t *bottom_data_ = bottom_data.data_ptr<scalar_t>();
        const int64_t *mask_h_idx_ = mask_h_idx.data_ptr<int64_t>();
        const int64_t *mask_w_idx_ = mask_w_idx.data_ptr<int64_t>();
        scalar_t *top_data_ = top_data.data_ptr<scalar_t>();

        MaskedCol2imForward<scalar_t>
            <<<GET_BLOCKS(output_size), THREADS_PER_BLOCK, 0, stream>>>(
                output_size, bottom_data_, height, width, channels, mask_h_idx_,
                mask_w_idx_, mask_cnt, top_data_);
      }));
  AT_CUDA_CHECK(cudaGetLastError());
}

} // namespace cvpods
