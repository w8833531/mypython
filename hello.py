#!/usr/bin/env python
# -*- coding: utf-8 -*-
print u'中文测试正常'
print u'你好，%s' % u'世界'
print u'你好，%s %02d世纪 欢迎你' % (u'吴鹰', 21)
print u'你好冒险者，我是穆，请问你是'
name=raw_input(u'请输入姓名:'.encode('utf-8')).decode('utf-8')
print u'%s，你好，真是一个不错的名字，欢迎来到%s'%(name,u"法兰城")
