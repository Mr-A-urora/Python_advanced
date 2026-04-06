"""
案例：减肥案例

需求：小明同学当前体重是100kg，每当他跑步一次时，则会减少0.5kg；每当他大吃大喝一次时，则会增加2kg，请试着采用面向对象的方式完成案例
"""
class Student:
    def __init__(self):
        self.current_weight = 100

    def run(self):
        print('疯狂跑步...')
        self.current_weight -= 0.5

    def eat(self):
        print('大吃大喝一顿...')
        self.current_weight += 2

    def __str__(self):
        return f'当前体重：{self.current_weight} kg!'

if __name__ == '__main__':
    XM = Student()

    XM.run()
    XM.run()

    XM.eat()

    print(XM)