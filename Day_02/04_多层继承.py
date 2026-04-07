"""
案例：演示多层继承
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

    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)

class TuSun(Prentice):
    pass

if __name__ == '__main__':
    TS = TuSun()

    TS.make_cake()
    TS.make_master_cake()
    TS.make_school_cake()
    