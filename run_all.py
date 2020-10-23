#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : 侯伟
# @Time : 2020/01/10
# @E-Mail : 714279539@qq.com
import os,time
import smtplib
import unittest,threading
import HTMLTestRunner_cn
from tomorrow import threads
#中文版报告，适用于unittest，带截图和失败重跑
from BeautifulReport import BeautifulReport
#中文版报告，美观，有用例筛选功能
from common.path import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from case.test_morethread import Test_morethread
from case.test_1 import DataDrivenDDT1
#当前脚本所在路径
import subprocess
from multiprocessing.pool import ThreadPool



def add_case(case=case_path,rule='test*.py'):
    #case是存放用例的文件夹，rule是匹配用例脚本名称的规则，默认匹配test开头的
    '''加载所有符合条件的测试用例'''
    #如果不存在这个文件夹，就自动生成一个
    if not os.path.exists(case):os.mkdir(case)
    print('test case path:{}'.format(case))
    #定义discover方法参数
    discover=unittest.defaultTestLoader.discover(case,
                                                 pattern=rule,
                                                 top_level_dir=None)
    print(discover)
    return discover
# @threads(10)其他多线程写法
def run_case_BeautifulReport(all_case,report=report_path):
    '''执行所有用例'''
    now=time.strftime('%Y_%m_%d_%H_%M_%S',time.localtime(time.time()))
    if not os.path.exists(report):os.mkdir(report) #如果不存在的话，则创建一个
    filename=os.path.join(now+'result.html')
    result=BeautifulReport(all_case)
    result.report(filename=filename,description='请下载附件用浏览器打开',log_path=report)
    #filename 输入测试报告名字   log_path 输入测试报告存放位置
    print('运行结束，测试报告保存在%s'%filename)
def run_case_HTMLTestRunner(all_case,report=report_path):
    '''执行所有用例（另一种报告生成方式）'''
    now=time.strftime('%Y_%m_%d_%H_%M_%S')
    if not os.path.exists(report):os.mkdir(report) #如果不存在就创建一个
    report_abspath=os.path.join(report,now+'result.html')
    print('report_path:%s'%report_abspath)
    fp=open(report_abspath,'wb')
    runner=HTMLTestRunner_cn.HTMLTestRunner(stream=fp,
                                         title=u'自动化测试报告，测试结果如下：',
                                         description=u'如想看截图及详情，请下载后用浏览器打开,截图如果看不清楚可以把图片下载放大',
                                            save_last_try=False, #失败重跑用例是否显示，Flase为显示，True为不显示
                                            verbosity=0,#想看详细可以改参数为2
                                            retry=2)# 用例失败重跑次数


    #调用add_case返回
    runner.run(all_case)
    fp.close()
    print('运行结束，测试报告保存在%s'%report_abspath)
def suites(TestCases):
    '''添加一个测试类里的全部用例，如果不想运行某个用例的话可以用@unittest.skip跳过'''
    suite = unittest.TestSuite()
    loder=unittest.TestLoader()
    suite.addTest(loder.loadTestsFromTestCase(TestCases)) #如果有用数据驱动的话用此方法比较好
    return suite
def get_report_file(report_path=report_path):
    '''获取最新的测试报告'''
    lists=os.listdir(report_path)
    lists.sort(key=lambda fn:os.path.getmtime(os.path.join(report_path,fn)))
    print(u'最新测试生成的报告：'+lists[-1])
    #找到最新生成的报告文件
    report_file=os.path.join(report_path,lists[-1])
    return report_file
def send_mail(sender,psw,receivers,smtpserver,report_file,port):
    '''发送测试报告'''
    with open(report_file,'rb')as f:
        mail_body=f.read()
    #定义邮件内容
    msg=MIMEMultipart()
    body=MIMEText(mail_body,_subtype='html',_charset='utf-8')
    msg['Subject']=u'自动化测试报告'
    msg['from']=sender
    msg['to']=",".join(receivers) if isinstance(receivers,list) else receivers
    '''
    经过多次测试发现MIMEText()["to"]的数据类型与sendmail(from_addrs,to_addrs,...)的to_addrs不同；

    前者为str类型，多个地址使用逗号分隔，后者为list类型。
    '''
    msg.attach(body)
    #添加附件
    att=MIMEText(open(report_file,'rb').read(),'base64','utf-8')
    att["Content-Type"]="application/octet-stream"
    att["Content-Disposition"]='attachment;filename="report.html"' #这里可以修改邮件附件的名称
    msg.attach(att)
    try:
        smtp=smtplib.SMTP_SSL(smtpserver,port)
    except:
        smtp=smtplib.SMTP()
        smtp.connect(smtpserver,port)
    #用户名密码
    smtp.login(sender,psw)
    # 此处填写 list格式
    if not isinstance(receivers, list):
        receivers = receivers.split(",")
    smtp.sendmail(sender,receivers,msg.as_string())
    smtp.quit()
    print('test report email has send out!')
