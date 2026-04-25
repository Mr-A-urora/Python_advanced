"""
案例：线程入门案例，一边听音乐，一边写代码

线程和进程的关系：
    1. 进程是CPU分配资源的基本单位，线程是CPU调度资源的最小单位
    2. 线程是依附于进程的，每个进程至少有1个线程（主线程栈）
    3. 进程间数据相互隔离，（同一个进程的）线程间数据可以共享
"""
import threading
import time

def coding(name, num):
    for i in range(1, num+1):
        time.sleep(0.1)
        print(f'{name} 正在敲第 {i} 遍代码...')

def music(name, count):
    for i in range(1, count+1):
        time.sleep(0.1)
        print(f'{name} 正在听第 {i} 首音乐！')

if __name__ == '__main__':
    t1 = threading.Thread(target=coding, args=('理想', 100))
    t2 = threading.Thread(target=music, kwargs={'count': 50, 'name': '李四'})

    t1.start()
    t2.start()
