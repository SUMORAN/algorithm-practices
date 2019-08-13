# https://cloud.tencent.com/developer/article/1198054
# 文章写的很好，可以是不是回顾一下

'''
函数架构
Convolution functions
    zero Padding
    Convolve Window
    Convolution fordward
    Convolution backward

Pooling function
    Pooling forward
    Create mask
    Create mask
    Pooling backward

'''
import numpy as np

"""
 Padding的作用在进行卷积操作之后不必减少图片的深度和宽度，这对于构建更深层的网络很重要。
 其次，它帮助我们保存更多图像边缘的信息，没有Padding,下一层的值很少被图像的边缘所影响。
 这里我们使用np.pad—numpy.pad(array, pad_width, mode, **kwargs)
"""
def zero_pad(X, pad):
    """
    Pad with zeros all images of the dataset X. The padding is applied to the height and width of an image, 
    as illustrated in Figure 1.
    
    Argument:
    X -- python numpy array of shape (m, n_H, n_W, n_C) representing a batch of m images
    pad -- integer, amount of padding around each image on vertical and horizontal dimensions
    
    Returns:
    X_pad -- padded image of shape (m, n_H + 2*pad, n_W + 2*pad, n_C)
    """

    ### START CODE HERE ### (≈ 1 line)
    X_pad = np.pad(X, ((0,0), (pad,pad), (pad,pad), (0,0)), 'constant', constant_values = (0,0))
    ### END CODE HERE ###

    return X_pad

###  单步卷积
def conv_single_step(a_slice_prev, W, b):
    """
    Apply one filter defined by parameters W on a single slice (a_slice_prev) of the output activation 
    of the previous layer.
    
    Arguments:
    a_slice_prev -- slice of input data of shape (f, f, n_C_prev)
    W -- Weight parameters contained in a window - matrix of shape (f, f, n_C_prev)
    b -- Bias parameters contained in a window - matrix of shape (1, 1, 1)
    
    Returns:
    Z -- a scalar value, result of convolving the sliding window (W, b) on a slice x of the input data
    """

    ### START CODE HERE ### (≈ 2 lines of code)
    # Element-wise product between a_slice and W. Do not add the bias yet.
    s = a_slice_prev * W
    # Sum over all entries of the volume s.
    Z = np.sum(s)
    # Add bias b to z. Cast b to a float() so that Z results in a scalar value
    Z = Z + b
    ### END CODE HERE ###
    return Z

### 卷积神经网络前向传播
def conv_forward(A_prev, W, b, hparameters):
    """
    Implements the forward propagation for a convolution function
    
    Arguments:
    A_prev -- output activations of the previous layer, numpy array of shape (m, n_H_prev, n_W_prev, n_C_prev)
    W -- Weights, numpy array of shape (f, f, n_C_prev, n_C)
    b -- Biases, numpy array of shape (1, 1, 1, n_C)
    hparameters -- python dictionary containing "stride" and "pad"
        
    Returns:
    Z -- conv output, numpy array of shape (m, n_H, n_W, n_C)
    cache -- cache of values needed for the conv_backward() function
    """
    
    ### START CODE HERE ###
    # Retireve dimensions from A_pre's shape (≈1 line)
    (m, n_H_prev, n_W_prev, n_C_prev) = np.shape(A_prev)

    # Retrieve dimensions from W's shape  (≈1 line) 
    # f相当于 kernel_size
    (f, f, n_C_prev, n_C) = np.shape(W)

    # Retrieve information from "hparameters"  (≈2 line)
    stride = hparameters['stride']
    pad = hparameters['pad']

    # 计算CONV 的输出的维度
    n_H = int((n_H_prev - f + 2*pad) / stride) + 1
    n_W = int((n_W_prev - f + 2*pad) / stride) + 1
    
    # 初始化卷积输出
    Z = np.zeros(m, n_H, n_W, n_C)

    # Create A_prev_pad by padding A_prev
    A_prev_pad = zero_pad(A_prev, pad)

    for i in range(m):
        # 第i条数据
        a_prev_pad = A_prev_pad[i, :, :, :]
        for h in range(n_H):
            for w in range(n_W):
                for c in n_C:
                    # Find the corners of the current "slice" (≈4 lines)
                    vert_strat = h * stride
                    vert_end = vert_strat + f
                    horiz_start = w * stride
                    horiz_end = horiz_start + f
                    
                    # Use the corners to define the (3D) slice of a_prev_pad (See Hint above the cell). (≈1 line)
                    a_slice_prev = a_prev_pad[vert_strat:vert_end, horiz_start:horiz_end, :]

                    # Convolve the (3D) slice with the correct filter W and bias b, to get back one output neuron. (≈1 line)
                    Z[i, h, w, c] = conv_single_step(a_slice_prev, W[:, :, :, c], b[:, :, :, c])

    ### END CODE HERE ###

    # Making sure your output shape is correct
    assert(Z.shape == (m, n_H, n_W, n_C))

    # save information in "cache" for backprop
    cache = (A_prev, W, b, hparameters)

    return Z, cache

