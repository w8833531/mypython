#!/usr/bin/env python
# -*- coding: utf-8 -*-
#把f(x)函数应用在list range(1,11)的每一个元素上
def f(x):
    return x * x

print map(f,range(1,11))

#把一个list的每个数字转换成字符
print map(str, range(1, 11))

#把list中每个word改成首字母大写，其它小写
string_list = ['adam', 'LISA', 'barT']
print map(str.title,string_list)
