from keras import backend as K
from keras import Optimizers
from keras.opitimizers import Adam

class Adam(Optimizer):
    """
        参数：
            lr: float >= 0  学习率， 值越大表示权值调整动作越大，对应算法描述中的alpha
            beta_1: 接近1的常数，（有偏）一阶矩估计的指数衰减因子，体现惯性保持
            beta_2: 接近1的常数，（有偏）二阶矩估计的指数衰减因子，体现环境感知
            epsilon: 大于但接近0的数，放在分母上，避免出现除以0的情况
            decay: 学习速率衰减因子，用作更新lr使用，这样在逻辑回归的每个epoch中，学习率也会更新。
    """
    def __init__(self, lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-8, decay=0., **kwargs):
        super(Adam, self).__init__(**kwargs)
        self.iterations = K.variable(0) # 迭代次数变量
        self.lr = K.variable(lr)
        self.beta_1 = K.variable(beta_1)
        self.beta_2 = K.variable(beta_2)
        self.epsilon = epsilon
        self.decay = K.variable(decay)
        self.initial_decay = decay

    def get_updates(self, params, contraints, loss):
        grads = self.get_gradients(loss, params) # 计算梯度g_t
        self.updates = [K.update_add(self.iterations, 1)] # 迭代次数加1

        lr = self.lr
        if self.initial_decay > 0: # 如果初始学习速率衰减因子不为0， 则随着迭代次数增加，学习速率不断减小
            lr *= (1./self.decay * self.iterations)
        
        t = self.iterations + 1
        # 有偏估计到无偏估计的校正值
        # 这里将循环内的公共计算提到循环外面，提高速度
        lr_t = lr * (K.sqrt(1. - K.pow(self.beta_2, t))) / (1. - K.pow(self.beta_1, t)))
        shapes = [K.get_variable_shape(p) for p in params] # 获得权值形状
        ms = [K.zeros(shape) for shape in shapes] # 一阶矩估计初始值
        vs = [K.zeros(shape) for shape in shapes] # 二阶矩估计初始值
        self.weights = [self.iterations] + ms + vs

        for p, g, m, v in zip(params, grads, ms, vs):
            m_t = (self.beta_1*m) + (1.-self.beta-1)*g # 一阶矩估计
            v_t = (self.beta_2*v) + (1.-self.beta_2)*K.square(g) # 二阶矩估计
            p_t = p - lr_t*m_t / (K.sqrt(v_t) + self.epsilon) # 权值更新

            self.updates.append(K.update(m, m_t))
            self.updates.append(K.update(v, v_t))

            new_p = p_t
            # 对权值加约束
            if p in constrains:
                c = contrains[p]
                new_p = c(new_p)
            self.updates.append(K.update(p, new_p))
        return self.updates

    # 获取当前超参数
    def get_config(self):
        config = {'lr': float(K.get_value(self.lr)),
            'beta_1': float(K.get_value(self.beta_1)),
            'beta_2': float(K.get_value(self.beta_2)),
            'decay': float(K.get_value(self.decay)),
            'epsilon': self.epsilon
        }
        base_config = super(Adam, self).get_config()
        return dict(list(base_config.items()) + list(config.items()))

