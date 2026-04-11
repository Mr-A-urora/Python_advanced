"""
该文件用于记录学生类，学生的属性信息为：姓名，年龄，性别，手机号，描述信息
"""
class Student:
    def __init__(self, name, gender, age, phone_num, description):
        """
        该魔法方法，用于初始化 属性信息。
        :param name: 姓名
        :param age: 性别
        :param gender: 年龄
        :param phone_num: 手机号
        :param description: 描述信息
        """
        self.name = name
        self.gender = gender
        self.age = age
        self.phone_num = phone_num
        self.description = description

    def __str__(self):
        """
        该魔法方法用于打印学生信息
        :return:
        """
        return f'姓名：{self.name}，年龄：{self.age}, 性别：{self.gender}，手机号：{self.phone_num}，描述信息：{self.description}'

if __name__ == '__main__':
    s = Student('乔峰', '38', '男', '1234567899', '丐帮帮主')
    print(s)
