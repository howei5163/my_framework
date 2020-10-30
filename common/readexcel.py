#coding=utf-8
import xlrd,json,xlwt,os
from bs4 import BeautifulSoup
from common.path import *
from xlwt import *
from xlutils3.copy import copy
import traceback
def Readexcel(file):
    '''定义一个读取excel内容的方法'''
    try:
        wookbook=xlrd.open_workbook(file)
        sh=wookbook.sheet_by_name('Sheet1') #通过表名的方式进行查找
        nrow=sh.nrows  #获取最大函数
        if nrow>1: #如果行数大于1，证明有数据，否则表内没有数据
            keys=sh.row_values(0)  #以表内的第一行为key值
            params=[]
            for i in range(1,nrow):
                if nrow==0:
                    print('表内没有数据')
                values=sh.row_values(i)
                params.append(dict(zip(keys,values)))
            return params
        else:
            print('表内没有数据')
    except FileNotFoundError as F:
        print('没有找到文件')
        print('错误内容:%s'%F)

def yangshi1():
    style=XFStyle()
    fnt=Font()
    fnt.name=u'微软雅黑'
    fnt.bold=True
    fnt.underline=True #下划线
    style.font=fnt
    alignment=xlwt.Alignment()
    alignment.horz=xlwt.Alignment.HORZ_CENTER
    alignment.vert=xlwt.Alignment.VERT_CENTER
    style.alignment=alignment #添加居中属性
    style.font.height=430
    return style
def yangshi2():
    style1 = XFStyle()
    alignment = xlwt.Alignment()
    alignment.horz = xlwt.Alignment.HORZ_CENTER
    alignment.vert = xlwt.Alignment.VERT_CENTER
    style1.alignment = alignment  # 给样式添加文字居中属性
    style1.font.height = 330  # 设置字体大小
    return style1

def write_excel(file_name,sheet_name,datas):
    '''write根据实际情况在进行更改'''
    if not os.path.exists(file_name):
        # 如果不存在这个文件就创建一个
        workbook=xlwt.Workbook(encoding='utf-8')
        sheet=workbook.add_sheet(sheet_name)
        workbook.save(file_name)
        print('目标文件不存在，已生成，地址为%s'%file_name)
    try:
        '''如果sheet已经存在，不生产，否则添加sheet'''
        if not sheet_name in xlrd.open_workbook(file_name).sheet_names():
            Workbook=copy(xlrd.open_workbook(file_name))
            Workbook.add_sheet(sheet_name)
            Workbook.save(file_name)
        else:
            print('%s已存在'%sheet_name)


    except:
        print(str(traceback.format_exc()))
    try:
        workbook=xlrd.open_workbook(file_name)
        worksheet=workbook.sheet_by_name(sheet_name)
        new_workbook=copy(workbook) #将xlrd对象拷贝转化为xlwt对象
        new_worksheet=new_workbook.get_sheet(sheet_name)
        li=datas
        for i in range(worksheet.nrows):
            '''清空所有数据'''
            for j in range(len(worksheet.row_values(i))):
                new_worksheet.write(i,j,"")
        style=xlwt.XFStyle()
        row=li[0]
        for keys in range(len(row)):
            new_worksheet.write(0,keys,list(row.keys())[keys],style)
            #这里.keys()返回的无法取索引，可以转换成list就可以了

        for col_index in range(len(row)):
            for row_index in range(1,len(li)+1):
                #因为第一行要写KEY值，所以要从第二行开始，最大值要加一，要不会少写一行数据
                new_worksheet.write(row_index,col_index,list(li[row_index-1].values())[col_index],style)


        new_workbook.save(file_name)
    except :
        print('打开文件异常%s'%str(traceback.format_exc()))


if __name__ == '__main__':
    print(Readexcel(os.path.join(data_path,'shuju.xlsx')))
    write_excel(os.path.join(data_path,'ssss.xlsx'),'ssssss',Readexcel(os.path.join(data_path,'shuju.xlsx')))
