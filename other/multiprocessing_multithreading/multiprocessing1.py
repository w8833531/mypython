#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, time, sys, random
from multiprocessing import Process, Queue, Pool
      
#Unix/Linux操作系统提供了一个fork()系统调用，它非常特殊。普通的函数调用，调用一次，返回一次，但是fork()调用一次，返回两次，因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回。子进程>永远返回0，而父进程返回子进程的ID。这样做的理由是，一个父进程可以fork出很多子进程，所以，父进程要记下每个子进程的ID，而子进程只需要调用getppid()就可以拿到父进程的ID。Python的os模块封装了常见的系统调用，其中就包括fork，可以在Pytho0n程序中轻松创建子进程：
      
print 'Process (%s) start...' % os.getpid()
for i in range(1,8):
    print '================ %s ================' % i
    pid = os.fork()
    if pid == 0:
        print 'I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid())
        sys.exit()
time.sleep(0.2)
print 'I (%s) just created a child process (%s).' % (os.getpid(),pid)

#如果你打算编写多进程的服务程序，Unix/Linux无疑是正确的选择。由于Windows没有fork调用，难道在Windows上无法用Python编写多进程的程序？由于Python是跨平台的，自然也应该提供一个跨平台的多进程支持。multiprocessing模块就是跨平台版本的多进程模块。multiprocessing模块提供了一个Process类来代表一个进程对象，下面的例子演示了启动一个子进程并等待其结束：


# 子进程要执行的代码
def run_proc(name):
    print 'Run child process %s (%s)...' % (name, os.getpid())

print 'Parent process %s.' % os.getpid()
p = Process(target=run_proc, args=('test',))
print 'Process will start.'
p.start()
p.join()
print 'Process end.'


#Pool:如果要启动大量的子进程，可以用进程池的方式批量创建子进程：
def long_time_task(name):
    print 'Run task %s (%s)...' % (name, os.getpid())
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print 'Task %s runs %0.2f seconds.' % (name, (end - start))

print 'Parent process %s.' % os.getpid()
p = Pool()
for i in range(5):
    p.apply_async(long_time_task, args=(i,))
print 'Waiting for all subprocesses done...'
p.close()
p.join()
print 'All subprocess done.'


#进程间通信
#Process之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据。我们以Queue为例，在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据：

#写数据进程代码：
def write(q):
    for value in range(10):
        print 'Put %d to queue...' % value
        q.put(value)
        time.sleep(random.random() * value)
#读数据进程执行代码：
def read(q):
    while True:
        value = q.get(True)
        print 'Get %d from queue.' % value
#父进程创建Queue,并传给各个子进程：
q = Queue()
pw = Process(target=write, args=(q,))
pr = Process(target=read, args=(q,))
#启动子进程pw,写入
pw.start()
#启动子进程pr,读出
pr.start()
#等待pw结束
pw.join()
#结束pr,因为是死循环
pr.terminate()

