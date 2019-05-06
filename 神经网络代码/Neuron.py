'''这是对一个神经元的编码'''


import numpy as np

# 定义一个激活函数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# 创建一个神经元的类
class Neuron:
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias

    def feedforward(self, inputs):
        total = np.dot(self.weights, inputs) + self.bias
        return sigmoid(total)


weights = np.array([0, 1])
bias = 4
# 实例化神经元
n = Neuron(weights, bias)
x = np.array([2, 3])
print(n.feedforward(x))
