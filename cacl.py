#!/usr/bin/env python
# -*- coding: utf-8 -*-
#这个脚本用来生成20以内的加减法，让女儿练习数学
import random, time  
num=50
ok= 0
err= 0
string_list=[]
for i in range(1,num+1):
    x = random.randint(1,15)
    y = random.randint(3,15)
    z = x + y
    string = str(i)+':             '+str(x)+' + '+str(y)+' = '
    start = time.time()
    input_result = raw_input(string)
    while not input_result.isdigit(): 
        input_result = raw_input(string)
    if ( int(input_result) == z):
        ok = ok + 1
    else:
        err = err + 1
        string = string + input_result
        string_list.append(string)
    use_time = time.time() - start
    if (use_time > 5):
        print '用时过长，%0.2f 秒' % use_time
print ('做对 '+str(ok)+' 题，做错 '+str(err)+' 题') 
print ('====做错的题目====')
for j in string_list:
    print j

