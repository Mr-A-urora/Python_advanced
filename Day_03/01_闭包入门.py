"""
案例：闭包入门。

闭包解释：
    概述：
        内部函数使用了外部函数的变量，这样的写法就称为闭包。
    格式：
        def 外部函数名(形参列表):
            外部函数的(局部)变量

            def 内部函数名(形参列表):
                使用外部函数的变量

            return 内部函数名
    前提条件：
        1. 有嵌套
        2. 有引用
        3. 有返回
    细节：
        1.函数名 和 函数名() 是两个概念，前者表示 函数对象，后者表示 调用函数，获取返回值
"""
def get_sum(a, b):
    return a + b

print(get_sum)
print(get_sum(1, 2))

my_sum = get_sum
print(my_sum)
print(my_sum(1, 2))

print('-' * 23)


def fun_outer(num1):
    def fun_inner(num2):
        sum = num1 + num2
        print(f'求和结果：{sum}')

    return fun_inner

fun_inner = fun_outer(1)
fun_inner(2)

print('-' * 23)

fun_outer(1)(2)
