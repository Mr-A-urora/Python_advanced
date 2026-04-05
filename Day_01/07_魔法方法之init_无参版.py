"""
案例：演示 init魔法方法的用法

常用的魔法方法：
    __init__() 在创建对象的时候，会自动触发该类的 __init__()函数
    __str__()
    __del__()

需求：定义汽车类，默认属性为：color=黑色，number=3
"""
class Car:
    def __init__(self):
        print('我是 无参 的 init 魔法方法')

        # 在init魔法方法中，初始化属性，则：该类中所有的对象，一创建，就有这些属性了。
        self.color = '黑色'
        self.num = 3

    def show(self):
         print(f'颜色：{self.color}，轮胎数：{self.num}')

# 创建汽车类对象会自动调用 __init__()函数
car1 = Car()

car1.color = '红色'
car1.num = 6
print(car1.color, car1.num)
car1.show()

print('-' * 34)

car2 = Car()
car2.show()
