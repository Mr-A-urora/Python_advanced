"""
案例：演示单继承，即：1个子类继承自一个父类

故事1：一个摊煎饼的老师傅，研发了一套精湛的摊煎饼技术，师傅要把这套技术传授给他的徒弟，
"""
class Master:
    def __init__(self):
        self.kongfu = '[古法配方]'

    def make_cake(self):
        print(f'采用 {self.kongfu} 摊煎饼果子！')

class Prentice(Master):
    pass

if __name__ == '__main__':
    p = Prentice()

    p.make_cake()
