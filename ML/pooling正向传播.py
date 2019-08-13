'''
池化层正向传播子函数

池化层输出改变的是输入的大小，不改变channel大小
长：H_out = (H - kernel_size)/stride + 1
宽：W_out = (W - kernel_size)/stride + 1

https://blog.csdn.net/weixin_37251044/article/details/81328494
'''
import numpy as np
def forward(self, in_data):
    self.bottom_val = in_data #

    N, C, H, W = in_data.shape # 输入数据的条数、Channel、长、宽，比如10张图片，每张图的表示有3个channel， 每个channel表示长一个长x宽的矩阵
    HH, WW, stride = self.kernel.size, self.kernel_size, self.stride
    
    H_out = int((H - HH)/stride + 1) # 池化之后剩多长
    W_out = int((W - WW)/stride + 1) # 池化之后剩多宽
    out = np.zeros((N, C, H_out, W_out))
    for i in range(H_out):
        for j in range(W_out):
            x_masked = in_data[:, :, i*stride: i*stride+HH, j*stride: j*stride+WW]
            out[:, :, i, j] = np.max(x_masked, axis=(2, 3)) # H和M位置的最大值
    return out
    