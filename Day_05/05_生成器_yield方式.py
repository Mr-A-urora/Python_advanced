"""
案例：演示生成器之推导式写法

生成器介绍：
    概述：
        所谓的生成器就是基于 数据规则，用一部分再生成一部分，而不是一下子生成完所有
    目的：
        可以节省大量的内存
    实现方式：
        1. 推导式写法
        2. yield关键字

# 需求：通过yield方式，获取到生成器之 1 ~ 10 之间的整数
"""
def my_fun():
    for i in range(10):
        yield i

my_generator = my_fun()
print(type(my_generator))

print(next(my_generator))
print(next(my_generator))
