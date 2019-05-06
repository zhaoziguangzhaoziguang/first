import matplotlib.pyplot as plt
import numpy as np
import torch
import torch.nn.functional as F
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import TensorDataset, DataLoader

# 生成1000个数据
x = np.linspace(-20, 20, 1000)


# 定义一个函数，根据给定的函数得到y值
def result():
    z = []
    for a in x:
        if a == 0:
            y = 1
            z.append(y)
        else:
            y = np.sin(a) / a
            z.append(y)
    return z


# 将y变成矩阵的形式，否则，无法将y转化为张量
y = np.array(result())
# 分别将x，y，转化为张量
inputs = torch.from_numpy(x)
targets = torch.from_numpy(y)
# 对inputs，targets进行变形
inputs = inputs.reshape(1000, 1)
targets = targets.reshape(1000, 1)
# 将inputs，targets转化为单精度类型的，不然训练时会报错
inputs = inputs.float()
targets = targets.float()
# 将inputs，targets作为参数传给TensorDataset，返回一个元组，第一个元素表示的
# 是inputs的值，第二个元素表示的是targets的值
train_ds = TensorDataset(inputs, targets)
# 分批次进行训练，批次大小为5
batch_size = 5
# 创建一个数据加载器，这个加载器会将数据分成指定的批次，通常和for-in搭配使用
train_dl = DataLoader(train_ds, batch_size=batch_size, shuffle=True)
# 快速定义一个神经网络
net = nn.Sequential(
    nn.Linear(1, 10),
    nn.ReLU(),
    nn.Linear(10, 1)
)
# 使用mse函数作为优化的目标函数
loss_fn = F.mse_loss
# 使用随机梯度下降法进行优化神经网络的参数
opt = optim.SGD(net.parameters(), lr=1e-5)
num_epochs = 500
epoch_x = []
loss_y = []
for epoch in range(num_epochs):
    # 对数据进行分批次训练
    for xb, yb in train_dl:
        pred = net(xb)
        loss = loss_fn(pred, yb)
        opt.zero_grad()
        loss.backward()
        opt.step()
    if epoch % 5 == 0:
        epoch_x.append(epoch)
        # 这里的loss是每个batch的mse，以batch的mse代表整体的mse
        loss_y.append(loss)
        print('Epoch[{}/{}], Loss:{:.4f}'.format(epoch, num_epochs, loss))
plt.plot(epoch_x, loss_y)
plt.show()
