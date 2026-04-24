"""
案例：带参数的装饰器

细节：1. 1个装饰器的参数有且只能有1个
    2. 如果装饰器有多个参数，可以在该装饰器的外边再包裹一层，把该装饰器当作其内部函数返回即可

需求：定义一个既可以装饰减法，又可以装饰加法的装饰器 -> 即：带有参数的装饰器
"""
def logging(flag):
    def my_decorator(fun_name):
        def fun_inner(a, b):
            if flag == "+":
                print('正在努力计算 加法 中...')
            if flag == "-":
                print('正在努力计算 减法 中...')

            return fun_name(a, b)
        return fun_inner
    return my_decorator

@logging('+')
def get_sum(a, b):
    return a + b

@logging('-')
def get_sub(a, b):
    return a - b

print(get_sum(1, 2))

print('-' * 34)

print(get_sub(1, 2))
