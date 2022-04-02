# -*- coding = utf-8 -*-
# @Time: 2022/3/26 0026 17:22
# @Author: crayonxiaoxin
# @File: spider.py
# @Software: PyCharm


# 网页解析，获取数据
from bs4 import BeautifulSoup
# 正则表达式
import re
# 指定 url 获取网页数据
import urllib.request, urllib.error
# excel 操作
import xlwt
import time
import sqlite3


def main():
    baseurl = "https://movie.douban.com/top250?start="
    # 1. 爬取网页
    datalist = getData(baseurl)

    # 3. 保存数据
    # 保存到 Excel
    # savepath = "./豆瓣电影Top250.xls"
    # saveData(datalist, savepath)

    # 保存到 sqlite
    dbpath = 'movie.db'
    saveData2DB(datalist, dbpath)


# 影片链接的规则
findLink = re.compile(r'<a href="(.*?)">')
# 影片图片
findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S)  # re.S 让换行符包括在匹配中
# 影片片名
findTitle = re.compile(r'<span class="title">(.*)</span>')
# 影片评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
# 影片评价
findJudge = re.compile(r'<span>(\d*)人评价</span>')
# 概括
findInq = re.compile(r'<span class="inq">(.*)</span>')
# 影片的相关内容
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)


# 爬取网页
def getData(baseurl):
    datalist = []
    # for i in range(0, 1):
    for i in range(0, 10):
        url = baseurl + str(i * 25)
        html = askUrl(url)
        # 2. 解析数据
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all("div", class_="item"):  # 查找符合要求的字符串，形成列表
            # print(item)  # 测试：查看电影item全部信息
            data = []
            item = str(item)

            # 获取影片详情链接
            link = re.findall(findLink, item)[0]  # re 库通过正则表达式查找指定字符串
            data.append(link)  # 添加链接

            imgSrc = re.findall(findImgSrc, item)[0]
            data.append(imgSrc)  # 添加图片

            titles = re.findall(findTitle, item)  # 片名可能只有一个中文名，没有英文名
            if len(titles) == 2:
                ctitle = titles[0]
                data.append(ctitle)  # 添加中文名
                otitle = titles[1].replace("/", "")
                data.append(otitle)  # 添加外文名
            else:
                data.append(titles[0])
                data.append(' ')

            rating = re.findall(findRating, item)[0]
            data.append(rating)  # 添加评分

            judge = re.findall(findJudge, item)[0]
            data.append(judge)  # 添加评论人数

            inq = re.findall(findInq, item)
            if len(inq) != 0:
                inq = inq[0].replace("。", "")
            else:
                inq = " "
            data.append(inq)  # 添加概述

            bd = re.findall(findBd, item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?', " ", bd)  # 去掉 <br/>
            bd = re.sub('/', " ", bd)  # 去掉 /
            data.append(bd.strip())  # 去掉前后的空格

            datalist.append(data)  # 把处理好的一部电影信息放入 datalist
        # 设置时间间隔，防止 ip 被 ban
        time.sleep(2)

    # print(datalist)
    return datalist


# 得到指定一个url的网页内容
def askUrl(url):
    head = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36 "
    }
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


def saveData(datalist, savepath):
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)
    sheet = book.add_sheet("豆瓣电影Top250", cell_overwrite_ok=True)
    col = ("电影详情链接", "电影图片", "电影中文名", "电影外文名", "电影评分", "电影评论人数", "电影概述", "相关信息")
    for i in range(0, len(col)):
        sheet.write(0, i, col[i])
    for i in range(0, len(datalist)):
        data = datalist[i]
        for j in range(0, len(data)):
            sheet.write(i + 1, j, data[j])
    book.save(savepath)
    pass


def saveData2DB(datalist, dbpath):
    init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    for data in datalist:
        for index in range(len(data)):
            if index == 4 or index == 5:
                continue
            data[index] = '"' + data[index] + '"'
        sql = '''
            insert into movie250(info_link,pic_link,cname,ename,score,rated,introduction,info)
            values(%s)
            ''' % ",".join(data)
        cursor.execute(sql)
        conn.commit()

    cursor.close()
    conn.close()
    pass


def init_db(dbpath):
    sql = '''
        create table if not exists movie250(
            id integer primary key autoincrement,
            info_link text,
            pic_link text,
            cname varchar,
            ename varchar,
            score numeric,
            rated numeric,
            introduction text,
            info text
        )
    '''
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()


if __name__ == '__main__':  # 当程序执行时
    main()
    # init_db("movietest.db")
    print("爬取完毕")
