#!/usr/bin/env python
# -*- coding: utf-8 -*-
#这个脚本用来测试把会函数的函数
#定义一个返回求和函数的函数
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1, 3, 5, 7, 9)
print f
print f()
