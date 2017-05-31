#!/usr/bin/env python
# -*- coding=utf-8 -*-
import math
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
xx=float(raw_input(u'请输入一个自然数:'.encode('utf-8')).decode('utf-8'))
print '%.2f' %  my_abs(xx)

def move(x, y, step, angle=0):
    print angle
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print x,y

def power(x, n=2):
    s = 1
    for i in range(0,n):
        print i
        s = s * x
    return s

print power(xx,3)

def enroll(name, gender, age=6, city='Beijing'):
    print 'name:', name
    print 'gender:', gender
    print 'age:', age
    print 'city:', city

enroll('Larry', 'M', city='ShangHai')

def cacl(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print cacl(1, 3, 5,7,9)

def person(name, age, **kw):
    print 'name:', name, 'age:', age, 'other:', kw

person('Adam', 45, gender='M', job='Engineer')
