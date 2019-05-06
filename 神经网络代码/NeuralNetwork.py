'''这个程序展现了通过神经元创建了一个神经网络，这里只有前向传播
，没有参数的更新'''



import numpy as np

# 定义一个激活函数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# 创建一个神经元的类
class Neuron:
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias
    # 进行前向传播
    def feedforward(self, inputs):
        total = np.dot(self.weights, inputs) + self.bias
        return sigmoid(total)

# 创建一个神经网络的类
class OurNeuralNetwork:
    def __init__(self):
        weights = np.array([0, 1])
        bias = 0
        self.h1 = Neuron(weights, bias)
        self.h2 = Neuron(weights, bias)
        self.o1 = Neuron(weights, bias)

    def feedforward(self, x):
        out_h1 = self.h1.feedforward(x)
        out_h2 = self.h2.feedforward(x)
        out_o1 = self.o1.feedforward(np.array([out_h1, out_h2]))
        return out_o1

# 实例化一个神经网络
network = OurNeuralNetwork()
x = np.array([2, 3])
print(network.feedforward(x))
