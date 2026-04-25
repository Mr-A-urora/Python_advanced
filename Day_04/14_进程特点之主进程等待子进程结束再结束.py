"""
案例：演示进程特点之 默认情况下，主进程会等待子进程执行结束再结束

进程的特点：
    默认情况下，主进程会等待子进程执行结束再结束。
    如果要设置主进程结束，子进程同步结束，方式如下：
      思路1：设置了进程为 守护进程
      思路2：强制关闭子进程（可能会导致子进程变成僵尸进程，交由Python解释器自动回收，底层有init初始化进程来管理维护）
"""
import multiprocessing
import time

def work():
    for i in range(10):
        print('正在努力工作ing...')
        time.sleep(0.2)

if __name__ == '__main__':
    # 细节：进程的默认命名规则是：Process-编号，编号是从1开始的
    # p1 = multiprocessing.Process(target=work, name='刘亦菲')
    # print(f'p1进程的名字：{p1.name}')

    p1 = multiprocessing.Process(target=work)
    # 思路一：设置 p1 为守护进程
    p1.daemon = True
    p1.start()
    time.sleep(1)

    # 思路二：强制关闭子进程
    # p1.terminate()

    print('main进程结束了')