#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Student(object):
    
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    #获取name & score
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    #设置name & score
    def set_name(self, name):
        self.__name = name
    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')
    #打印name & score    
    def print_score(self):
        print '%s: %s' % (self.__name, self.__score)
    #获取grade
    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

bart = Student('Bart Simpson', 97)
Larry = Student('Larry Wu', 87)
print 'bart object point to %s' % bart
print 'Student class point to %s' % Student 
#在增加__后，__name 和 __score 变成了私有变量，从实例外部已经完成正常访问
#print 'Score: %s   %s' % (bart.__name, bart.__score)
#只能通过print_score方法来访问了
bart.print_score()
#设置bart的成绩
bart.set_score(59)
bart.print_score()
print bart.get_grade()
Larry.print_score()
print Larry.get_grade()
