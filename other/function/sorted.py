#!/usr/bin/env python
# -*- coding: utf-8 -*-
#sorted()函数就可以对list进行排序
num_list = [36, 5, 12, 9, 21]
print sorted(num_list)

#sorted()函数也是一个高阶函数，它还可以接收一个比较函数来实现自定义的排序,下面是一个倒序排序
def reversed_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    else:
        return 0
print sorted(num_list, reversed_cmp)

#生成一个随机number list,并进行sorted()排序
import random
print random.sample(range(1,101),100)
print sorted(random.sample(range(1,101),100),reversed_cmp)

#对字符时行排序
s_list = ['bob', 'about', 'Zoo', 'Credit']
def cmp_ignore_case(s1, s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0
print sorted(s_list, cmp_ignore_case)


