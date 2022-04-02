# -*- coding = utf-8 -*-
# @Time: 2022/3/26 0026 18:02
# @Author: crayonxiaoxin
# @File: test_urllib.py
# @Software: PyCharm

import urllib.request

# 获取一个 get 请求
# response = urllib.request.urlopen("https://hixin.cc")
# print(response.read().decode('utf-8'))  # 对获取到的网页源码进行 utf-8 解码


# 获取一个 post 请求
# import urllib.parse
#
# data = bytes(urllib.parse.urlencode({"hello": "world"}, encoding="utf-8").encode("utf-8"))
# response = urllib.request.urlopen("https://httpbin.org/post", data=data)
# print(response.read().decode("utf-8"))

import urllib.error
import urllib.parse

# 获取一个 get 请求
# try:
#     response = urllib.request.urlopen("https://httpbin.org/get", timeout=0.1)
#     print(response.read().decode("utf-8"))
# except urllib.error.URLError as e:
#     print(e)


# response = urllib.request.urlopen("https://www.baidu.com", timeout=1)
# # print(response.getheaders())
# print(response.getheader("Server"))

# url = "https://www.douban.com"
# url = "https://httpbin.org/post"
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
#                          "Chrome/99.0.4844.82 Safari/537.36",
#            }
# data = bytes(urllib.parse.urlencode({"name": "hh"}, encoding="utf-8").encode("utf-8"))
# req = urllib.request.Request(url=url, data=data, headers=headers, method="POST")
# response = urllib.request.urlopen(req, timeout=1)
# print(response.read().decode("utf-8"))


url = "https://www.douban.com"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/99.0.4844.82 Safari/537.36",
           }
req = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))