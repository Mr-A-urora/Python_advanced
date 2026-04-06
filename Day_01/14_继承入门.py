"""
案例：继承入门

需求：定义父类（男，散步），定义子类，继承父类
"""
class Father:
    def __init__(self):
        self.gender = '男'

    def walk(self):
        print('饭后走一走，活到九十九！')

    def smoking(self):
        print('抽烟有害健康！')

class Son(Father):
    pass

s = Son()

print(f'性别：{s.gender}')
s.walk()
s.smoking()
