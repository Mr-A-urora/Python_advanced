"""
该文件用于完成学生管理系统的具体业务的操作，即：增删改查，保存学生信息等...
"""
import time
from student import Student

class StudentCMS:
    def __init__(self):
        self.stu_list = []

    @staticmethod
    def show_view():
        print('*' * 23)
        print('学生管理系统V2.0版')
        print('\t1.添加学生信息')
        print('\t2.删除学生信息')
        print('\t3.修改学生信息')
        print('\t4.查询单个学生信息')
        print('\t5.查询所有学生信息')
        print('\t6.保存学生信息')
        print('\t0.退出系统')
        print('*' * 23)

    def add_student(self):
        name = input('请输入学生姓名：')
        gender = input('请输入学生性别：')
        age = int(input('请输入学生年龄：'))
        phone = input('请输入学生电话：')
        description = input('请输入学生描述信息：')

        stu = Student(name, gender, age, phone, description)
        self.stu_list.append(stu)

        print(f'添加 {name} 信息成功！\n')

    def del_student(self):
        del_name = input('请输入要删除的学生姓名：')

        for stu in self.stu_list:
            if stu.name == del_name:
                self.stu_list.remove(stu)
                print(f'已成功删除 {del_name} 信息！\n')
                break
        else:
            print(f'未查询到 {del_name} 信息！\n')

    def update_student(self):
        update_name = input('请输入要修改的学生姓名：')

        for stu in self.stu_list:
            if stu.name == update_name:
                stu.age = int(input('请输入修改后的年龄：'))
                stu.gender = input('请输入修改后的性别：')
                stu.phone_num = input('请输入修改后的手机号码：')
                stu.description = input('请输入修改后的描述信息：')

                print(f'已成功删修改 {update_name} 信息！\n')
                break
        else:
            print(f'未查询到 {update_name} 信息！\n')


    def search_one_student(self):
        search_name = input('请输入要查询的学生姓名：')

        for stu in self.stu_list:
            if stu.name == search_name:
                print(f'已成功查询 {search_name} 信息！')
                print(stu, end='\n\n')
                break
        else:
            print(f'未查询到 {search_name} 信息！\n')

    def search_all_student(self):
        if len(self.stu_list) == 0:
            print('暂无学生信息，请添加后查询。\n')
        else:
            for stu in self.stu_list:
                print(stu)
            print('已查询到所有学生信息！\n')

    def save_student(self):
        with open('./stu_data.txt', 'w', encoding='utf-8') as dest_f:
            stu_dict = [stu.__dict__ for stu in self.stu_list]

            dest_f.write(str(stu_dict))

    def load_student(self):
        try:
            with open('./stu_data.txt', 'r', encoding='utf-8') as src_f:
                stu_data = src_f.read()
                # 将字符串转为列表
                stu_list = eval(stu_data)
                if len(stu_list) == 0:
                    stu_list = []
                self.stu_list = [Student(**stu_dict) for stu_dict in stu_list]
        except:
            with open('./stu_data.txt', 'w', encoding='utf-8') as src_f:
                pass

    def start(self):
        self.load_student()

        while True:
            time.sleep(1)
            StudentCMS.show_view()
            imput_num = input('请输入您要操作的编号：')

            if imput_num == '1':
                self.add_student()
            elif imput_num == '2':
                self.del_student()
            elif imput_num == '3':
                self.update_student()
            elif imput_num == '4':
                self.search_one_student()
            elif imput_num == '5':
                self.search_all_student()
            elif imput_num == '6':
                self.save_student()
                print('学生信息已保存！\n')
            elif imput_num == '0':
                result = input('您确定要退出吗？（Y/N）\n')
                if result.lower() == 'y':
                    # 自动保存
                    self.save_student()
                    print('谢谢您的使用，期待下次再会！\n')
                    break
            else:
                print('录入有误，请重新录入！\n')

if __name__ == '__main__':
    cms = StudentCMS()
    cms.start()
