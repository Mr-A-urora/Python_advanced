"""
案例：演示魔法方法之 init 有参版，实际开发常用

__init__()魔法方法，在创建对象的时候，会被自动调用，一般用于给该类对象的属性进行初始化

需求：创建汽车类，不给默认值，由汽车对象 外部各自赋值即可
"""
class Car:
    def __init__(self, color, number):
        """
        该魔法方法用于给 汽车类 对象的属性赋值
        :param color: 车的颜色
        :param number: 车的轮胎数量
        """
        self.color = color
        self.number = number

    def show(self):
        print(f'颜色：{self.color}，轮胎数：{self.number}')

car1 = Car('红色', 6)
car1.show()

print('-' * 34)

car2 = Car('绿色', 4)
car2.show()
