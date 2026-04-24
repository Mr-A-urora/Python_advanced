"""
案例：装饰器装饰_无参无返回的原函数

细节：装饰器的内部函数要和被装饰的原函数保持一致
    即：原函数是无参无返回的，则 装饰器的内部函数也必须是 无参无返回的
        原函数是有参有返回的，则 装饰器的内部函数也必须是 有参有返回的

需求：定义无参无返回的 get_sum() 求和函数，在不改变其代码的基础上，添加友好提示：正在努力计算中...
"""
def my_decorator(fun_name):
    def fun_inner():
        print('正在努力计算中...')
        fun_name()
    return fun_inner

@my_decorator
def get_sum():
    a = 10
    b = 20
    sum = a + b
    print(f"sum求和结果{sum}")

# 传统方式
# get_sum = my_decorator(get_sum)
# get_sum()

# 语法糖
get_sum()
