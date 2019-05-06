import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
# 通过rcParams设置全局横纵轴字体的大小
mpl.rcParams['xtick.labelsize'] = 24
mpl.rcParams['ytick.labelsize'] = 24
np.random.seed(42)
# x轴采样点
x = np.linspace(0, 5, 100)
# 通过下面曲线加上噪声生成数据，所以拟合模型就用y
y = 2*np.sin(x) + 0.3*x**2
y_data = y + np.random.normal(scale=0.3, size=100)
plt.figure('data')
plt.scatter(x, y_data)
plt.figure('model')
plt.plot(x, y)
plt.figure('data&model')
# 通过‘k’指定线的颜色，lw指定线的宽度
# 第三个参数除了颜色也可以指定线形，比如‘r--’表示红色的虚线
plt.plot(x, y, 'k', lw=3)
plt.scatter(x, y_data)
plt.show()