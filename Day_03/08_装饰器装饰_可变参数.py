"""
案例：装饰器装饰_可变参数

细节：装饰器的内部函数要和被装饰的原函数保持一致
    即：原函数是无参无返回的，则 装饰器的内部函数也必须是 无参无返回的
        原函数是有参有返回的，则 装饰器的内部函数也必须是 有参有返回的

需求：定义1个可以计算多个数据和字典value值和的函数，并给其友好提示
"""
def my_decorator(fun_name):
    def fun_inner(*args, **kwargs):
        print('正在努力计算中...')
        return fun_name(*args, **kwargs)
    return fun_inner

@my_decorator
def get_sum(*args, **kwargs):
    """
    该函数用于计算 数字列表 和 字典value值 之和
    :param args: 数字列表， *args -> 接收所有的位置参数，封装到 元组中
    :param kwargs: 字典，键是字符串，值是数字，**kwargs -> 接收所有的关键字参数，封装到 字典
    :return: 结果之和
    """
    # sum = 0
    #
    # for i in args:
    #     sum += i
    # for v in kwargs.values():
    #     sum += v
    #
    # return sum

    return sum(args) + sum(kwargs.values())

sum = get_sum(1, 2, 3, a=4, b=5, c=6)
print(sum)
