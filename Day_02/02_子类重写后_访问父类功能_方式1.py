"""
案例：子类重写父类功能后，继续访问父类功能

思路：
    1. 父类名.父类函数名(self)   精准访问，想找哪个父类，就调用哪个父类
    2. super().父类函数名()     只能访问最近的那个父类，有就用，没有就往后继续查找

需求：很多顾客都希望能吃到徒弟做出的有自己独立品牌的煎饼果子，也有黑马配方技术的煎饼果子味道
"""
class Master:
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子！')

class School:
    def __init__(self):
        self.kongfu = '[黑马AI煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子！')

class Prentice(School, Master):
    def __init__(self):
        self.kongfu = '[独创煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子！')

    def make_master_cake(self):
        Master.__init__(self)
        Master.make_cake(self)

if __name__ == '__main__':
    XM = Prentice()

    print(XM.kongfu)
    XM.make_cake()
    XM.make_master_cake()

    print('-' * 34)

    XM.make_cake()
