#pragma once
#include <torch/types.h>

namespace cvpods {
    
void masked_im2col_forward(const at::Tensor im, const at::Tensor mask_h_idx,
                           const at::Tensor mask_w_idx, at::Tensor col,
                           const int kernel_h, const int kernel_w,
                           const int pad_h, const int pad_w);

void masked_col2im_forward(const at::Tensor col, const at::Tensor mask_h_idx,
                           const at::Tensor mask_w_idx, at::Tensor im, int height,
                           int width, int channels);

} // namespace cvpods
