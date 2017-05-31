#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Python的class中还有许多这样有特殊用途的函数，可以帮助我们定制类。

#__str__  打印一个实例,定义好__str__()方法，返回一个好看的字符串
class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name: %s)' % self.name
    __repr__ = __str__
print Student('Michael')
s = Student('Larry')
print s

#__iter__方法，该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的next()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 #初始化两个计数器
    def __iter__(self):
        return self  #实例本身就是迭代对象，故返回自己
    def next(self):
        self.a, self.b = self.b, self.a + self.b #计算下一个值
        if self.a > 100:  #退出循环的条件
            raise StopIteration()
        return self.a #返回下一个值
    #要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：
    def __getitem__(self,n):
        if isinstance(n, int): #如果传入参数是int
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):#如果传入参数是切片
            start = n.start
            stop = n.stop
            L=[]
            a, b = 1, 1
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L
        
#试试把Fib实例作用于for循环
for n in Fib():
    print n
#按下标访问数列的任意一项
f = Fib()
print 'Fib\'s 第三个数: %s' % f[3]
print 'Fib\'s 第十个数: %s' % f[10]
print 'Fib\'s 第100个数: %s' % f[100]
print 'Fib\'s 第10到20个数是 %s' % f[10:20]

#__getattr__ 方法，动态返回一个属性。正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错。
#实际上可以把一个类的所有属性和方法调用全部动态化处理了，不需要任何特殊手段
#这种完全动态调用的特性有什么实际作用呢？作用就是，可以针对完全动态的情况作调用

#如果要写SDK，给每个URL对应的API都写一个方法，那得累死，而且，API一旦改动，SDK也要改。
#利用完全动态的__getattr__，我们可以写出一个链式调用：
class Chain(object):
    def __init__(self,path=''):
        self._path = path
    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))
    def __str__(self):
        return self._path
c = Chain()
print c.status.user.timeline.list


#__call__ 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用
class Student(object):
    def __init__(self, name):
        self.name = name
    def __call__(self):
        print('My name is %s.' % self.name)
s = Student('Larry')
#对实例进行直接调用就好比对一个函数进行调用一样，所以你完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没啥根本的区别。
print s()
print dir(Student)

#通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。
print 'class Student is %s' % callable(Student)
print 'class Chain is %s' % callable('Chain')
print 'class int is %s' % callable('int')
print 'class string is %s' % callable('string')
