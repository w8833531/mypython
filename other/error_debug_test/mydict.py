#!/usr/bin/env python
# -*- coding: utf-8 -*-
#我们来编写一个Dict类，这个类的行为和dict一致，但是可以通过属性来访问
#用起来是这个样子：
#d = Dict(a=1, b=2)
#print d.a
class Dict(dict):

    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

