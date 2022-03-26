# -*- coding = utf-8 -*-
# @Time: 2022/3/26 0026 10:07
# @Author: crayonxiaoxin
# @File: demo3.py
# @Software: PyCharm

# 元组    （不可变 List）

"""
tuple1 = ()  # 创建空元组
print(type(tuple1))

# tuple2 = (50)   # 这个不是元组，是 int
tuple2 = (50,)  # 这个是元组，只有一个数据，需要加逗号
tuple2 = (50, 60, 70)  # 这个是元组
print(type(tuple2))
"""

"""
tup1 = ("abc", "def", 123, 456)
print(tup1[0])
print(tup1[-1])
print(tup1[1:5])        # 左闭右开
"""

"""
# 增     (连接)
tup1 = (12, 34, 56)
tup2 = ("abc", "def")
tup = tup1 + tup2
print(tup)
"""

"""
# 删
tup1 = (12, 34, 56)
print(tup1)
del tup1        # 删除了整个元组变量
print("删除后")
print(tup1)     # 报错，没有变量
"""

"""
# 改
tup1 = (12, 34, 56)
tup1[0] = 100  # 报错，不能修改
"""

# 查


# 字典     （类似 Map）

# 定义
"""
info = {"name": "吴彦祖", "age": 18}
"""

# 字典的访问
"""
print(info['name'])
"""

# 访问了不存在的键
"""
# print(info['address'])  # 直接访问，会报错
# print(info.get("address"))  # 使用 get 方法，没有找到对应的键，默认返回 None
print(info.get("address", "China"))  # 使用 get 方法，没有找到对应的键，可以设定默认值
"""

# 增
"""
info = {"name": "吴彦祖", "age": 18}
newID = input("请输入学号：")
info['id'] = newID
print(info)
"""

# 删
# [ del ]
"""
info = {"name": "吴彦祖", "age": 18}
print("删除前：%s" % info['name'])
del info['name']     # 删除的是键值对
print("删除后：%s" % info.get("name"))
"""

"""
info = {"name": "吴彦祖", "age": 18}
print("删除前：%s" % info)
del info
print("删除后：%s" % info)      # 删除字典后，再访问会报错
"""

# [ clear ]
"""
info = {"name": "吴彦祖", "age": 18}
print("删除前：%s" % info)
info.clear()
print("删除后：%s" % info)      # 清空
"""

# 改
"""
info = {"name": "吴彦祖", "age": 18}
print("修改前：%s" % info)
info['name']="彭于晏"
print("修改后：%s" % info)
"""

# 查
info = {"id": 1, "name": "吴彦祖", "age": 18}
"""
print(info.keys())  # 所有的键，List 形式
print(info.values())  # 所有的值，List 形式
print(info.items())  # 所有的项，List 形式，但每个元素都是元组
"""

# 遍历所有的键
"""
for key in info.keys():
    print(key, info.get(key))
"""

# 遍历所有的值
"""
for value in info.values():
    print(value)
"""

# 遍历所有的键值对
"""
for key, value in info.items():     # info.items() 返回的是 List，每个元素都是元组
    print(key, value)
"""

# 使用枚举函数，同时拿到列表的下标和值
mylist = ["a", "b", "c", "d"]
print(enumerate(mylist))
for i, x in enumerate(mylist):
    print(i, x)

"""
列表  List    可变，类似数组  
元组  List    不可变
字典  dict    key不可变，val可变，类似 Map
集合  Set     可变，不可重复，Set
"""
