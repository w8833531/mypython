#!/usr/bin/env python
#-*- coding: utf-8 -*-
#mysql-connector           - MySQL driver written in Python
#MySQL的SQL占位符是%s；
#通常我们在连接MySQL时传入use_unicode=True，让MySQL的DB-API始终返回Unicode。
import mysql.connector
try:
    conn = mysql.connector.connect(host='192.168.0.2', user='root', password='qwer1234', database='test', use_unicode=True)
    cursor = conn.cursor()
    cursor.execute('insert into user (id, name) values (%s, %s)', ['5', 'Ying'])
    cursor.execute('select * from user')
    values = cursor.fetchall()
    print (cursor.rowcount)
    print (values)
    conn.commit()
    cursor.execute('select * from user')
    values = cursor.fetchall()
    print (cursor.rowcount)
    print (values)
finally:
    cursor.close()
    conn.close()
    
