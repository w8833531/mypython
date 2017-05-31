#!/usr/bin/env python
#-*- coding: utf-8 -*-
#这个脚本用来跑CPU数-1个进程，死循环，看CPU占用情况
from multiprocessing import Process, Queue, Pool
import  multiprocessing

def loop():
    x = 0
    while True:
        x = x ^ 1

p = Pool()
print multiprocessing.cpu_count() - 1
for i in range(multiprocessing.cpu_count() - 1):
    p.apply_sync(loop,)    
    p.start()
