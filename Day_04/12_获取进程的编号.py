"""
案例：演示获取进程的编号
"""
import multiprocessing, time
import os

def coding(name, num):
    for i in range(1, num + 1):
        time.sleep(0.1)
        print(f'{name} 正在敲第 {i} 行代码...')
    print(f'p1进程的pid：{os.getpid()}, {multiprocessing.current_process().pid}, 父进程id(ppid)为：{os.getppid()}')

def music(name, count):
    for i in range(1, count + 1):
        time.sleep(0.1)
        print(f'{name} 正在听第 {i} 首歌...')
    print(f'p2进程的pid：{os.getpid()}, {multiprocessing.current_process().pid}, 父进程id(ppid)为：{os.getppid()}')

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=coding, args=('虚竹', 10))
    p2 = multiprocessing.Process(target=music, kwargs={'name' : '刘备', 'count' : 10})

    p1.start()
    p2.start()

    print(f'main进程的pid：{os.getpid()}, {multiprocessing.current_process().pid}, 父进程id(ppid)为：{os.getppid()}')
