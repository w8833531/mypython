#!/usr/bin/env python
# -*- coding: utf-8 -*-
#为了编写单元测试，我们需要引入Python自带的unittest模块，编写mydict_test.py如下：
import unittest

from mydict import Dict
#编写单元测试时，我们需要编写一个测试类，从unittest.TestCase继承。
class TestDict(unittest.TestCase):

    def setUp(self):
        print 'setUp start test...'

    def tearDown(self):
        print 'tearDown end test...'

    def test_init(self):  #以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行。
        d = Dict(a=1, b='test')
        self.assertEquals(d.a, 1)   # 断言函数返回两个变量相等
        self.assertEquals(d.b, 'test')
        self.assertTrue(isinstance(d, dict))  # 断言函数返回的结果是否为真

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEquals(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEquals(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError): #另一种重要的断言就是期待抛出指定类型的Error，比如通过d['empty']访问不存在的key时，断言会抛出KeyError
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty
#运行 python -m unittest mydict_test  来跑测试脚本，注意不要加.py
#单元测试可以有效地测试某个程序模块的行为，是未来重构代码的信心保证。

#单元测试的测试用例要覆盖常用的输入组合、边界条件和异常。

#单元测试代码要非常简单，如果测试代码太复杂，那么测试代码本身就可能有bug。

#单元测试通过了并不意味着程序就没有bug了，但是不通过程序肯定有bug。

