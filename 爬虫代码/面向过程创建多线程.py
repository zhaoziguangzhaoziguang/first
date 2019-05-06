# 面向过程


import threading
import time
def sing(a):
    print('线程为%s,接受过来的参数为%s'%(threading.current_thread().name,a))
    for x in range(6):
        print('我在唱舞娘')
        time.sleep(1)
def dance(a):
    print('线程为%s,接受过来的参数为%s'%(threading.current_thread().name, a))
    for x in range(6):
        print('我在跳钢管舞')
        time.sleep(1)
def main():
    a = '孙悟空'
    b= '唐僧'
    # 创建唱歌线程
    tsing = threading.Thread(target=sing, name='唱歌', args=(a,))
    # 创建跳舞线程
    tdance = threading.Thread(target=dance, name='跳舞', args=(a,))
    # 启动线程
    tsing.start()
    tdance.start()
    # 让主线程等待子线程结束之后再结束
    tdance.join()
    tsing.join()
    # 这里是主线程在运行
    print('这是主线程')


if __name__ == '__main__':
    main()