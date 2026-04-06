"""
案例：演示 init魔法方法的用法

常用的魔法方法：
    __init__() 在创建对象的时候，会自动触发该类的 __init__()函数
    __str__() 当用print()函数 打印对象的时候，会自动调用该对象（所在类）的 str 魔法方法。
              该魔法方法默认打印的是对象的地址值，无意义，一都会重写，改为打印对象的各个属性值。
    __del__() 当.py文件执行结束，或者手动 del 释放对象资源，会自动调用该函数
"""
class Car:
    def __init__(self, brand):
        self.brand = brand

    def __str__(self):
        return f'品牌：{self.brand}'

    def __del__(self):
        print(f'{self} 对象被删除了！')

car1 = Car('小米 SU7 Ultra')

print(car1)
print(car1.brand)

print('-' * 23)

del car1
print('程序结束！')
