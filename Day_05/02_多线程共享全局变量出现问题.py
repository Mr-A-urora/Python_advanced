"""
案例：演示多线程共享全局变量，可能出现的问题

多线程共享全局变量，出现问题的问题：
    累加次数不够

产生原因：
    线程1还没有来得及执行完（一个完整的动作）前，被线程2抢走了资源，就可能出问题

解决方案：
    加锁思想，即：互斥锁

细节：
    使用互斥锁对的时候，要在合适的时机释放所，否则可能出现 死锁 或者 锁不住 的情况

进程和线程的区别：
    1. 线程依赖进程
    2. 进程更消耗资源，不能共享全局变量，相对更稳定
    3. 线程更轻量级，可以共享全局变量，相对更灵活

需求：定义两个函数，分别对全局变量累加100w次，创建两个线程，关联这两个函数，执行看效果
"""
import threading

global_num = 0

# 创建锁对象
mutex = threading.Lock()

def target_fun1():
    # 加锁
    mutex.acquire()
    global global_num
    for i in range(1000000):
        global_num += 1
    print(f'target_fun1函数结果: {global_num}')
    # 释放锁
    mutex.release()

def target_fun2():
    mutex.acquire()
    global global_num
    for i in range(1000000):
        global_num += 1
    print(f'target_fun2函数结果: {global_num}')
    mutex.release()

if __name__ == '__main__':
    t1 = threading.Thread(target=target_fun1)
    t2 = threading.Thread(target=target_fun2)

    t1.start()
    t2.start()
