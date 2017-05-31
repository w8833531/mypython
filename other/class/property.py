#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Python内置的@property装饰器就是负责把一个方法变成属性调用,这样，可以来进行属性输入数据的check

class Student(object):
    @property
    def score(self):
        return self._score
    #@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作
    #我们在对实例属性操作的时候，就知道该属性很可能不是直接暴露的，而是通过getter和setter方法来实现的。
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100')
        self._score = value
    #不定义setter方法就是一个只读属性：
    @property
    def age(self):
        return 30
#@property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性。
s = Student()
s.score = 60
print s.score
print s.age
# s.score = 101  #报错ValueError: score must between 0 ~ 100

