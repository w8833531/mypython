#!/usr/bin/env python
#-*- coding: utf-8 -*-
#由于SQLite的驱动内置在Python标准库中，所以我们可以直接来操作SQLite数据库。
#要操作关系数据库，首先需要连接到数据库，一个数据库连接称为Connection；
#连接到数据库后，需要打开游标，称之为Cursor，通过Cursor执行SQL语句，然后，获得执行结果。
#导入SQLite 驱动
import sqlite3
try:
# 连接到SQLite数据库
# 数据库文件是test.db
# 如果文件不存在，会自动在当前目录创建:
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
#    cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
    cursor.execute('insert into user (id, name) values(\'3\', \'Wu\')')
    print cursor.rowcount
except sqlite3.Error as e:
    print e
finally:
    cursor.close()
    conn.commit()
    conn.close()
#在Python中操作数据库时，要先导入数据库对应的驱动，然后，通过Connection对象和Cursor对象操作数据。
#要确保打开的Connection对象和Cursor对象都正确地被关闭，否则，资源就会泄露。
try:
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute('select * from user')
    values = cursor.fetchall()
    print values
except sqlite3.Error as e:
    print e
finally:
    cursor.close()
    conn.close()
 
    
