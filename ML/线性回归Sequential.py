'''
用keras实现线性回归
'''
import keras
import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense

# 使用numpy生成100个随机点
x_data = np.random.rand(100)
noise = np.random.normal(loc=0, scale=0.01, size=x_data.shape) # 生成标准正态分布
y_data = x_data*0.1 + 0.2 + noise

# 把这些点在坐标轴中打印出来
plt.scatter(x_data, y_data)
plt.xlabel("x")
plt.ylabel("y")
plt.title("random")
plt.show()

# 构建一个顺序模型
model = Sequential()
# 模型中添加一个全连接层
model.add(Dense(units=1, input_dim=1)) # activation = 'relu'
#sgd随机梯度下降，mse均方误差
model.compile(
    optimizer='sgd', 
    loss='mse',
    metrics=['accuracy']
    )

model.summary()

# 训练3001个批次
for step in range(3001):
    # 每一个批次
    cost = model.train_on_batch(x_data, y_data)
    if step%500==0:
        print("cost:",cost)

# 打印权值和偏置值
w, b = model.layers[0].get_weights()
print("w:",w," b:",b)

#x_data输入网络中，得到预测值y_pred
y_pred = model.predict(x_data)

# 显示随机点
plt.scatter(x_data, y_data)

# 显示预测结果
plt.plot(x_data, y_pred, 'r-', lw=3)
plt.show()