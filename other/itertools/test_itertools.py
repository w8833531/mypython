#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数。
#itertools模块提供的全部是处理迭代功能的函数，它们的返回值不是list，而是迭代对象，只有用for循环迭代的时候才真正计算。

#首先，我们看看itertools提供的几个“无限”迭代器：
import itertools
#natuals = itertools.count(1)
#for n in natuals:
#    print n

#repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数：
print "====itertools.repeat===="
ns = itertools.repeat('ABC', 10)
for n in ns:
    print n

#无限序列只有在for迭代时才会无限地迭代下去，如果只是创建了一个迭代对象，它不会事先把无限个元素生成出来，事实上也不可能在内存中创建无限多个元素。

#无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列：
print "=====itertools.takewhile====="
cs = itertools.count(1) 
ns = itertools.takewhile(lambda x: x <= 10, cs)
for c in ns:
    print c

#groupby()把迭代器中相邻的重复元素挑出来放在一起
print "=====itertools.groupby ======"
for key, group in itertools.groupby('AAABBBCCAAA'):
    print key, list(group)

#imap
print "===== itertools.imap ===="
for x in itertools.imap(lambda x, y: x * y, [10, 20, 30, 40, 50], itertools.count(1)):
    print x

#imap()实现了“惰性计算”，也就是在需要获得结果的时候才计算。类似imap()这样能够实现惰性计算的函数就可以处理无限序列
r = itertools.imap(lambda x: x * x, itertools.count())
for n in itertools.takewhile(lambda x: x < 10, r):
    print n
#imap()和map()的区别在于，imap()可以作用于无穷序列，并且，如果两个序列的长度不一致，以短的那个为准。
#注意imap()返回一个迭代对象，而map()返回list。当你调用map()时，已经计算完毕：
print itertools.imap(lambda x: x * x, itertools.count(1))
#print map(lambda x: x * x, itertools.count(1)) # 这是个死循环
