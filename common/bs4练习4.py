# coding:utf-8
from bs4 import BeautifulSoup
import requests

r = requests.get("http://www.cnblogs.com/yoyoketang/")
# 请求首页后获取整个html界面
blog = r.content
# print blog
# 用html.parser解析html
soup = BeautifulSoup(blog, "html.parser")
# 获取所有的class属性为dayTitle，返回Tag类
times = soup.find_all(class_="dayTitle")
# for i in times:
#     print i.a.string  # 获取a标签的文本

title = soup.find_all(class_="postTitle")
# for i in title:
#     print i.a.string

# 读取摘要内容
descs = soup.find_all(class_="postCon")
# for i in descs:
#     # tag的 .contents 属性可以将tag的子节点以列表的方式输出
#     c = i.div.contents[0]  # 取第一个
#     print c

for i, j, k in zip(times,title,descs):
    print (i.a.string)
    print (j.a.string)
    print (k.div.contents[0])
    print ("")