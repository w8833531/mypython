#!/usr/bin/env python
#-*- coding: utf-8 -*-
#这个client用来测试server.py程序
import socket, threading
def socket_client(s):
    # 建立连接:
    s.connect(('127.0.0.1', 9999))
    # 接收欢迎消息:
    print s.recv(1024)
    for data in ['Michael', '', 'Sarah']:
        # 发送数据:
        if data:
            print '========= %s ==========' % data
            s.send(data)
            print s.recv(1024)
    s.send('exit')
    s.close()
#使用并发线程的方式来访问server端
for i in range(1):
    print '============== %s ============' % i
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #创建新线程来处理TCP连接
    t = threading.Thread(target = socket_client, args=(ss,))
    t.start()
