#coding=utf-8
import os
from common.path import *
# for fpath,dirname,fnames in os.walk(img_path):
'''os.walk获取所有目录'''
    # print(fpath)#所有文件夹路径
    # print(dirname)#所有文件夹名字
    # print(fnames)#所有文件名字

# li=[]
'''获取所有句尾是.jpg的文件'''
# for fp,dir,fn in os.walk(img_path):
#     for i in fn:
#         if i.endswith('.jpg'):
#             li.append(i)
# print(li)

# print(os.getcwd())
'''获取当前位置'''

'''用os。system执行cmd命令'''
# os.system("taskkill /IM chrome.exe /F")
# os.system("taskkill /IM chromedriver.exe /F")
# os.system('ipconfig')

# if not os.path.exists(img_path):
'''判断如果路径下不存在该文件夹，就生成一个，不可用于生成文件'''
    # os.mkdir(img_path)

# print(os.listdir(project_path))
# '''将路径下的文件、文件夹以列表形式返回'''

# os.makedirs(os.path.join(report_path,'sada/asdsa/aaa/ss'))
'''递归创建文件夹'''
# os.remove(path)
'''删除一个文件，不可删除文件夹会报错'''
# os.rmdir(os.path.join(report_path,'sada/asdsa/aaa/ss'))
'''删除空文件夹'''

# print(os.path.abspath(report_path))
# '''文件的绝对路径'''
# print(os.path.getctime(report_path))
# '''文件的创建时间'''
# print(os.path.getmtime(report_path))
# '''文件的修改时间'''
a=os.listdir(report_path)
'''查找最新生产的文件'''
a.sort(key=lambda fn:os.path.getctime(os.path.join(report_path,fn)))
'''将list以创建时间进行降序排序(默认是降序)'''
print(a[-1])
'''此时列表中最后一个就是最新生成的文件'''