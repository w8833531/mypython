#!/usr/bin/env python
# -*- coding: utf-8 -*-
#这个脚本用来测试高介函数filter 的功能

#去掉一个num list中的偶数
def is_odd(n):
    return n % 2 == 1
print filter(is_odd, range(1,101))

#删除一个字符串中的空格
def is_space(s):
    return not s == ' '
print filter(is_space, 'abcd eFe s  s')
