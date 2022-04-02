# -*- coding = utf-8 -*-
# @Time: 2022/3/24 0024 22:16
# @Author: crayonxiaoxin
# @File: demo2.py
# @Software: PyCharm

# 列表    （List，类似数组）

# namelist = []   # 空列表

"""
namelist = ["小明", "小红", "小刚"]
print(namelist[1])
print(namelist[-1])
print(type(namelist))

testlist = ["小明", 123, True]
print(testlist)
print(type(testlist[1]))
print(type(testlist[2]))
"""

"""
namelist = ["小明", "小红", "小刚"]
for name in namelist:
    print(name)

print(len(namelist))

length = len(namelist)
i = 0
while i < length:
    print(namelist[i])
    i += 1
"""

namelist = ["小明", "小红", "小刚"]

# 增
"""
# 增加 append
print("------增加前------")
print(namelist)
namelist.append("小李")   # 末尾追加
print("------增加后------")
print(namelist)
"""

"""
a = [1, 2]
b = [3, 4]
a.append(b) # 将列表b当做一个元素整体，加入a列表中  [1, 2, [3, 4]]
print(a)

a.extend(b) # 将列表b中的每个元素逐一追加到a列表中 [1, 2, [3, 4], 3, 4]
print(a)
"""

"""
a = [1, 2, 3]
a.insert(1, 8)  # 把 8 插入到下标 1 的位置处
print(a)
"""

# 删
"""
movieName = ["加勒比海盗", "指环王", "哈利波特", "指环王", "第一滴血", "黑客帝国", "速度与激情", "复仇者联盟"]
print("------删除前------")
print(movieName)
# del movieName[2]   # 删除 指定下标 元素
# movieName.pop()      # 弹出 末尾 元素
movieName.remove("指环王")  # 删除 指定内容 元素 （删除匹配的第一个）
print("------删除后------")
print(movieName)
"""

# 改
"""
print("------修改前------")
print(namelist)
namelist[1] = "小刘"  # 修改指定下标元素
print("------修改后------")
print(namelist)
"""

# 查
"""
findName = input("请输入你要查找的姓名：")
if findName in namelist:
    print("找到了")
else:
    print("没有找到")
"""

"""
a = ["a", "b", "c", "a", "e"]
print(a.index("a", 1, 4))  # 在 指定范围内 查找元素的下标
print(a.index("a", 1, 3))  # 范围区间  左闭右开  [)  # 找不到会报错
"""

"""
a = ["a", "b", "c", "a", "e"]
print(a.count("a"))     # 计算有多少个 a
"""

# 排序 和 反转
"""
a = [1,4,8,3]
print(a)
a.reverse()     # 列表翻转
print(a)

a.sort()        # 排序，升序
print(a)
a.sort(reverse=True)    # 排序，降序
print(a)
"""

"""
import random

offices = [[], [], []]
names = ["A", "B", "C", "D", "E", "F", "G", "H"]
for name in names:
    index = random.randint(0, 2)
    offices[index].append(name)
print(offices)
for office in offices:
    print("办公室人数：%d" % (len(office)))
"""

products = [["iphone", 6888], ["MacPro", 14800], ["小米6", 2499], ["Coffee", 31], ["Book", 60], ["Nike", 699]]
print("----- 商品列表 -----")
for i in range(len(products)):
    product = products[i]
    product.insert(0, i)
    print(product[0], product[1], product[2], sep="\t")
cart = []
while True:
    want = input("选择一个商品购买: ")
    want.isdecimal()
    want.isdigit()
    if want.isnumeric():
        if '0' <= want <= '9':
            num = int(want)
            if num >= len(products):
                print("不存在")
            else:
                cart.append(products[num])
        else:
            print("不存在")
            continue
    elif want == "q":
        break
    else:
        print("请输入数字")
print("----- 购物车列表 -----")
for i in range(len(cart)):
    product = cart[i]
    product.insert(0, i)
    print(product[0], product[1], product[2], product[3], sep="\t")
