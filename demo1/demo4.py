# -*- coding = utf-8 -*-
# @Time: 2022/3/24 下午5:40
# @Author: crayonxiaoxin
# @File: demo4.py
# @Software: PyCharm

"""
# 循环
for i in range(5):
    print(i)
"""

"""
for i in range(0, 5):
    print(i)
"""

"""
for i in range(0, 12, 3): # 从 0 到 12，不包括 12，步进 3
    print(i)
"""

"""
name = "crayonxiaoxin"
for char in name:
    print(char, end="\t")
"""

"""
arr = ["aa", "bb", "cc", "dd", 12]
for i in range(0, len(arr)):
    print(i, arr[i])
"""

"""
i = 0
while i < 5:
    print("当前是第%d次执行" % (i + 1))
    print("i=%d" % i)
    i += 1
"""

"""
# 1 到 100 求和
n = 1
sum = 0
while n <= 100:
    sum += n
    n += 1
print("(0 到 %d) sum = %d" % (100, sum))
"""

"""
i = 0
while i < 10:
    i += 1
    print("-" * 30)
    if i == 5:
        # break 跳出整个循环，只打印到 4
        break
    print(i)
"""

"""
i = 0
while i < 10:
    i += 1
    print("-" * 30)
    if i == 5:
        # continue 跳过本次循环，跳过了 5
        continue
    print(i)
"""

"""
i = 0
while i < 10:
    i += 1
    print("-" * 30)
    if i == 5:
        # pass 占位，不做任何事情
        pass
    print(i)
"""

# 九九乘法表
i = 1
n = 9
while i <= n:
    for x in range(1, i + 1):
        print("%d * %d = %d" % (i, x, i * x), end="\t")
    print("")
    i += 1
