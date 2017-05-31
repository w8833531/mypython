#!/usr/bin/env python
#-*- coding: utf-8 -*-
#读文件操作
#像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object。除了file外，还可以是内存的字节流，网络流，自定义流等等。file-like Object不要求从特定类继承，只要写个read()方法就行。
try:
    f = open('./aaa.txt', 'r')
    print f.read()
finally:
    if f:
        f.close()
with open('./aaa.txt', 'r') as f:
    print f.readline()
    print f.readlines()

#读二进制文件
print '=======rb read======='
with open('./bbb.txt', 'rb') as f:
    print f.read()
    print type(f)

#写文件
with open('./aaa.txt', 'w') as f:
    f.write('Hello, world!')

#在Python中，文件读写是通过open()函数打开的文件对象完成的。使用with语句操作文件IO是个好习惯。