def start_test():
    if ConfigReader().read('driver')['driver'].upper()=='CHROME' or '谷歌':
        print('当前浏览器为谷歌浏览器')
        if ConfigReader().read('driver')['headless'].upper()=="Y":
            print('已开启无头浏览器模式')
        if ConfigReader().read('driver')['enable-automation'].upper() == "Y":
            print('已开启反爬虫识别模式')
        if ConfigReader().read('driver')['disable-infobars'].upper() == "Y":
            print('已去除浏览正在受到自动化软件控制字样')
        if ConfigReader().read('driver')['no-sandbox'].upper() == "Y":
            print('以最高权限启动浏览器')
        if ConfigReader().read('driver')['incognito'].upper() == "Y":
            print('已开启无痕浏览器(隐身模式)')
        if ConfigReader().read('driver')['driver_mize'].upper() == "Y":
            print('浏览器窗口设置为最大化')
        elif ConfigReader().read('driver')['driver_mize'].upper() == "N":
            print('浏览器分辨率为{}x{}'.format(ConfigReader().read('driver')['scroll_width'],ConfigReader().read('driver')['scroll_height']))
    if ConfigReader().read('driver')['driver'].upper()=='FIREFOX' or '火狐':
        print('当前浏览器为火狐浏览器')


def close_driver():
    '''强行删除，需要管理员权限'''
    os.system("taskkill /IM chrome.exe /F")
    os.system("taskkill /IM chromedriver.exe /F")
def xiancheng(all_case):
    threads=[]
    for case in all_case:
        t=threading.Thread(target=run_case_BeautifulReport,args=case)
        threads.append(t)
    return threads

def run_threads(all_case):
    i = 0
    for t in xiancheng(all_case):
        i += 1
        print('线程%s启动'%i)
        t.start()
    for t in xiancheng(all_case):
        t.join()
if __name__ == '__main__':
    start_test()
    all_case=suites(DataDrivenDDT1)
    # 只添加一个类里的用例部分用例，参数输入导入的测试类，该类必须继承unittest.TestCase

    # all_case=add_case()
    # #加载所有符合条件的用例

    #其他多线程写法，这种方法会生成3个报告，并将前两个报告的内容统合到第三个报告内
    # threadNum=3
    # pool=ThreadPool(threadNum)
    # pool.map(run_case_BeautifulReport,all_case)
    # pool.close()
    # pool.join() #阻塞主线程，等子线程结束一起结束

    # run_case_BeautifulReport(all_case)
    #用BeautifulRepor执行用例后生成报告，界面美观，自带用例筛选 用例过多时建议用这个 必须把附件下载然后用浏览器打开才能正常显示，缺点截图比较麻烦

    run_case_HTMLTestRunner(all_case)
    # 用HTMLTestRunner执行后生成测试报告,带截图功能,失败重跑，界面简单整洁
    # run_threads(all_case)
    #运行多线程后速度快，但是测试报告的内容会乱，暂时未想到解决办法

    close_driver()
    #强行关闭浏览器，需要管理员权限

    # 获取最新的测试报告文件
    report_path=report_path#报告存放文件夹
    report_file=get_report_file()#获取最新的测试报告
    print('最新的测试报告为%s'%report_file)
    # 邮箱配置
    # sender=ConfigReader().read("email")["sender"]
    # psw=ConfigReader().read("email")["psw"]
    # smtp_server=ConfigReader().read("email")["smtp_server"]
    # port=ConfigReader().read("email")["port"]
    # receivers=ConfigReader().read("email")["receivers"]
    # send_mail(sender,psw,receivers,smtp_server,report_file,port)
    # #最后一步发送报告
