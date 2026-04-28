"""
案例：演示正则替换

回顾正则的使用步骤：
        1. 导包
            import re
        2. 正则匹配
            result = re.match('正则表达式', '要校验的字符串')   从前往后依次匹配，只要能匹配即可
            result = re.search('正则表达式', '要校验的字符串')   分段查找
            result = re.compile('正则表达式').sub(替换后的内容, 要被替换的字符串)
        3. 获取匹配结果
            result.group()
"""
import re

s = '开心你就大声笑,哈哈,呵呵,嘿嘿,嘻嘻,桀桀桀,啦啦啦'

result = re.compile('哈|呵|嘿|嘻|桀').sub('*', s)
print(result)

print("-" * 34)

result = re.sub('哈|呵|嘿|嘻|桀', '@', s)
print(result)
