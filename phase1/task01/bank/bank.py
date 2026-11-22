import re

say=input("Please say: ")

# 去掉多余的空格
res=re.match('\s*',say)
if res:
    say=say.strip(res.group())

# 开始匹配
if say.startswith('hello') or say.startswith('Hello'):
    print('$0')



elif say.startswith('h') or say.startswith('H'):
    print('$20')



else:
    print('$100')





































