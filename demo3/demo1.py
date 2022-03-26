# -*- coding = utf-8 -*-
# @Time: 2022/3/26 0026 10:50
# @Author: crayonxiaoxin
# @File: demo1.py
# @Software: PyCharm


"""
# 函数的定义
def printInfo():
    print("-" * 30)
    print("人生苦短，我用Python")
    print("-" * 30)


# 函数的调用
printInfo()
printInfo()
"""

"""
# 带参数

def add2num(a, b):
    print(a + b)

add2num(1, 2)
"""

"""
# 带返回值
def add2num(a, b):
    return a + b

print(add2num(1, 2))
"""

"""
# 带多个返回值
def divide(a, b):
    # shang = a / b   # 这个带小数点
    shang = a // b  # 这个取整
    yushu = a % b
    return shang, yushu

# 接收多个返回值
sh, yu = divide(11, 3)
# print(divide(11, 3))
print(sh, yu)
"""

"""
def print_line():
    print("-" * 30)


print_line()


def print_lines(n):
    if type(n) is int:
        for i in range(n):
            print_line()


print_lines(2)


def three_sum(a, b, c):
    return a + b + c


def three_average(a, b, c):
    total = three_sum(a, b, c)
    return total / 3


print(three_average(1, 2, 3))
"""

# 全局变量 和 局部变量
# 局部变量
"""
def test1():
    a = 300
    print("test1 ------- 修改前： a = %d" % a)
    a = 100
    print("test1 ------- 修改后： a = %d" % a)


test1()
"""

# 全局变量
"""
a = 800


def test1():
    a = 300
    print("test1 ------- 修改前： a = %d" % a)
    a = 100
    print("test1 ------- 修改后： a = %d" % a)


def test2():
    print(a)


test1()
test2()
"""

# 全局变量 和 局部变量 名字相同
"""
a = 800


def test1():
    a = 300
    print("test1 ------- 修改前： a = %d" % a)
    a = 100
    print("test1 ------- 修改后： a = %d" % a)


def test2():
    print(a)

test1()
test2()
"""

# 函数中修改全局变量
"""
a = 800


def test1():
    global a  # 修改全局变量
    a = 300
    print("test1 ------- 修改前： a = %d" % a)
    a = 100
    print("test1 ------- 修改后： a = %d" % a)


def test2():
    print(a)


test1()
test2()
"""
