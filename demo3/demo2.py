# -*- coding = utf-8 -*-
# @Time: 2022/3/26 0026 11:22
# @Author: crayonxiaoxin
# @File: demo2.py
# @Software: PyCharm

"""
# 打开文件： w模式，不存在则创建
f = open("test.txt", "w")
# f = open("test.txt")   # 默认是 r 模式，没有文件会 FileNotFoundError

f.write("hello world, i am here")

# 关闭文件
f.close()
"""

"""
# read 方法，读取指定长度字符，开始时定位在开头，每读一次向后移动指定长度位置
f = open("test.txt","r")

# content = f.read()
content = f.read(5)  # hello
print(content)
content = f.read(5)  # worl
print(content)

# 关闭文件
f.close()
"""

"""
# readlines 读取多行为列表

f = open("test.txt","r")
# content = f.readline()
# print(content)
content = f.readlines()     # 列表
print(content)
f.close()
"""

"""
import os

os.rename("test.txt", "test-new.txt")
"""
