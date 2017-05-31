#!/usr/bin/env python
#-*- coding: utf-8 -*-
#collections是Python内建的一个集合模块，提供了许多有用的集合类。

#namedtuple
#namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
#from collections import namedtuple
from collections import namedtuple
Point = namedtuple('Point',['x', 'y'])
p = Point(1, 2)
print p.x, p.y
print isinstance(p, Point)
print isinstance(p, tuple)

#deque
#使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。
#deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
from collections import deque
q = deque(['a','b','c'])
q.append('x')
q.appendleft('y')
print q

#defaultdict
#使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：
from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print dd['key1'] 
print dd['key2']

#Counter
#Counter是一个简单的计数器，例如，统计字符出现的个数：
from collections import Counter
c = Counter()
for ch in 'This is a Programming':
    c[ch] = c[ch] + 1
print c
