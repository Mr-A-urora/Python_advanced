"""
案例：演示多态入门

多态的前提条件：
    1. 要有继承
    2. 要有方法重写，不然多态没意义
    3. 要有父类引用指向子类对象
"""
class Animal:
    def speak(self):
        print('动物会叫！')

class Dog(Animal):
    def speak(self):
        print('狗叫：汪汪汪！')

class Cat(Animal):
    def speak(self):
        print('猫叫：喵喵喵！')

class Car:
    def speak(self):
        print('车叫：嘀嘀嘀！')

def make_noise(an):
    an.speak()

if __name__ == '__main__':
    # an:Animal = Dog()   # 父类引用指向子类对象

    d = Dog()
    c = Cat()
    car = Car()

    make_noise(d)
    make_noise(c)

    print('-' * 34)

    make_noise(car)
