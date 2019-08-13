'''
用keras实现线性回归
不用Sequential
'''
import keras
import numpy as np
import matplotlib.pyplot as plt
from keras.models import Model
from keras.layers.core import Dense
from keras.layers import Input

# 搭建模型
inputs = Input(shape=(1,), dtype='float32', name='inputlayer')
dense = Dense(units=1, input_dim=1, activation='linear')(inputs)
model = Model(inputs=inputs, outputs=dense)
model.compile(
    loss='mse',
    optimizer='sgd',
    metrics=['accuracy']
)
model.summary()

x = np.random.rand(100) # 随机生成100个点
noise = np.random.normal(loc=0, scale=0.01, size=x.shape) # 生成标准正态分布
y = x*0.1 + 0.2 + noise

model.fit(x, y, epochs=3000, verbose=0) # batch_size=64
y_pred = model.predict(x)

# cost = model.evaluate(x_test, y_yesy, batch_size=40)
# print("cost on test:", cost)

w,b = model.layers[1].get_weights()
print("w = ", w, "bias = ", b)


# 显示随机点
plt.scatter(x, y)

# 显示预测结果
plt.plot(x, y_pred, 'r-', lw=2)
plt.show()
