"""
案例：演示自定义迭代器

迭代器介绍：
    概述：
        自定义的类，只要重写了 __iter__() 和 __next__() 方法，就可以称为 迭代器
    目的：
        隐藏底层的逻辑，让用户使用更方便
        惰性加载，用的时候才会获取

需求：模拟range(1, 6)，自定义 迭代器实现同等逻辑
"""
# 场景一：回顾range()用法
for i in range(1,6):
    print(i)
print('-' * 34)

# 场景二：自定义迭代器
class MyIterator:
    # 通过init魔法方法，初始化属性。
    def __init__(self, start, end):
        self.current_value = start
        self.end = end

    # 重写iterator魔法方法，返回当前对象
    def __iter__(self):
        return self

    # 重写next魔法方法，返回当前值，并更新当前值
    def __next__(self):
        if self.current_value >= self.end:
            raise StopIteration

        self.current_value += 1
        return self.current_value - 1

for i in MyIterator(1,6):
    print(i)

print('-' * 34)

my_itr = MyIterator(10,13)
print(next(my_itr))
print(next(my_itr))
print(next(my_itr))
# print(next(my_itr))
