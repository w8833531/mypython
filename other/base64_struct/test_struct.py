#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Python提供了一个struct模块来解决str和其他二进制数据类型的转换。
#pack
#struct的pack函数把任意数据类型变成字符串：

import struct
#>表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。
print struct.pack('>I', 10240099)
#根据>IH的说明，后面的str依次变为I：4字节无符号整数和H：2字节无符号整数。
print struct.unpack('>IH', '\xf0\xf0\xf0\xf0\x80\x80')

#Windows的位图文件（.bmp）是一种非常简单的二进制文件格式
#BMP格式采用小端方式存储数据，文件头的结构按顺序如下：

#两个字节：'BM'表示Windows位图，'BA'表示OS/2位图；
#一个4字节整数：表示位图大小；
#一个4字节整数：保留位，始终为0；
#一个4字节整数：实际图像的偏移量；
#一个4字节整数：Header的字节数；
#一个4字节整数：图像宽度；
#一个4字节整数：图像高度；
#一个2字节整数：始终为1；
#一个2字节整数：颜色数。

#所以，组合起来用unpack读取：struct.unpack('<ccIIIIIIHH', s)
#下面的函数用来分析一个BMP文件的上述属性
def bmpinfo(file):
    with open(file, 'rb') as f:
        con = f.read(30)
        if con.find('BM') == 0:
            print ('The file of %s is a windows BMP bit file.' % file)
            s = struct.unpack('<ccIIIIIIHH', con)
            size = s[2]
            wide = s[6]
            high = s[7]
            color = s[9]
            print ('BMP bit file %s info: size %s ,wide * high %s * %s, color %s' % (file, size, wide, high, color)) 
bmpinfo('./1.bmp')
