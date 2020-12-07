#coding=utf-8

def Readtxt(file):
    params=[]
    with open(file,'r',encoding='utf-8') as f:
        for i in f.readlines():
            params.append(i.strip('\n').split(',')) #strip 删除两边的某个字段  split通过指定分隔符对字符串进行切片
    return params
def readtxt(file):
    with open(file,'r',encoding='utf-8')as f:
        txt=f.read()
    return txt

