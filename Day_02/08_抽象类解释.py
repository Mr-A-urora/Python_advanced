"""
案例：演示抽象类的用法

抽象类解释：
    概述：
        在 Python 中，抽象类 = 接口，即：在抽象方法的类就是 抽象类，也叫 接口
        抽象方法 = 没有方法体的方法，即：方法体是 pass 修斯的
    作用：
        抽象类一般充当父类，用于指定行业规范，准则，具体的实现交由 子类 来完成
"""
class AC:
    def cool_wind(self):
        pass

    def hot_wind(self):
        pass

    def swing_wind(self):
        pass

class XiaoMi(AC):
    def cool_wind(self):
        print('小米 核心 制冷技术！')

    def hot_wind(self):
        print('小米 核心 制热技术！')

    def swing_wind(self):
        print('小米 静音左右摆风 技术！')

class Gree(AC):
    def cool_wind(self):
        print('格力 核心 制冷技术！')

    def hot_wind(self):
        print('格力 核心 制热技术！')

    def swing_wind(self):
        print('格力 静音左右摆风 技术！')

if __name__ == '__main__':
    xm = XiaoMi()
    gl = Gree()

    xm.cool_wind()
    xm.hot_wind()
    xm.swing_wind()

    print('-' * 34)

    gl.cool_wind()
    gl.hot_wind()
    gl.swing_wind()
