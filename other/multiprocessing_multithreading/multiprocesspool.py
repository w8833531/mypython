#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, time, sys, random
from multiprocessing import Process, Pool

def long_time_task(name):
    print 'Run task %s (%s)...' % (name, os.getpid())
    start = time.time()
    time.sleep(random.random() * 6)
    end = time.time()
    print 'Task %s runs %0.2f seconds.' % (name, (end - start))

print 'Parent process %s.' % os.getpid()
p = Pool()
for i in range(5):
    p.apply_async(long_time_task, args=(i,))
print 'Waiting for all subprocesses done...'
p.close()
p.join()
print 'All subprocesses done.'
