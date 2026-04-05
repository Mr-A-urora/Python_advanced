"""
案例：定义手机类，能开机，关节，拍照
"""
class Phone:
    def open(self):
        print(f'{self} 手机开机了')

    def shutdown(self):
        print(f'{self} 手机关机了')

    def take_photo(self):
        print(f'{self} 手机拍照了')

phone1 = Phone()
print(f'phone1的对象：{phone1}')
phone1.open()
phone1.take_photo()
phone1.shutdown()
print('-' * 34)

phone2 = Phone()
print(f'phone2的对象：{phone2}')
phone2.open()
phone2.take_photo()
phone2.shutdown()
