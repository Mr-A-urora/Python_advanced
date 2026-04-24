"""
案例：多个装饰器装饰1个函数

细节：多个装饰器装饰1个函数，是按照 由内向外的顺序来装饰的，
    但如果你要是用 装饰器的写法来做，看到的效果是: 从上往下执行的

需求：发表评论千前需要先登录，再验证验证码
"""
def check_login(fun_name):
    def fun_inner():
        print('校验登录！')

        fun_name()
    return fun_inner

def check_code(fun_name):
    def fun_inner():
        print('校验验证码！')

        fun_name()
    return fun_inner

@check_login
@check_code
def comment():
    print('发表评论')

# 传统方法
# comment = check_code(comment)
# comment = check_login(comment)
# comment()

# 语法糖
comment()
