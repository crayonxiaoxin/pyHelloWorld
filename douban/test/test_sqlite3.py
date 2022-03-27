# -*- coding = utf-8 -*-
# @Time: 2022/3/26 0026 22:24
# @Author: crayonxiaoxin
# @File: test_sqlite3.py
# @Software: PyCharm


import sqlite3

# conn = sqlite3.connect("test.db")  # 打开或创建数据库文件
# print("opened db successfully")

"""
conn = sqlite3.connect("test.db")  # 打开或创建数据库文件
print("成功打开数据库")

cursor = conn.cursor()  # 获取游标
sql = '''
    create table if not exists company 
    (id integer primary key autoincrement  not null,
     name text not null,
     age int not null,
     address char(50),
     salary real);
'''

cursor.execute(sql)  # 执行sql语句
cursor.close()
conn.commit()  # 提交数据库操作
conn.close()  # 关闭数据库
print("成功建表")
"""

# 插入数据
"""
conn = sqlite3.connect("test.db")  # 打开或创建数据库文件
print("成功打开数据库")

cursor = conn.cursor()  # 获取游标
sql1 = '''
    insert into company(id,name,age,address,salary) values(1,'张三',20,'广东',8000);
'''
sql2 = '''
    insert into company(id,name,age,address,salary) values(2,'李四',30,'上海',15000);
'''

cursor.execute(sql1)  # 执行sql语句
cursor.execute(sql2)  # 执行sql语句
cursor.close()
conn.commit()  # 提交数据库操作
conn.close()  # 关闭数据库
print("成功插入数据")
"""

# 查询数据
conn = sqlite3.connect("test.db")  # 打开或创建数据库文件
print("成功打开数据库")

cursor = conn.cursor()  # 获取游标
sql1 = '''
   select * from company;
'''

c = cursor.execute(sql1)  # 执行sql语句
for row in cursor:
    print("id=", row[0])
    print("name=", row[1])
    print("age=", row[2])
    print("address=", row[3])
    print("salary=", row[4])

cursor.close()
conn.commit()  # 提交数据库操作
conn.close()  # 关闭数据库
