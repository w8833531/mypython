#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Base64,就是用来把二进制转换为文本数据，编码会把3字节的二进制数据编码为4字节的文本数据，长度增加33%，好处是编码后的文本数据可以在邮件正文、网页等直接显示。

import base64
print base64.b64encode('binarystring')
print base64.b64decode('YmluYXJ5AHN0cmluZw==')
print base64.urlsafe_b64encode('i\xb7\x1d\xfb\xef\xff')
print base64.urlsafe_b64decode('abcd--__')
print "base64.b64decode('YWJjZA==')", base64.b64decode('YWJjZA==')
#print base64.b64decode('YWJjZA') # TypeError

#由于=字符也可能出现在Base64编码中，但=用在URL、Cookie里面会造成歧义，所以，很多Base64编码后会把=去掉：
#下面写一个safe_b64decode函数，用来自动完成去掉=号字符的base64解码处理
def safe_b64decode(str):
    length = len(str) % 4
    if length == 0:
        return base64.b64decode(str)
    else:
        for i in range(4- int(length)):
            str = str + '='
        return base64.b64decode(str)
#来一个更加简单的
def b64(str):
    return base64.b64decode(str+'='*(4-len(str)%4))

print "safe_b64decode('YWJjZA')", safe_b64decode('YWJjZA')
print "b64('YWJjZA')", b64('YWJjZA')


