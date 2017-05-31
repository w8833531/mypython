#!/usr/bin/env python
#-*- coding: utf-8 -*-
#正则表达式:
import re
#切分字符串:
print  "re.split(r'\s+', 'a b   c')    ", re.split(r'\s+', 'a b   c')
print  "re.split(r'[\s\,]+', 'a     ,  b ,  c')    ", re.split(r'[\s\,]+', 'a     ,  b ,  c') 
print  "re.split(r'[\s\,\;]+', 'a  ;;   ,  b ,  c')    ", re.split(r'[\s\,\;]+', 'a  ;;   ,  b ,  c') 

#分组
#除了简单地判断是否匹配之外，正则表达式还有提取子串的强大功能。用()表示的就是要提取的分组（Group）
#果正则表达式中定义了组，就可以在Match对象上用group()方法提取出子串来。
print "分组匹配："
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345678')
print "m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345678')"
print 'm.group(0)', m.group(0)
print 'm.group(1)', m.group(1)
print 'm.group(2)', m.group(2)
#匹配时间：
t = '19:05:30'
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print "匹配时间:"
print "t = '19:05:30'"
print "m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)"
print "m.groups()", m.groups()
#贪婪匹配：
#正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符。
print "贪婪匹配："
print "由于\d+采用贪婪匹配，直接把后面的0全部匹配了，结果0*只能匹配空字符串了。"
print "re.match(r'^(\d+)(0*)$', '102300').groups()   ", re.match(r'^(\d+)(0*)$', '102300').groups()
print "必须让\d+采用非贪婪匹配（也就是尽可能少匹配），才能把后面的0匹配出来，加个?就可以让\d+采用非贪婪匹配："
print "re.match(r'^(\d+?)(0*)$', '102300').groups()  ", re.match(r'^(\d+?)(0*)$', '102300').groups()

#编译：
#如果一个正则表达式要重复使用几千次，出于效率的考虑，我们可以预编译该正则表达式，接下来重复使用时就不需要编译这个步骤了，直接匹配：
re_telephone = re.compile(r'(\d{3})-(\d{3,8})')
print "re_telephone.match('010-12345').groups()",  re_telephone.match('010-12345').groups()

#匹配邮箱地址
print "re.match(r'^\w+@\w+\.\w+', 'someone@qq.com').group", re.match(r'^\w+@\w+\.\w+$', 'someone@qq.com')
