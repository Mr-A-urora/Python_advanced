"""
案例：演示单任务，前边不执行完毕，后边绝对无法执行
"""
def fun_A():
    for i in range(10):
        print('hello world!')

def fun_B():
    for i in range(10):
        print('hello python!')

fun_A()
print('-' * 34)
fun_B()
