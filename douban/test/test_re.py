# -*- coding = utf-8 -*-
# @Time: 2022/3/26 0026 20:27
# @Author: crayonxiaoxin
# @File: test_re.py
# @Software: PyCharm

import re

# 创建模式对象
# pat = re.compile("AA")
# m = pat.search("CBA")
# m = pat.search("ABCAA")
# m = pat.search("ABCAADDCCAAA")  # search方法，进行比对查找
# print(m)

# 没有模式对象
# m = re.search("asd","Aasd")
# print(m)

# print(re.findall("a", "ASDaDFGAa"))
# print(re.findall("[A-Z]", "ASDaDFGAa"))
# print(re.findall("[A-Z]+", "ASDaDFGAa"))


print(re.sub("a", "A", "ASDaDFGAa"))  # 找到 a，并用 A 来替换  ASDADFGAA

# 建议在正则表达式中，被比较的字符串前面加个 r ，不用担心转义字符的问题
a = r"\aabd-\'"
print(a)