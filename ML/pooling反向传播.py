'''
pooling反向传播

https://blog.csdn.net/weixin_37251044/article/details/81328494
'''

import numpy as np

bottom_data_7 = np.load('pic.npy')
print("Maxpooling层的bottom_data的shape是：", bottom_data_7.shape)

x_masked = bottom_data_7[:, :, 0:3, 0:3]
print("bottom_data的第一个batch的第一个3X3区域的数是：")
print(x_masked.shape)
print(x_masked[0][0])

max_x_masked = np.max(x_masked, axis=(2,3))

print("bottom_data的第一个batch的第一个3X3区域的最大的数是：")
print(max_x_masked.shape)
print((max_x_masked)[:,:,None,None][0][0])

temp_binary_mask = (x_masked == (max_x_masked)[:, :, None, None])
print("bottom_data的第一个batch的第一个3X3区域最大的数在本区域中的位置是（true）：")
print(temp_binary_mask[0][0])

residual_6_relu = np.load('residual_6_relu.npy')
dx = np.zeros_like(residual_6_relu)
print("下层传过来的残差residual的shape是：")
print(residual_6_relu.shape)
print("下层传过来的残差residual的第一个batch的第一个通道的第一个diff是：")
print(residual_6_relu[0,0,0,0])
dx[:, :, 0:3, 0:3] += temp_binary_mask*(residual_6_relu[:, :, 0, 0])[:, :, None, None]
print("将残差正向传播时取的在3X3区域内的最大数的位置：")
print(dx[0][0][0])


