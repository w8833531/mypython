#!/usr/bin/env python
# -*- coding: utf-8 -*-
#这个脚本使用reduce函数来重写sum()及prod()函数
def fx(x,y):
    return x+y
def sum(num_list):
    return reduce(fx,num_list)
print sum(range(1,6))

def fy(x,y):
    return x * y
def prod(num_list):
    return reduce(fy,num_list)
print prod(range(1,6))
