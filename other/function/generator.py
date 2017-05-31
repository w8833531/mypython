#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Note: 这个脚本用来测试生成器功能
#生成器: 如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器（Generator）。

#创建一个generator
#只要把一个列表生成式的[]改成()，就创建了一个generator
g = ( x * x for x in range(10))
#直接print ，显示结果为空
print g
#正确的方式是用迭代方式打印
for n in g:
    print n

#用生成器来计算一个斐波拉契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
for n in fib(16):
    print n



