#coding=utf-8
import xlrd,json,xlwt,os,time
from bs4 import BeautifulSoup
from common.path import *
from xlwt import *
from xlutils.copy import copy
import traceback
def Readexcel(file,sheetname='Sheet1'):
    '''定义一个读取excel内容的方法'''
    try:
        wookbook=xlrd.open_workbook(file)
        sh=wookbook.sheet_by_name(sheetname) #通过表名的方式进行查找
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
def redfont(data):
    if data ==False:
        style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on')  # Times New Roman文字,红色字体，加粗
        return style0
    elif data==True:
        style0 = xlwt.easyxf('font: name Times New Roman, color-index green, bold on')  # 绿色字体，加粗
        return style0
    else:
        style0 = xlwt.easyxf('font: name 宋体, color-index black, bold on')  # 黑色字体，加粗
        return style0

def write_excel(file_name,sheet_name,datas,new=None):
    '''使用另存功能时，原excel表如果没有参数的sheet则会生成一个，但不会写入数据'''
    now=time.strftime('%Y-%m-%d-%H-%M-%S')
    if not os.path.exists(file_name):
        # 如果不存在这个文件就创建一个
        workbook=xlwt.Workbook(encoding='utf-8')
        sheet=workbook.add_sheet(sheet_name)
        workbook.save(file_name)
        print('目标文件不存在，已生成，地址为%s'%file_name)
    try:
        '''如果sheet已经存在，不生成，否则添加sheet'''
        if not sheet_name in xlrd.open_workbook(file_name).sheet_names():
            Workbook=copy(xlrd.open_workbook(file_name))
            Workbook.add_sheet(sheet_name)
            Workbook.save(file_name)
        else:
            print('%s工作表已存在'%sheet_name)


    except:
        print(str(traceback.format_exc()))
    try:
        workbook=xlrd.open_workbook(file_name,formatting_info=True)#加上formatting_info参数后可以读取更多的信息，比如字体样式，颜色等等，但部分xlrd版本并不支持这个参数
        worksheet=workbook.sheet_by_name(sheet_name)
        new_workbook=copy(workbook) #将xlrd对象拷贝转化为xlwt对象
        new_worksheet=new_workbook.get_sheet(sheet_name)
        nrows=worksheet.nrows
        ncols=worksheet.ncols
        li=datas
        if type(li) is list:
            '''用于将传入的数据写入excel并清除之前的内容'''
            for i in range(worksheet.nrows):
                '''清空所有数据'''
                for j in range(len(worksheet.row_values(i))):
                    new_worksheet.write(i,j,"")
            style=yangshi1()
            row=li[0]
            for keys in range(len(row)):
                new_worksheet.write(0,keys,list(row.keys())[keys],style)
                #这里.keys()返回的无法取索引，可以转换成list就可以了

            for col_index in range(len(row)):
                for row_index in range(1,len(li)+1):
                    #因为第一行要写KEY值，所以要从第二行开始，最大值要加一，要不会少写一行数据
                    new_worksheet.write(row_index,col_index,list(li[row_index-1].values())[col_index],style)
            if new==None:
                new_workbook.save(file_name)
            elif new =='yes':
                '''如果参数不是None的话就把数据另存'''
                new_workbook.save(file_name)
                othersave(file_name)

            else:
                print('参数错误'+str(traceback.format_exc()))
        elif type(li) is dict:
            '''判断id值在excel表中的第几行'''
            for i in li.keys():
                for v in range(nrows):
                    if i == worksheet.cell(v,2).value:
                        new_worksheet.write(v,9,'',redfont(''))
                        new_worksheet.write(v,9,li[i],redfont(li[i]))
                        # print(li[i])
                        new_workbook.save(file_name)


    except :
        print('打开文件异常%s'%str(traceback.format_exc()))
def othersave(filename,add=None):
    '''
    :param filename:原文件地址
    :param add:附加标识，可不填
    :return:
    '''
    now=time.strftime('%Y-%m-%d-%H-%M-%S')
    workbook=xlrd.open_workbook(filename,formatting_info=True)
    new_workbook=copy(workbook)
    if add==None:
        new_workbook.save(os.path.join(os.path.dirname(filename),(now+'.xls')))
    else:
        new_workbook.save(os.path.join(os.path.dirname(filename),(add+now+'.xls')))

if __name__ == '__main__':
    # print(Readexcel(os.path.join(data_path,'shuju.xlsx')))
    write_excel(os.path.join(data_path,'ssss.xlsx'),'ssssssw',Readexcel(os.path.join(data_path,'shuju.xlsx')),'yes')
