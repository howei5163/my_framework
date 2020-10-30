#encoding=utf-8
import requests,re,os
from bs4 import BeautifulSoup
from common.path import *

import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
'''读取文件出现UnicodeEncodeError错误时,加上这一行就行'''

'''用bs4框架爬图片'''
url='http://699pic.com/sousuo-218808-13-1.html'
r=requests.get(url)

soup=BeautifulSoup(r.content,"lxml")
a=soup.a
# print(soup.prettify())#将解析的文件以html格式打印
# 获取html的a标签的信息(soup.a默认获取第一个a标签，想获取全部就用for循环去遍历)
print(a['href'])
'''获取href属性'''
print(a.attrs)

'''获取a标签的所有属性'''
t1=soup.find_all(class_="lazy")#查找所有的标签名字为“class_="lazy"”的对象

# t2=soup.find_all('img')#查找所有的标签名字为“img”的对象
# 爬取所有图片
for i in t1:
    try:
        r1=requests.get("http:"+i["data-original"])
        f=open(os.path.join(img_path,'%s.jpg'%i['title']),'wb')#以二进制格式打开
        f.write(r1.content)
        f.close()
    except:
        pass
