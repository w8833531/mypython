#!/usr/bin/env python
# -*- coding: utf-8 -*-
#如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如XML，但更好的方法是序列化为JSON，因为JSON表示出来就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便。

import json
import os
d = dict(name='小红', age=20, score=88)
print 'DATA:', d
#dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个file-like Object。
print 'Json Dump:', json.dumps(d).encode('utf-8')
with open('./json.txt', 'w') as f:
    json.dump(d, f)
    print 'write to ./json.txt'
#要把JSON反序列化为Python对象，用loads()或者对应的load()方法，前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化：
print 'Json Load:', json.loads(json.dumps(d))
with open('./json.txt', 'r') as f:
    print 'read from ./json.txt'
    print json.load(f)
    
#Python的dict对象可以直接序列化为JSON的{}，不过，很多时候，我们更喜欢用class表示对象，比如定义Student类，然后序列化：
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
s = Student('小红', 20, 88)
#默认情况下，dumps()方法不知道如何将Student实例变为一个JSON的{}对象。
#可选参数default就是把任意一个对象变成一个可序列为JSON的对象，我们只需要为Student专门写一个转换函数，再把函数传进去即可：
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }
print(json.dumps(s, default=student2dict))
