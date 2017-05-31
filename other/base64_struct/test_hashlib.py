#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等
#摘要算法: 又称哈希算法、散列算法。它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）。
#MD5是最常见的摘要算法，速度很快，生成结果是固定的128 bit字节，通常用一个32位的16进制字符串表示.
import hashlib
md5 = hashlib.md5()
md5.update('how to use md5 in')
print "hashlib.md5.hexdigest()    ", md5.hexdigest()
#SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示。
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in ')
print "sha1.hexdigest()    ", sha1.hexdigest()
#SHA256
sha256 = hashlib.sha256()
sha256.update('how to use sha1 in ')
print "sha256.hexdigest()    ", sha256.hexdigest()
print get_md5('aaaaa')
