"""
案例：演示Python内置的dict属性

__dict__属性介绍：它是Python内置的属性，可以把对象转成字典形式

需求1：把学生对象 -> 字典形式，属性名做键，属性值做值。
需求2：把 [学生对象, 学生对象, 学生对象] -> [字典, 字典, 字典]
需求3：把字典转为学生对象
"""
from 学生管理系统_面向对象版.student import Student

s1 = Student('fla', 'saf', 23, 'fasf', 'asfwe')
print(s1)

my_dict = s1.__dict__
print(my_dict)
print(type(my_dict))

print('-' * 23)

s2 = Student('sadfw', 'sdfaw', 234, 'safwef', 'fawefwa')
stu_list = [s1, s2]

# 列表推导式：
list_dict = [stu.__dict__ for stu in stu_list]
print(list_dict)

print('-' * 23)

my_dict = {'name': 'fla', 'gender': 'saf', 'age': 23, 'phone_num': 'fasf', 'description': 'asfwe'}
# ** 依次根据键拿到每个值，然后做填充
s3 = Student(**my_dict)
print(s3)
