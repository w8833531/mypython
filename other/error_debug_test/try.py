#!/usr/bin/env python
#-*- coding: utf-8 -*-
#当我们认为某些代码可能会出错时，就可以用try来运行这段代码，如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，即except语句块，执行完except后，如果有finally语句块，则执行finally语句块，至此，执行完毕。
try:
    print 'try...'
    r = 10 / 0
    print 'result:', r
except ZeroDivisionError, e:
    print 'except:', e
finally:
    print 'finally...'
print 'END'

#int()函数可能会抛出ValueError，所以我们用一个except捕获ValueError，用另一个except捕获ZeroDivisionError。此外，如果没有错误发生，可以在except语句块后面加一个else，当没有错误发生时，会自动执行else语句：
try:
    print 'try...'
    r = 10 / int('a')
    print 'result:', r
except ValueError, e:
    print 'ValueError:', e
except ZeroDivisionError, e:
    print 'ZeroDivisionError:', e
else:
    print 'no error!'
finally:
    print 'finally...'
print 'END'

#第二个except永远也捕获不到ValueError，因为ValueError是StandardError的子类，如果有，也被第一个except给捕获了。
try:
    foo()
except StandardError, e:
    print 'StandardError'
except ValueError, e:
    print 'ValueError'

#使用try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用，比如函数main()调用foo()，foo()调用bar()，结果bar()出错了，这时，只要main()捕获到了，就可以处理：
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except StandardError, e:
        print 'Error!', e
    finally:
        print'finally...'

main()

#如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获，打印一个错误信息，然后程序退出。来看看err.py：
#如果不捕获错误，自然可以让Python解释器来打印出错误堆栈，但程序也被结束了
print '##############err.py###########'
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    bar('0')

#main() #如果不捕获错误，自然可以让Python解释器来打印出错误堆栈，但程序也被结束了

#Python内置的logging模块可以非常容易地记录错误信息：
import logging
logging.basicConfig(level=logging.INFO)

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except StandardError, e:
        logging.exception(e)

main() #这时，程序不会结束，后面的代码会继续运行
print 'END'  


#assert的意思是，表达式n != 0应该是True，否则，后面的代码就会出错
# err.py
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('0')
#main() #打开的话，程序就中断了。
print '###################'

#把print替换为logging是第3种方式，和assert比，logging不仅可以抛出错误，而且可以输出到文件：
import logging
#logging的好处，它允许你指定记录信息的级别，有debug，info，warning，error等几个级别，当我们指定level=INFO时，logging.debug就不起作用了。同理，指定level=WARNING后，debug和info就不起作用了。这样一来，你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。
logging.basicConfig(level=logging.INFO)
s = '0'
n = int(s)
#logging的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件。
logging.info('n = %d' % n)
print 10 / n
#logging才是终极武器
