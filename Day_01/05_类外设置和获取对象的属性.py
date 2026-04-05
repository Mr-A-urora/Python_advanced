"""
案例：演示在类外 如何获取 和 设置 对象的属性

需求：创建汽车类。设置为红色，四个轮胎，有跑的功能
"""
class Car:
    def run(self):
        print('汽车会跑！')

car1 = Car()
car1.run()

car1.color = 'red'
car1.num = 4

print(f'颜色：{car1.color}, 轮胎数：{car1.num}')
print('-' * 34)

car2 = Car()
car2.run()

# print(f'颜色：{car2.color}, 轮胎数：{car2.num}')，未传入。会报错
