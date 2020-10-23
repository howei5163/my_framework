#coding=utf-8
from bs4 import BeautifulSoup
import requests
from common.path import *
import os
r=requests.get('http://www.cnblogs.com/yoyoketang/p/')
soup=BeautifulSoup(r.content,'html.parser')
title=soup.find_all(class_='postTitl2')
# print(r.text)
for i in title:
    print(i.a)
    print(i.a.get_text())
    #先找到父节点，在找他下面的a标签，然后获取文本