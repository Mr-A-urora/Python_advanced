"""
案例：演示子类重写父类功能

需求：小明掌握了老师傅和黑马的技术后，自己潜心钻研一套自己的独门配方的全新摊煎饼果子技术
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

if __name__ == '__main__':
    XM = Prentice()

    print(XM.kongfu)
    XM.make_cake()
