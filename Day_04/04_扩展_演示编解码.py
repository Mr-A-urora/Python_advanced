"""
案例：演示编解码

细节：英文字母，数字，特殊符号无论什么码表都只占1个字节，中文在gbk占两个字节，utf-8中占3个字节
"""
s1 = '黑马123abCD@#!'

print(s1.encode())
print(s1.encode('utf-8'))
print(s1.encode('gbk'))
print('-' * 34)

bys = b'\xe9\xbb\x91\xe9\xa9\xac123abCD@#!'
print(type(bys))

s2 = bys.decode()
s3 = bys.decode('utf-8')
print(s2)
print(s3)
print('-' * 34)

s4 = bys.decode('gbk')
print(s4)
