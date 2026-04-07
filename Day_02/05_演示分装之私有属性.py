"""
案例：演示分装之私有属性

私有格式：
    __属性名
    __函数名（）

需求：小明把技术给徒孙的时候，不希望把自己的私房钱给徒孙，代码模拟
"""
class Prentice:
    def __init__(self):
        self.kongfu = '[黑马煎饼果子配方]'
        self.__money = 20000

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

    # 针对私有的属性，提供公共的访问方式
    def get_money(self):
        return self.__money

    # 修改私有属性的方法
    def set_money(self, money):
        self.__money = money

class TuSun(Prentice):
    pass

if __name__ == '__main__':
    TS = TuSun()

    print(TS.kongfu)
    TS.make_cake()

    print('-' * 34)

    # 报错：父类私有成员，子类无法万访问
    # print(TS.__money)

    # 通过父类提供的公共访问方式，访问父类的私有成员
    print(TS.get_money())
    TS.set_money(100)

    print('=' * 34)

    print(TS.get_money())
