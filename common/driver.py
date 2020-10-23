import os
import threading
from selenium import webdriver
from common.readConfig import ConfigReader
from common.readmysql import Mysql
from common.path import *
#初始装配工具(一个线程分配一个驱动，一个mysql)
class Driver:
    def __init__(self):
        #驱动装配
        self.assemble_driver()
        if ConfigReader().read('mysql')['open'].upper()=="Y":
            self.assemble_mysql()
        else :
            self.mysql_tool=None

    def assemble_driver(self):
        if  ConfigReader().read('driver')['driver'].upper()=="CHROME" or "谷歌":
            option=webdriver.ChromeOptions()
            if ConfigReader().read('driver')['headless'].upper()=="Y":
                option.add_argument('--headless')  # 设置谷歌无头浏览器

            if ConfigReader().read('driver')['enable-automation'].upper()=="Y":
                option.add_experimental_option('excludeSwitches', ['enable-automation'])
                # 反爬虫识别，如果不开这个，在进行登录的时候部分网站会让输入验证码等一些麻烦的识别操作

            if ConfigReader().read('driver')['disable-infobars'].upper()=="Y":
                option.add_argument('--disable-infobars')
                # 设置禁用浏览器正在被自动化程序控制的提示，有些网站会通过这个提示来识别爬虫

            if ConfigReader().read('driver')['no-sandbox'].upper() == "Y":
                option.add_argument('--no-sandbox')
                # 以最高权限启动
            if ConfigReader().read('driver')['incognito'].upper() == "Y":
                option.add_argument('--incognito')
                # 开启无痕浏览器
            if  ConfigReader().read('driver')['disable-gpu'].upper() == "Y":
                option.add_argument('--disable-gpu')  # 禁用GPU硬件加速。如果软件渲染器没有就位，则GPU进程将不会启动。
            if  ConfigReader().read('driver')['hide-scrollbars'].upper() == "Y":
                option.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
            if  ConfigReader().read('driver')['disable-pciture'].upper() == "Y":
                option.add_argument('blink-settings=imagesEnabled=false') 
                # 不加载图片, 提升速度
            if ConfigReader().read('driver')['phone'].upper() == "Y":
                phone_size=ConfigReader().read('phone')['phone_size']
                option.add_experimental_option('mobileEmulation', {'deviceName':phone_size})
                print('当前设备为%s'%phone_size)
                #模拟手机打开浏览器
            self.driver = webdriver.Chrome(chrome_options=option, executable_path=chromedriver_path)
            if ConfigReader().read('driver')['driver_mize'].upper() == "Y":
                '''设置打开浏览器的大小'''
                self.driver.maximize_window()
                self.driver.implicitly_wait(ConfigReader().read('driver')['implicitly_wait'])

            elif ConfigReader().read('driver')['driver_mize'].upper() == "N":
                scroll_width = ConfigReader().read('driver')['scroll_width']
                scroll_height =ConfigReader().read('driver')['scroll_height']
                # 设置窗口分辨率
                self.driver.set_window_size(scroll_width, scroll_height)
                self.driver.implicitly_wait(ConfigReader().read('driver')['implicitly_wait'])
            else:
                raise RuntimeError('config中driver信息输入错误')
        elif  ConfigReader().read('driver')['driver'].upper()=="FIREFOX" or "火狐":
            '''
            火狐浏览器目前没打算用，如果需要的话可以再次进行开发
            '''
            fire_options=webdriver.FirefoxOptions()
            fire_options.add_argument('no-sandbox')
            self.driver=webdriver.Firefox(executable_path=firefoxdriver_path,firefox_options=fire_options)

    #获取驱动
    def get_driver(self):
        return self.driver

    def disassemble_driver(self):
        if self.driver is not None:
            self.driver.quit()
            self.driver=None

    def assemble_mysql(self):
        self.mysql_tool=Mysql()
        self.mysql_tool.get_db_conn()

    #关闭游标与连接
    def disassemble_mysql(self):
        if self.mysql_tool is not None:
            self.mysql_tool.close_mysql()
            self.mysql_tool=None
    #获取数据库
    def get_mysql(self):
        return self.mysql_tool
