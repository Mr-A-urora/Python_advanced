"""
案例：演示正则表达式之校验单个字符

正则表达式介绍：
    概述：
        正确的，符合特定规则的 字符串
        Regular Expression，正则表达式，简称：re
    细节：
        1. 学正则表达式，就是学正则表达式的规则，你不用背，网上一艘一大堆
        2. 关于正则我对大家的要求是，能用我们讲的规则，看懂别人写的式子，且会简单修改即可
        3. 正则不独属于Python，像Java，JavaScript，PHP，Go等都支持
    步骤：
        1. 导包
            import re
        2. 正则匹配
            result = re.match('正则表达式', '要校验的字符串')   从前往后依次匹配，只要能匹配即可
            result = re.search('正则表达式', '要校验的字符串')   分段查找
        3. 获取匹配结果
            result.group()
"""
import re

# result = re.match('.it', '你it')
result = re.match('.it', '\nit')

if result:
    print(result.group())
else:
    print('匹配失败！')
