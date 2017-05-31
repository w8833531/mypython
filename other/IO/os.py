#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Python的os模块封装了操作系统的目录和文件操作，要注意这些函数有的在os模块中，有的在os.path模块中。
import os
print 'os.name:', os.name
print 'os.uname:', os.uname
print 'os.environ:', os.environ
print "os.getenv('PATH'):", os.getenv('PATH')
print "os.path.abspath('.'):", os.path.abspath('.')
#print "os.mkdir('/root/mypython/IO/test')", os.mkdir('/root/mypython/IO/test')
#print "os.rmdir('/root/mypython/IO/test')", os.rmdir('/root/mypython/IO/test')
print "os.path.split('/root/mypython/IO/aaa.txt')", os.path.split('/root/mypython/IO/aaa.txt')
#print "os.rename('bbb.txt', 'ccc.txt')", os.rename('bbb.txt', 'ccc.txt')
#最后看看如何利用Python的特性来过滤文件。比如我们要列出当前目录下的所有目录，只需要一行代码：
print [x for x in os.listdir('.') if os.path.isfile(x)]
#要列出所有的.py文件，也只需一行代码：
print [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']

#练习：编写一个search(s)的函数，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出完整路径：
def search(name, path='.'):
    found = []
    for f in [os.path.abspath(os.path.join(path, x)) for x in os.listdir(path)]:
        if os.path.isfile(f) and os.path.split(f)[1].find(name) != -1:
            found.append(f)
    for path in [x for x in os.listdir(path) if os.path.isdir(x)]:
        found.extend(search(name, path))
    return found

l = search('aaa')
for aa in l:
    print aa
