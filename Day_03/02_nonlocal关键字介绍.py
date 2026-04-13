"""
案例：nonlocal 关键字介绍

nonlocal：
    它是Python内置的关键字，可以实现 在内部函数中 修改外部函数的 变量值

需求：编写一个闭包，让内部函数访问外部函数的参数 a = 100，并观察结果。
"""
def fun_outer():
    a = 100

    def fun_inter():
        nonlocal a
        a += 1
        print(f'a：{a}')

    return fun_inter

if __name__ == '__main__':
    fun_inner = fun_outer()
    fun_inner()
    fun_inner()
    fun_inner()
