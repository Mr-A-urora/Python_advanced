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
"""
import sys
# 需求1：生成1 ~ 10之间的整数
my_generator = (i for i in range(1, 11))
print(my_generator)
print(type(my_generator))
print('-' * 34)

# 需求2：生成 1 ~ 10 之间的偶数
my_generator2 = (i for i in range(1, 11) if i % 2 == 0)
print(my_generator2)
print('-' * 34)

# 需求3：如何从生成器中获取数据
# 思路1：next()
print(next(my_generator2))
print(next(my_generator2))
print('-' * 34)

for i in my_generator2:
    print(i)
print('-' * 34)

# 验证生成器的目的，就是可以减少内存占用
my_list = [i for i in range(1000000)]
my_generator3 = (i for i in range(1000000))
print(type(my_list), type(my_generator3))

# 查看my_list的内存空间占用
print(f'my_list的内存占用：{sys.getsizeof(my_list)}')
print(f'my_generator3的内存占用：{sys.getsizeof(my_generator3)}')
