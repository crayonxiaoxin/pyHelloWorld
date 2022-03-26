# -*- coding = utf-8 -*-
# @Time: 2022/3/26 0026 11:39
# @Author: crayonxiaoxin
# @File: demo3.py
# @Software: PyCharm


# 打开不存在的文件，r模式
"""
print("---------------test----1")
f = open("123.txt", "r")            # 出现异常
print("---------------test----2")   # 不会被执行
"""

# 捕获异常

"""
try:
    print("---------------test----1")
    f = open("123.txt", "r")
    print("---------------test----2")
except IOError:  # 文件没找到，属于IO异常
    pass
"""

# 捕获多个异常
"""
try:
    print("---------------test----1")
    f = open("test-new.txt", "r")
    print("---------------test----2")
    print(num)
except (IOError, NameError):
    print("产生错误")
    pass
"""

# 异常描述
"""
try:
    print("---------------test----1")
    f = open("test-new.txt", "r")
    print("---------------test----2")
    print(num)
except (IOError, NameError) as result:
    print("产生错误")
    print(result)   # 字符串
    pass
"""

# 捕获所有异常 Exception
"""
try:
    print("---------------test----1")
    f = open("test-new.txt", "r")
    print("---------------test----2")
    print(num)
except Exception as result:
    print("产生错误")
    print(result)   # 字符串
    pass
"""

# try...finally 和 嵌套
"""
import time

try:
    f = open("test-new.txt", "r")
    try:
        while 1:
            content = f.readline()
            if len(content) == 0:
                break
            time.sleep(2)
            print(content)
    finally:
        f.close()
        print("文件关闭")
except Exception as result:
    print("发生异常。。。")
"""


def write2file(filename, content):
    f = open(filename, "w", encoding="utf-8")   # encoding="utf-8"，防止中文乱码
    f.write(content)
    f.close()


def readfile(filename):
    try:
        f = open(filename, "r", encoding="utf-8")   # encoding="utf-8"，防止中文乱码
        content = f.read()
        f.close()
        return content
    except Exception:
        content = "异常。。。"
        print(content)
        return content


gushi = """
    绝句
  作者：杜甫
两个黄鹂鸣翠柳，
一行白鹭上青天。
窗含西岭千秋雪，
门泊东吴万里船。
"""
write2file("gushi.txt", gushi)
content = readfile("gushi.txt")
print(content)
write2file("copy.txt", content)
print("复制完毕")
