from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.browser_common import BrowserCommon

class Page(BrowserCommon):
    #基本方法封装

    def find_element_by_xpath(self,xpath):
        '''
        通过xpath找元素
        :param xpath:元素定位
        :return: 原生通过xpath找元素方法
        '''
        return self.driver.find_element_by_xpath(xpath)

    def find_elements_by_xpath(self,xpath):
        '''
        通过xpath找多个元素
        :param xpath: 元素定位
        :return: 原生通过xpath找元素方法
        '''
        return self.driver.find_elements_by_xpath(xpath)


    def find_elemetnt(self,*args):
        '''
        找单个元素
        :param args: 定位与通过什么定位
        :return: 元素找多元素方法
        '''
        return self.driver.find_element(*args)

    def find_elemetnts(self,*args):
        '''
        找多个元素
        :param args:定位与通过什么定位
        :return: 元素找多元素方法
        '''
        return self.driver.find_elements(*args)

    def click_element(self,xpath):
        '''
        点击元素
        :param xpath:元素定位
        :return: 返回原生点击事件
        '''
        WebDriverWait(self.driver,20,0.1).until(EC.element_to_be_clickable(("xpath",xpath)))
        #判断元素是否可点
        self.driver.find_element_by_xpath(xpath).click()

    def input(self,xpath,value):
        '''
        输入值
        :param xpath: 元素定位
        :param value: 输入值
        :return: 返回send_keys原生方法
        '''
        #确认元素可点击
        WebDriverWait(self.driver,20,0.1).until(EC.element_to_be_clickable(("xpath",xpath)))
        #输入框输入数据
        self.driver.find_element_by_xpath(xpath).send_keys(value)
