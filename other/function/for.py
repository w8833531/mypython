#!/usr/bin/env python
# -*- coding: utf-8 -*-

#List Iteration迭代
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print name
sum=0
for x in range(100):
    sum = sum + x
print sum

#Dict Iteration迭代
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print key,d[key]

for k,v in d.iteritems():
    print k,v

#Iterable 测试
from collections import Iterable
print isinstance(d, Iterable)
print isinstance('abcd', Iterable)
print isinstance(123, Iterable)

#enumerate函数把一个list 变成索引元素对
for i, ch in enumerate('abcdDSC'):
    print i, ch

#print list ,list的值为一个元组tuple
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print x, y
