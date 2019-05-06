# 面向对象

import threading
import time

# 写一个类，继承自threading.Thread
class SingThread(threading.Thread):
    # 这个也是重写父类的__init__的方法
    def __init__(self, name, a):
    # 有时候不调用父类的__init__的方法，会出现错误，因为你不知道在父类中这个方法做了什么
    # 所以不调用可能会出问题，调用的话就不会出问题，完美的办法就是只要重写了这个
    # 方法就调用一下父类的
        super().__init__()
        self.name = name
        self.a = a

    # 这个函数只能叫做run，这是重写了父类的方法，start的时候，会自动执行这个方法
    def run(self):
        print('线程名字是%s,接收到的参数是%s' % (self.name, self.a))
        for x in range(6):
            print('我在唱七里香')
            time.sleep(1)


class DanceThread(threading.Thread):
    # 这个也是重写父类的__init__的方法
    def __init__(self, name, a):
    # 有时候不调用父类的__init__的方法，会出现错误，因为你不知道在父类中这个方法做了什么
    # 所以不调用可能会出问题，调用的话就不会出问题，完美的办法就是只要重写了这个
    # 方法就调用一下父类的
        super().__init__()
        self.name = name
        self.a = a
    # 这个函数只能叫做run,这是重写了父类的方法，start的时候，会自动执行这个方法
    def run(self):
        print('线程名字是%s,接收到的参数是%s' % (self.name, self.a))
        for x in range(6):
            print('我在跳广场舞')
            time.sleep(1)


def main():
    # 创建线程
    tsing = SingThread('sing', '猪八戒')
    tdance = DanceThread('dance', '猪悟能')
    # 线程启动
    tsing.start()
    tdance.start()
    # 让主线程等待子线程结束后再结束
    tsing.join()
    tdance.join()
    print('主线程和子线程全部结束')

if __name__ == '__main__':
    main()