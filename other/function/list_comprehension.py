#!/usr/bin/env python
# -*- coding: utf-8 -*-

#用range函数生成list
print range(11)

#用append函数生成list
L=[]
for x in range(1,11):
    L.append(x * x)
print L

#使用一行语句生成一个list
print [ x * x for x in range(1,11)]

#在上面的语句加个if条件
print [ x * x for x in range(1,11) if x % 2 == 0]

#两层循环
print [ m + n for m in 'ABC' for n in 'XYZ']

#列出当前目录所有文件
import os
print [d for d in os.listdir('.')]

#dict 转 list
d = {'x': 'A', 'y': 'B', 'z': 'C' }
print [k + '=' + v for k, v in d.iteritems()]

#转换list中数据
L = ['Hello', 'World', 'IBM', 'Apple']
print [s.lower() for s in L]
