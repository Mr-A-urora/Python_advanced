"""
案例：演示类内如何获取对象的属性

需求：定义汽车类，创建该类对象，赋予颜色 和 轮胎数两个属性，并在类内访问该属性
"""
class Car:
    def run(self):
        print('汽车会跑')

    def show(self):
        print(f'我是 show 函数，对象的颜色：{self.color}，轮胎数：{self.num}')

car1 = Car()

car1.color = '红色'
car1.num = 4

print(f'颜色：{car1.color}, 轮胎数{car1.num}')

car1.run()
car1.show()

print('-' * 34)

car2 = Car()
car2.run()

# 报错
# car2.show()
