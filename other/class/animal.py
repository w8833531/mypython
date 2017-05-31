#!/usr/bin/env python
# -*- coding: utf-8 -*-
#这个脚本用来测试class 的继承和多态

class Animal(object):
    def run(self):
        print 'Animal is running...'
#当我们需要编写Dog和Cat类时，就可以直接从Animal类继承：
#当子类和父类都存在相同的run()方法时，我们说，子类的run()覆盖了父类的run()，在代码运行的时候，总是会调用子类的run()。这样，我们就获得了继承的另一个好处：多态。
class Dog(Animal):
    def run(self):
        print 'Dog is running...'

class Cat(Animal):
    def run(self):
        print 'Cat is running...'

dog = Dog()
dog.run()

cat = Cat()
cat.run()

#重要：当我们定义一个class的时候，我们实际上就定义了一种数据类型。我们定义的数据类型和Python自带的数据类型，比如str、list、dict没什么两样：
a = list() # a是list类型
b = Animal() # b是Animal类型
c = Dog() # c是Dog类型
#isinstance()就可以告诉我们，一个对象是否是某种类型,isinstance()判断的是一个对象是否是该类型本身，或者位于该类型的父继承链上
print 'a is list type? %s' % isinstance(a, list)
print 'b is Animal type? %s' % isinstance(b, Animal)
print 'c is Dog type? %s' % isinstance(c, Dog)
print 'c is Animal type? %s' % isinstance(c, Animal)

#并且还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是str或者unicode：
print '\'a\' is a str %s' % isinstance('a',(str,unicode))
print 'u\'a\' is a unicode %s' % isinstance(u'a',(str,unicode))


#我们来判断对象类型，使用type()函数
print 'a type is %s' % type(a)
print 'b type is %s' % type(b)
print 'c type is %s' % type(c)

#最后注意到有一种类型就叫TypeType，所有类型本身的类型就是TypeType
import types
aa = type(int)==type(str)==types.TypeType
print 'int str type is TypeType %s' % aa

#如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的listdirid
print 'c class include %s' % dir(c)

#配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态
print 'obj c hasattr run %s' % hasattr(c, 'run')
print 'obj c hasattr run1 %s' % hasattr(c, 'run1')
print 'obj c setattr run1'
setattr(c,'run1', 19)
print 'obj c hasattr run1 %s' % hasattr(c, 'run1')
print 'obj c getattr run1 %s' % getattr(c, 'run1')
