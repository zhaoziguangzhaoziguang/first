'''这是一个二分类的神经网络，用到的损失函数是MSE，可见分类也是可以用
这个损失函数的'''

import numpy as np
import matplotlib.pyplot as plt


# 定义一个激活函数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


# 对sigmoid函数进行求导
def deriv_sigmoid(x):
    fx = sigmoid(x)
    return fx * (1 - fx)


# 定义损失函数
def mse_loss(y_true, y_pred):
    return ((y_true - y_pred) ** 2).mean()


# 定义一个神经网络的类
class OurNeuralNetwork:
    def __init__(self):
        # 随机初始化各层的权重和偏置
        self.w1 = np.random.normal()
        self.w2 = np.random.normal()
        self.w3 = np.random.normal()
        self.w4 = np.random.normal()
        self.w5 = np.random.normal()
        self.w6 = np.random.normal()
        self.b1 = np.random.normal()
        self.b2 = np.random.normal()
        self.b3 = np.random.normal()

    # 前向传播
    def feedforward(self, x):
        h1 = sigmoid(self.w1 * x[0] + self.w2 * x[1] + self.b1)
        h2 = sigmoid(self.w3 * x[0] + self.w4 * x[1] + self.b2)
        o1 = sigmoid(self.w5 * h1 + self.w6 * h2 + self.b3)
        return o1

    # 对网络进行训练，更新每层的权重和偏置，实际上就是通过反向传播进行更新参数
    def train(self, data, all_y_trues):
        learn_rate = 0.1
        epochs = 1000
        epoch_x = []
        loss_y = []
        for epoch in range(epochs):
            for x, y_true in zip(data, all_y_trues):
                sum_h1 = self.w1 * x[0] + self.w2 * x[1] + self.b1
                h1 = sigmoid(sum_h1)
                sum_h2 = self.w3 * x[0] + self.w4 * x[1] + self.b2
                h2 = sigmoid(sum_h2)
                sum_o1 = self.w5 * h1 + self.w6 * h2 + self.b3
                o1 = sigmoid(sum_o1)
                y_pred = o1
                d_L_d_ypred = -2 * (y_true - y_pred)
                d_ypred_d_w5 = h1 * deriv_sigmoid(sum_o1)
                d_ypred_d_w6 = h2 * deriv_sigmoid(sum_o1)
                d_ypred_d_b3 = deriv_sigmoid(sum_o1)
                d_ypred_d_h1 = self.w5 * deriv_sigmoid(sum_o1)
                d_ypred_d_h2 = self.w6 * deriv_sigmoid(sum_o1)
                d_h1_d_w1 = x[0] * deriv_sigmoid(sum_h1)
                d_h1_d_w2 = x[1] * deriv_sigmoid(sum_h1)
                d_h1_d_b1 = deriv_sigmoid(sum_h1)
                d_h2_d_w3 = x[0] * deriv_sigmoid(sum_h2)
                d_h2_d_w4 = x[1] * deriv_sigmoid(sum_h2)
                d_h2_d_b2 = deriv_sigmoid(sum_h2)
                # 更新权重和偏置
                self.w1 -= learn_rate * d_L_d_ypred * d_ypred_d_h1 * d_h1_d_w1
                self.w2 -= learn_rate * d_L_d_ypred * d_ypred_d_h1 * d_h1_d_w2
                self.b1 -= learn_rate * d_L_d_ypred * d_ypred_d_h1 * d_h1_d_b1
                self.w3 -= learn_rate * d_L_d_ypred * d_ypred_d_h2 * d_h2_d_w3
                self.w4 -= learn_rate * d_L_d_ypred * d_ypred_d_h2 * d_h2_d_w4
                self.b2 -= learn_rate * d_L_d_ypred * d_ypred_d_h2 * d_h2_d_b2
                self.w5 -= learn_rate * d_L_d_ypred * d_ypred_d_w5
                self.w6 -= learn_rate * d_L_d_ypred * d_ypred_d_w6
                self.b3 -= learn_rate * d_L_d_ypred * d_ypred_d_b3
            if epoch % 10 == 0:
                epoch_x.append(epoch)
                y_preds = np.apply_along_axis(self.feedforward, 1, data)
                loss = mse_loss(all_y_trues, y_preds)
                loss_y.append(loss)
                print("Epoch %d loss:%.3f" % (epoch, loss))
        plt.plot(epoch_x, loss_y)
        plt.show()


# 这里的数据都是经过预处理过得数据
data = np.array([
    [-2, -1],
    [25, 6],
    [17, 4],
    [-15, 6]
])
all_y_trues = np.array([
    1,
    0,
    0,
    1
])
# 实例化一个网络
network = OurNeuralNetwork()
# 传入数据进行训练
network.train(data, all_y_trues)
# 对网络进行一个小测试，对测试数据进行了同样的预处理
emily = np.array([-7, -3])
frank = np.array([20, 2])
print("Emily: %.3f" % network.feedforward(emily))
print("Frank: %.3f" % network.feedforward(frank))
