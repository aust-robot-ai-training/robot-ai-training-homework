# -*- coding: utf-8 -*-
def convert(strs):
    res = strs.replace(":(", '🙁')
    res1 = res.replace(":)", '🙂')
    return res1

def main():
    strs = input('输入文本')
    result=convert(strs)
    print(result)
main()