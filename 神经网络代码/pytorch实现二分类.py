# 用pytorch实现二分类


from sklearn import datasets
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import torch.optim as optim
import torch.utils.data as Data

# 创建一些数据
noisy_moons, labels = datasets.make_moons(n_samples=1000, noise=.05, random_state=10)
# 对数据进行分配
X_train, Y_train, X_test, Y_test = noisy_moons[: -200], labels[: -200], noisy_moons[-200:], labels[-200:]


# 创建一个神经网络的类
class classifer(nn.Module):
    def __init__(self):
        super(classifer, self).__init__()
        self.class_col = nn.Sequential(
            nn.Linear(2, 16),
            nn.ReLU(),
            nn.Linear(16, 16),
            nn.ReLU(),
            nn.Linear(16, 2)

        )

    def forward(self, x):
        out = self.class_col(x)
        return out


# 实例化一个神经网络
model = classifer()
loss_fn = nn.CrossEntropyLoss()
optimiser = optim.SGD(params=model.parameters(), lr=0.05)
# 将数据转化为tensor
X_train = torch.Tensor(X_train)
X_test = torch.Tensor(X_test)
Y_train = torch.Tensor(Y_train).long()
Y_test = torch.Tensor(Y_test).long()
torch_dataset = Data.TensorDataset(X_train, Y_train)
BATCH_SIZE = 25
loder = Data.DataLoader(
    dataset=torch_dataset,
    batch_size=BATCH_SIZE,
    shuffle=True,
)
loss_list = []
epoch_list = []
# 对网络进行训练 ，其中的'_'符号的意思是，因为有时需要给两个变量赋值，但是其中一个
# 没啥用，就用这个符号代替一个变量，这样也省的给变量起名字
for epoch in range(70):
    # 进行分批训练
    for _, (batch_x, batch_y) in enumerate(loder):
        optimiser.zero_grad()
        out = model(batch_x)
        loss = loss_fn(out, batch_y)
        loss.backward()
        optimiser.step()
    if epoch % 10 == 0:
        loss_list.append(loss)
        epoch_list.append(epoch)
        outputs_train = model(X_train)
        _, predicted_train = torch.max(outputs_train, 1)
        outputs_test = model(X_test)
        _, predicted_test = torch.max(outputs_test, 1)
        plt.figure()
        plt.subplot(121)
        plt.scatter(X_train[:, 0], X_train[:, 1], c=predicted_train)
        plt.subplot(122)
        plt.scatter(X_test[:, 0], X_test[:, 1], c=predicted_test)
        plt.show()
plt.plot(epoch_list, loss_list)
plt.show()