'''
上面的conv函数中包含padding， 同时卷积时考虑参数W和b
下面的池化是在conv的输出上进行的,不需要考虑padding和W，b，其余获取输入输出维度，
初始化输出矩阵，计算每个h每个w每个channel的过程跟conv一样，只是将上述算参数的过程变成对a_prev_slice求max或者求mean的过程
'''



# 池化层前向传播 
def pool_forward(A_prev, hparameters, mode="max"):
    """
    Implements the forward pass of the pooling layer
    
    Arguments:
    A_prev -- Input data, numpy array of shape (m, n_H_prev, n_W_prev, n_C_prev)
    hparameters -- python dictionary containing "f" and "stride"
    mode -- the pooling mode you would like to use, defined as a string ("max" or "average")
    
    Returns:
    A -- output of the pool layer, a numpy array of shape (m, n_H, n_W, n_C)
    cache -- cache used in the backward pass of the pooling layer, contains the input and hparameters 
    """

    # Retireve dimensions from the input shape
    (m, n_H_prev, n_W_prev, n_C_prev) = A_prev.shape

    # Retrieve hparameters from "hparameters"
    f = hparameters["f"]
    stride = hparameters["stride"]
    
    # Define the dimensions of the output
    n_H = int((n_H_prev - f)/stride) + 1
    n_W = int((n_W_prev - f)/stride) + 1
    n_C = n_C_prev

    # Initialize output matrix A
    A = np.zeros(m, n_H, n_W, n_C)

    ### START CODE HERE ###
    for i in range(m):              # loop over the training examples
        for h in range(n_H):        # loop on the vertical axis of the output volume
            for w in range(n_W):    # loop on the horizontal axis of the output volume
                for c in range(n_C):# loop over the channels of the output volume
                    vert_start = h*stride
                    vert_end = vert_start + f
                    horiz_start = w*stride
                    horiz_end = horiz_start + f
                    
                    a_prev_slice = A_prev[i, vert_start:vert_end, horiz_start:horiz_end, c]

                    if mode == "max":
                        A[i, h, w, c] = np.max(a_prev_slice)
                    elif mode == "average":
                        A[i, h, w, c] = np.mean(a_prev_slice)
    ### END CODE HERE ###

    # Store the input and hparameters in "cache" for pool_backward()
    cache = (A_prev, hparameters)

    # Making sure your output shape is correct
    assert(A.shape == (m, n_H, n_W, n_C))

    return A, cache


# 反向传播过程

# 计算dA
da_prev_pad[vert_start:vert_end, horiz_start:horiz_end, :] += W(:, :, :, c) * dZ[i, h, w, c] # Z是卷积函数的输出

