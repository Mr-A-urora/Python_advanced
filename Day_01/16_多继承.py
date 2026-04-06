"""
案例：演示多继承

扩展：MRO机制
    Python中有MRO机制，可以查看某个对象在调用函数的顺序。

需求：小明是个爱学习的好孩子，想学习更多的摊煎饼果子的技术，于是，在百度搜索到黑马程序员学校，报班来培训学习摊煎饼果子技术
"""
class Master:
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'

    def make_cake(self):
        print(f'运用 {self.kongfu} 制作煎饼果子')

class School:
    def __init__(self):
        self.kongfu = '[黑马AI煎饼果子配方]'

    def make_cake(self):
        print(f'运用 {self.kongfu} 制作煎饼果子')

class Prentice(School, Master):
    pass

if __name__ == '__main__':
    XM = Prentice()

    XM.make_cake()

    print('-' * 34)

    # 查看mro机制的结果
    print(Prentice.mro()) # Prentice -> School -> Master -> object
    print(Prentice.__mro__)
