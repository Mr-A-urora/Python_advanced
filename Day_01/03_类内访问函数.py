"""
案例：演示通过 self关键字实现 在类内访问其他函数

self关键字：
    概述：代表本类当前对象的引用，哪个对象调用，self就代表谁
    作用：用于实现函数区分不同对象的

需求：定义汽车类，类内有run()函数，并在work()中调用run()中函数，创建该类对象，调用上述的函数
"""
class Car:
    def run(self):
        print(f'{self} 汽车在跑...')

    def work(self):
        print(f'我是work函数， 我的self值为：{self}')
        self.run()

car1 = Car()
print(f'car1对象：{car1}')
car1.run()
print('-' * 34)
car1.work()

print('=' * 34)

car2 = Car()
print(f'car2对象：{car2}')
car2.run()
print('-' * 34)
car2.work()
