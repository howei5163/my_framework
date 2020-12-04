import time
from common.readConfig import ConfigReader
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#浏览器类封装浏览器操作
class BrowserCommon(object):
    def __init__(self,driver=None):
        if driver:
            self.driver=driver
        else:
            raise RuntimeError('页面类初始化失败')


    #获取当前所有页面句柄
    def get_window_handles(self):
        return self.driver.window_handles

    #返回当前页面句柄
    def get_window_handle(self):
        return self.driver.current_window_handle

    #获取当前页面标题
    def get_title(self):
        return self.driver.title

    #获取当前页面网址
    def get_url(self):
        return self.driver.current_url

    #返回当前驱动
    def get_driver(self):
        return self.driver

    #切换frame
    def switch_to_frame(self,param):
        self.driver.switch_to_frame(param)

    #切换alter
    def suitch_to_alert(self):
        return self.driver.switch_to_alert

    #切换窗口句柄
    def switch_to_window_handle(self,url=""):
        '''
        切换窗口
            窗口数==1，提示只有一个窗口
            窗口数==2，切换到另一个窗口
            窗口数>=3，切换到指定窗口
        '''
        window_handles=self.get_window_handles()
        if len(window_handles)==1:
            pass
        elif len(window_handles)==2:
            other_handle=window_handles[1-window_handles.index(self.get_window_handle())]
            #提取另一个窗口的句柄
            self.driver.switch_to_window(other_handle)
            #切换到另一个窗口
        else:
            for handle in window_handles:
                self.driver.switch_to_window(handle)
                #url 匹配到指定句柄是停止循环
                if url in self.get_url():
                    break

    def close(self):
        self.driver.quit()

    #执行js
    def execute_script(self,js,*args):
        self.driver.execute_script(js,*args)

    #显性等待
    def WebDriverWait(self,driver,timeout=ConfigReader().read('driver')['timeout'],*args):
        '''
        显式等待
        :param times:超时时间，需在config设置
        :param fn:expected_conditions函数
        :return:
        '''
        WebDriverWait(self.driver,timeout,0.5).until(*args)
    def find_element(self,*loc):
        return self.driver.find_element(*loc)

    def find_elemetnts(self,*loc):
        return self.driver.find_elements(*loc)

    def click_element(self,*loc):
        WebDriverWait(self.driver,EC.element_to_be_clickable(self.driver.find_element(*loc)))
        #判断元素是否可点
        self.find_element(*loc).click()

    def input(self,value,*loc):
        #确认元素可点击
        WebDriverWait(self.driver,EC.element_to_be_clickable(self.driver.find_element(*loc)))
        #输入框输入数据
        self.find_element(*loc).send_keys(value)