# 计算dW
# dWc是过滤器相对于loss的导数
dW[:, :, :, c] += a_slice * dZ[i, h, w, c]
# 计算db
db[:, :, :, c] += dZ[i ,h, w, c]

# 以下为完整的卷积过程的反向传播函数
def conv_backward(dZ, cache):
    """
    Implement the backward propagation for a convolution function
    
    Arguments:
    dZ -- gradient of the cost with respect to the output of the conv layer (Z), numpy array of shape (m, n_H, n_W, n_C)
    cache -- cache of values needed for the conv_backward(), output of conv_forward()
    
    Returns:
    dA_prev -- gradient of the cost with respect to the input of the conv layer (A_prev),
               numpy array of shape (m, n_H_prev, n_W_prev, n_C_prev)
    dW -- gradient of the cost with respect to the weights of the conv layer (W)
          numpy array of shape (f, f, n_C_prev, n_C)
    db -- gradient of the cost with respect to the biases of the conv layer (b)
          numpy array of shape (1, 1, 1, n_C)
    """

    ### START CODE HERE ###
    # Retrieve information from "cache"
    (A_prev, W, b, hparameters) = cache

    # Retrieve dimensions from A_prev's shape
    (m, n_H_prev, n_W_prev, n_C_prev) = np.shape(A_prev)

    # Retrieve dimensions from W's shape
    (f, f, n_C_prev, n_C) = np.shape(W)

    # Retrieve information from "hparameters"
    stride = hparameters['stride']
    pad = hparameters['stride']

    # Retrieve dimensions for dZ's shape
    (m, n_H, n_W, n_C) = np.shape(dZ)

    # Initialize dA_prev, dW, db with the correct shapes
    dA_prev = np.zeros((m, n_H_prev, n_W_prev, n_C_prev))
    dW = np.zeros((f, f, n_C_prev, n_C))
    db = np.zeros((1, 1, 1, n_C))

    # Pad A_prev and dA_prev
    A_pred_pad = zero_pad(A_prev, pad)
    dA_prev_pad = zero(pad(dA_prev, pad))

    for i in range(m):
        # select ith training example from A_prev_pad and dA_prev_pad
        a_prev_pad = A_pred_pad[i, :, :, :]
        da_prev_pad = dA_prev_pad[i, :, :, :]

        for h in range(n_H):
            for w in range(n_W):
                for c in range(n_C):
                    vert_start = h * stride
                    vert_end = vert_start + f
                    horiz_start = w * stride
                    horiz_end = horiz_start + f

                    a_slice = a_prev_pad[vert_start:vert_end, horiz_start:horiz_end, :]
                
                    # Update gradients for the window and the filter's parameters using the code formulas given above
                    da_prev_pad[vert_start:vert_end, horiz_start:horiz_end, :] += W[:, :, :, c] * dZ[i, h, w, c]
                    dW[:, :, :, c] += a_slice*dZ[i, h, w, c]
                    db[:, :, :, c] += dZ[i, h, w, c]

        # Set the ith training example's dA_prev to the unpaded da_prev_pad (Hint: use X[pad:-pad, pad:-pad, :])
        dA_prev[i, :, :, :] = da_prev_pad[pad:-pad, pad:-pad,:]

    ### END CODE HERE ###

    assert(dA_prev.shape == (m, n_H_prev, n_W_prev, n_C_prev))

    return dA_prev, dW, db



# 最大池化层反向传播
# 建立最大池化层反向传播之前，先建立一个帮助函数 create_mask_from_window()，
# 该帮助函数记录矩阵X的最大位置
# 如果有一个矩阵X和一个标量x， A = (X == x)，返回矩阵A，
# 如同以下代码效果
A[i,j] = True if X[i,j] = x
A[i,j] = False if X[i,j] != x

def create_mask_from_window(x):
    """
    Creates a mask from an input matrix x, to identify the max entry of x.

    Arguments:
    x -- Array of shape (f, f)

    Returns:
    mask -- Array of the same shape as window, contains a True at the position corresponding to the max entry of x.
    """

    ### START CODE HERE ### (≈1 line)
    maxk = x == np.max(x)
    ### END CODE HERE ###

    return mask

