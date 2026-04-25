"""
案例：演示多进程入门案例

多任务目的：
    它属于多任务的一种实现方式，目的是充分利用CPU资源，提高程序执行效率

实现方式：
    1. 导包
    2. 创建进程对象，关联目标函数
    3. 启动进程
"""
import multiprocessing
import time

def coding():
    for i in range(1, 11):
        time.sleep(0.1)
        print(f'正在敲第 {i} 遍代码！')

def music():
    for i in range(1, 11):
        time.sleep(0.1)
        print(f'正在听第 {i} 遍音乐......')

# 细节：通过main进程（主进程）来创建子进程
if __name__ == '__main__':
    # 进程p1关联 coding函数，p1进程抢到（CPU资源了），就会执行这个函数
    p1 = multiprocessing.Process(target=coding)
    p2 = multiprocessing.Process(target=music)

    p1.start()
    p2.start()
