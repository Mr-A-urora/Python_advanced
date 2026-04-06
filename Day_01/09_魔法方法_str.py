"""
案例：演示 init魔法方法的用法

常用的魔法方法：
    __init__() 在创建对象的时候，会自动触发该类的 __init__()函数
    __str__() 当用print()函数 打印对象的时候，会自动调用该对象（所在类）的 str 魔法方法。
              该魔法方法默认打印的是对象的地址值，无意义，一都会重写，改为打印对象的各个属性值。
    __del__()
"""
class Car:
    """
    该魔法方法用于给 汽车类 对象的属性赋值
    :param color: 车的颜色
    :param num: 车的轮胎数量
    """
    def __init__(self, color, num):
        self.color = color
        self.num = num

    def __str__(self):
        return f'颜色：{self.color}, 轮胎数：{self.num}'

# 创建汽车类对象会自动调用 __init__()函数
car1 = Car('绿色', 4)

print(car1)

print('-' * 23)

car2 = Car('红色', 6)

print(car2)
