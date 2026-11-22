# -*- coding: utf-8 -*-


def main():
    strs = input('输入文本')
    
    def convert(strs):
        res=strs.replace(":(",'🙁')
        res1=res.replace(":)",'🙂')
        print(res1)
    convert(strs)

main()