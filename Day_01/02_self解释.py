"""
案例：self关键字介绍

self介绍：
    概述：它是Python内置的关键字，用于表示本类当前对象的引用
    作用：1个类是可以有多个对象的，这多个对象都可以通过 对象名. 的方式访问类中的行为（函数）
        函数默认有self属性，函数通过self来区分到底是哪个对象调用的该函数

需求：定义汽车类，创建多个该类的的对象，看看打印结果。
"""
class Car:
    def run(self):
        print('汽车会跑！')
        print(f'我是run的函数，self的值为{self}')

car1 = Car()
print(f'car的对象的地址值：{car1}')
print(f'car的对象的地址值：{id(car1)}')

car1.run()
print('-' * 34)

car2 = Car()
print(f'car2的对象的地址值：{car2}')
print(f'car2的对象的地址值：{id(car2)}')

car2.run()
