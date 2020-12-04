#coding=utf-8
import os,sys,io
from bs4 import BeautifulSoup
def readHtml(filename):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')  # 改变标准输出的默认编码
    with open(filename,'r',encoding='utf-8') as f:
        soup=BeautifulSoup(f.read(),'html.parser')
    return soup
