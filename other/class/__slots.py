#!/usr/bin/env python
# -*- coding: utf-8 -*-
#动态绑定允许我们在程序运行的过程中动态给class加上功能
class Student(object):
    pass
#给实例绑定一个属性name
s = Student()
s.name = 'Michael'
print s.name

#还可以尝试给实例绑定一个方法：
def set_age(self, age):
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s, Student)  #给实例绑定一个方法
s.set_age(25)
print s.age

#给一个实例绑定的方法，对另一个实例是不起作用的
s2 = Student()
  #s2.set_age(25) #报错

#给一个class 绑定方法, 动态绑定允许我们在程序运行的过程中动态给class加上功能
def set_score(self, score):
    self.score = score
Student.set_score = MethodType(set_score, None, Student)
s.set_score(100)
s2.set_score(98)
print s.score
print s2.score

## 使用__slots__限制class的属性
class Student(object):
    __slots__ = ('name', 'age')
s = Student()
s.name = 'Michael'
s.age = 25
#s.score = 99 #报错

#使用__slots__要注意，__slots__定义的属性仅对当前类起作用，对继承的子类是不起作用的：
class GraduateStudent(Student):
    pass
g = GraduateStudent()
g.score = 99
print g.score
#除非在子类中也定义__slots__，这样，子类允许定义的属性就是自身的__slots__加上父类的__slots__
class GraduateStudent1(Student):
    __slots__ = ()
    pass
d = GraduateStudent1()
#d.score = 98 #报错
