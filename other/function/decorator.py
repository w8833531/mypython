#!/usr/bin/env python
# -*- coding: utf-8 -*-
#这个脚本用来测试函数的装饰器
def now(*args, **kw):
    print '2013-12-25'

#wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用。在wrapper()函数内，首先打印日志，再紧接着调用原始函数。
def log(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper
now = log(now)
print now(1,23,'aaa',ss=33)

#如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print '%s %s():' %(text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator

now = log('execute')(now)
print now()

#编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志
print '##################################################'
import functools
from types import FunctionType

def _spider(func, text=''):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('begin %s %s():' % (text, func.__name__))
        data = func(*args, **kw)
        print('end %s %s():' % (text, func.__name__))
        return data
    return wrapper

def log1(*args, **kwargs):
    if args is None or len(args) is 0 or not isinstance(args[0], FunctionType):
        return lambda func: _spider(func, *args, **kwargs)
    return _spider(*args, **kwargs)
@log1()
def now1(*args, **kw):
    print '2013-12-25'
now1()
