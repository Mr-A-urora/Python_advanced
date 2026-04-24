"""
案例：装饰器入门。

装饰器介绍：
    概述/作用：
        他的本质是1个闭包函数，目的是在不改变原有函数的基础上，对其功能做增强
    前提条件：
        1. 有嵌套
        2. 有引用
        3. 有返回
        4. 有额外功能
    装饰器的用法：
        格式1：传统写法：
            装饰后的函数名 = 装饰器名（被装饰的原函数名）
            装饰后的函数名（）

        格式2：语法糖
            在要被装饰的原函数上面，直接写 @装饰器名，之后直接调用原函数即可
需求：在发表评论前，都是需要先登录的
"""
def check_login(fn_name):   # fn_name: 被装饰的函数名（对象）
    def fn_inner():
        # 增加额外功能
        print('校验登录... 登录成功！')
        fn_name()
    return fn_inner

def comment():
    print('发表评论')

@check_login
def payment():
    print('充值中...')

# 传统方式
comment = check_login(comment)
comment()
print('-' * 34)

# 语法糖
payment()
