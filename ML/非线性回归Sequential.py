'''
用keras实现非线性回归
用Sequential
'''
import keras
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD
import matplotlib.pyplot as plt

x = np.linspace(-0.5, 0.5, 200)
noise = np.random.normal(loc=0, scale=0.01, size=x.shape)
y = np.square(x) + noise

model = Sequential()
model.add(Dense(units=10, input_dim=1, activation='tanh'))
model.add(Dense(units=1, activation='tanh'))
sgd = SGD(lr=0.3) # 如果没有这一句，下面compile中的optimizer='sgd'，注意要加引号
model.compile(
    loss='mse',
    optimizer=sgd
)
model.summary()

for step in range(3000):
    cost = model.train_on_batch(x,y)
    if step%500==0:
        print("cost:",cost)


y_pred = model.predict(x)

plt.scatter(x,y)
plt.plot(x, y_pred, 'r-')
plt.show()