# -*- coding = utf-8 -*-
# @Time: 2022/3/24 下午4:46
# @Author: crayonxiaoxin
# @File: demo3.py
# @Software: PyCharm

"""
# 条件语句
# if True:
# if 1:
if 0:
    print("True")
else:
    print("False")
"""

"""
score = 60
if score >= 90:
    print("本次考试，等级为 A")
elif score >= 80:
    print("本次考试，等级为 B")
elif 80 > score >= 60:
    print("本次考试，等级为 C")
else:
    print("本次考试，不及格")
"""

"""
gender = 1
isSingle = 1
if gender == 1:
    print("男生")
    if isSingle:
        print("单身狗：介绍个女朋友吧")
    else:
        print("名草有主了")
else:
    print("女生")
"""

"""
import random   # 随机库
a = random.randint(0,2) # 随机生成 [0,1,2] 之间的随机数
print(a)
"""

"""
import random

print("请输入：剪刀（0）、石头（1）、布（2）")
str = input("您出：")
if str.isnumeric():
    a = int(str)
    if a in range(0, 3):
        system = random.randint(0, 2)
        if a == 0:
            you = "剪刀（0）"
            if system == 0:
                result = "平局"
            elif system == 1:
                result = "你输了"
            else:
                result = "你赢了"
        elif a == 1:
            you = "石头（1）"
            if system == 0:
                result = "你赢了"
            elif system == 1:
                result = "平局"
            else:
                result = "你输了"
        else:
            you = "布（2）"
            if system == 0:
                result = "你输了"
            elif system == 1:
                result = "你赢了"
            else:
                result = "平局"
        print("您出：%s" % you)
        print("随机生成数：", system)
        print(result)
    else:
        print("你耍赖了，必须输入 0-2 之间的数字")
else:
    print("请输入 0-2 之间的数字，不能输入其他类型")
"""
