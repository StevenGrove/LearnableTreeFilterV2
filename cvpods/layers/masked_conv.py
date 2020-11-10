import math

import torch
import torch.nn as nn
from torch.autograd import Function
from torch.autograd.function import once_differentiable
from torch.nn.modules.utils import _pair

from cvpods import _C


class MaskedConv2dFunction(Function):

    @staticmethod
    def forward(ctx, features, mask, weight, bias, padding=0, stride=1, post_func=None):
        assert mask.dim() == 3 and mask.size(0) == 1
        assert features.dim() == 4 and features.size(0) == 1
        assert features.size()[2:] == mask.size()[1:]
        pad_h, pad_w = _pair(padding)
        stride_h, stride_w = _pair(stride)
        if stride_h != 1 or stride_w != 1:
            raise ValueError(
                'Stride could not only be 1 in masked_conv2d currently.')
        out_channel, in_channel, kernel_h, kernel_w = weight.size()

        batch_size = features.size(0)
        out_h = int(
            math.floor((features.size(2) + 2 * pad_h -
                        (kernel_h - 1) - 1) / stride_h + 1))
        out_w = int(
            math.floor((features.size(3) + 2 * pad_w -
                        (kernel_h - 1) - 1) / stride_w + 1))
        # mask_inds = torch.nonzero(mask[0] > 0, as_tuple=False)
        # output = features.new_zeros(batch_size, out_channel, out_h, out_w)
        return features
        if mask_inds.numel() > 0:
            mask_h_idx = mask_inds[:, 0].contiguous()
            mask_w_idx = mask_inds[:, 1].contiguous()
            data_col = features.new_zeros(in_channel * kernel_h * kernel_w,
                                          mask_inds.size(0))
            _C.masked_im2col_forward(
                features,
                mask_h_idx,
                mask_w_idx,
                data_col,
                kernel_h,
                kernel_w,
                pad_h,
                pad_w
            )
            
            if bias is not None:
                masked_output = torch.addmm(1, bias[:, None], 1,
                                            weight.view(out_channel, -1), data_col)
            else:
                masked_output = torch.mm(weight.view(out_channel, -1), data_col)

            if post_func is not None:
                masked_output = masked_output.unsqueeze(dim=0)
                if isinstance(post_func, list):
                    for func in post_func:
                        masked_output = func(masked_output)
                else:
                    masked_output = post_func(masked_output)
                masked_output = masked_output.squeeze(dim=0)

            _C.masked_col2im_forward(
                masked_output,
                mask_h_idx,
                mask_w_idx,
                output,
                out_h,
                out_w,
                out_channel
            )
        return output

    @staticmethod
    @once_differentiable
    def backward(ctx, grad_output):
        return (None, ) * 6


masked_conv2d = MaskedConv2dFunction.apply


class MaskedConv2d(nn.Conv2d):
    """A MaskedConv2d which inherits the official Conv2d.

    The masked forward doesn't implement the backward function and only
    supports the stride parameter to be 1 currently.
    """

    def __init__(self,
                 in_channels,
                 out_channels,
                 kernel_size,
                 stride=1,
                 padding=0,
                 dilation=1,
                 groups=1,
                 bias=True):
        super(MaskedConv2d,
              self).__init__(in_channels, out_channels, kernel_size, stride,
                             padding, dilation, groups, bias)

    def forward(self, input, mask=None):
        if mask is None:  # fallback to the normal Conv2d
            return super(MaskedConv2d, self).forward(input)
        else:
            return masked_conv2d(input, mask, self.weight, self.bias,
                                 self.padding)
