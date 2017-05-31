#!/usr/bin/env python
# -*- coding: utf-8 -*-

'使用模块'

__author__ = 'Larry Wu'

import sys

#导入模块时，还可以使用别名，这样，可以在运行时根据当前环境选择最合适的模块。比如Python标准库一般会提供StringIO和cStringIO两个库，这两个库的接口和功能是一样的，但是cStringIO是C写的，速度更快，所以，你会经常看到这样的写法：
try:
    import cStringIO as StringIO
except ImportError:
    import StringIO

#类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用
def _private_1(name):
    print '%s' % name

def _private_2(name):
    print 'Hello, %s' % name

#外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public
def test():
    #sys模块有一个argv变量，用list存储了命令行的所有参数
    args = sys.argv
    if len(args)==1:
        _private_1(args[0])
    elif len(args)==2:
        _private_2(args[1])
    else:
        print 'All arguments! %s' % args

#当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，而如果在其他地方导入该hello模块时，if判断将失败
if __name__=='__main__':
    test()