# 平均池化反向传播
# 建立帮助函数 distribute_value(dz, shape)
def distribute_value(dz, shape):
    """
    Distributes the input value in the matrix of dimension shape
    
    Arguments:
    dz -- input scalar
    shape -- the shape (n_H, n_W) of the output matrix for which we want to distribute the value of dz
    
    Returns:
    a -- Array of size (n_H, n_W) for which we distributed the value of dz
    """

    ### START CODE HERE ###
    # Retrieve dimensions from shape (≈1 line)
    (n_H, n_W) = shape

    # Compute the value to distribute on the matrix (≈1 line)
    average = dz / (n_H * n_W)

    # Create a matrix where every entry is the "average" value (≈1 line)
    a = np.full(shape, average)
    ### END CODE HERE ###

    return a

'''
现在可以构建池化层返现传播了，
需要一个四重循环（ training examples, height, width, and channels）。
通过if/else选择最大池化或者平均池化。
如果是平均池化，使用distribute_value(),如果是最大池化，使用create_mask_from_window()
'''
def pool_backward(dA, cache, mode="max"):
    """
    Implements the backward pass of the pooling layer
    
    Arguments:
    dA -- gradient of cost with respect to the output of the pooling layer, same shape as A
    cache -- cache output from the forward pass of the pooling layer, contains the layer's input and hparameters 
    mode -- the pooling mode you would like to use, defined as a string ("max" or "average")
    
    Returns:
    dA_prev -- gradient of cost with respect to the input of the pooling layer, same shape as A_prev
    """

    ### START CODE HERE ###

    # Retrieve information from cache (≈1 line)
    (A_prev, hparameters) = cache

    # Retrieve hyperparameters from "hparameters" (≈2 lines)
    stride = hparameters['stride']
    f = hparameters['f']

    # Retrieve dimensions from A_prev's shape and dA's shape (≈2 lines)
    m, n_H_prev, n_W_prev, n_C_prev = np.shape(A_prev)
    m, n_H, n_W, n_C = np.shape(dA)

    # Initialize dA_prev with zeros (≈1 line)
    dA_prev = np.zeros(np.shape(A_prev))

    for i in range(m):
        # select training example from A_prev (≈1 line)
        a_prev = A_prev[i,:,:,:]
        for h in range(n_H):
            for w in range(n_W):
                for c in range(n_C):
                    # Find the corners of the current "slice" (≈4 lines)
                    vert_start = h * stride
                    vert_end = vert_start + f
                    horiz_start = w * stride
                    horiz_end = horiz_start + f

                    # Compute the backward propagation in both modes.
                    if mode == "max":
                        # Use the corners and "c" to define the current slice from a_prev (≈1 line)
                        a_prev_slice = a_prev[vert_start:vert_end, horiz_start:horiz_end, c]
                        # Create the mask from a_prev_slice (≈1 line)
                        mask = create_mask_from_window(a_prev_slice)
                        # Set dA_prev to be dA_prev + (the mask multiplied by the correct entry of dA) (≈1 line)
                        dA_prev[i, vert_start:vert_end, horiz_start:horiz_end, c] += np.multiplied(mask, dA[i, h, w, c])
                    
                    elif mode == "average":
                        # Get the value a from dA (≈1 line)
                        da = dA[i, h, w, c]
                        # Define the shape of the filter as fxf (≈1 line)
                        shape = (f, f)
                        # Distribute it to get the correct slice of dA_prev. i.e. Add the distributed value of da. (≈1 line)
                        dA_prev[i, vert_start:vert_end, horiz_start:horiz_end, c] += distribute_value(da, shape)

    ### END CODE ###

    # Making sure your output shape is correct
    assert(dA_prev.shape == A_prev.shape)

    return dA_prev
    

                    





