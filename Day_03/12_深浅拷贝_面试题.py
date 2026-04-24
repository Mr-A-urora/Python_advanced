"""
案例：深浅拷贝

总结：
    1. 所谓的深浅拷贝分别指的是：
        浅拷贝：copy模块的copy()函数
        深拷贝：copy模块的deepcopy()函数
    2. 深浅拷贝主要是针对于可变类型来讲的，深拷贝拷贝所有层（可变），浅拷贝只拷贝第1层（可变）
    如果是针对于不可变类型，则用法和普通赋值一样，并无区别
"""

import copy

def dm01_普通赋值():
    # b是a的别名，b和a都指向相同的内存空间
    a = 10
    b = a
    print('id(a)->', id(a))   # 0x01
    print('id(b)->', id(b))   # 0x01
    print('id(10)->', id(10))   # 0x01

    a = [1, 2, 3]
    b = [11, 22, 33]
    c = [a, b]
    d = c
    print('id(c)->', id(c))   # 0x03
    print('id(d)->', id(d))   # 0x03

def dm02_浅拷贝可变类型():
    a = [1, 2, 3]
    b = [11, 22, 33]
    c = [6, 7, a, b]

    d = copy.copy(c)
    print('id(c)->', id(c))   # 0x03
    print('id(d)->', id(d))   # 0x04
    print('id(c)和id(d)值不一样，说明浅拷贝第1层（最外面一层的数据）')

    print(id(c[2]))   # 0x01
    print(id(a))   # 0x01
    print("id(c[2])和id(a)值一样，说明浅拷贝第2层的数据")

    a[2] = 22
    print('c->', c)   # [6, 7, [1, 2, 22], [11, 22, 33]]
    print('d->', d)   # [6, 7, [1, 2, 22], [11, 22, 33]]

def dm03_浅拷贝不可变类型():
    a = (1, 2, 3)
    b = (11, 22, 33)
    c = (6, 7, a, b)

    d = copy.copy(c)
    print('id(c)->', id(c))   # 0x03
    print('id(d)->', id(d))   # 0x03
    print("id(c)和id(d)值一样，说明c和d指向相同的内存空间")

def dm04_深拷贝可变类型():
    a = [1, 2, 3]
    b = [11, 22, 33]
    c = [6, 7, a, b]

    d = copy.deepcopy(c)
    print('id(c)->', id(c))   # 0x03
    print('id(d)->', id(d))   # 0x04

    a[1] = 100
    b[1] = 800
    print(f'c: {c}')   # [6, 7, [1, 100, 3], [11, 800, 33]]
    print(f'd: {d}')   # [6, 7, [1, 2, 3], [11, 22, 33]]

def dm05_深拷贝不可变类型():
    a = (1, 2, 3)
    b = (11, 22, 33)
    c = (a, b)

    d = copy.deepcopy(c)
    print(id(c))   # 0x03
    print(id(d))   # 0x03
    print("c/d内存空间相同，说明c和d指向相同的内存空间")

if __name__ == '__main__':
    dm01_普通赋值()
    # dm02_浅拷贝可变类型()
    # dm03_浅拷贝不可变类型()
    # dm04_深拷贝可变类型()
    # dm05_深拷贝不可变类型()
