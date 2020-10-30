#coding=utf-8
from common.path import *
from bs4 import BeautifulSoup
import os,re
from selenium import webdriver
import time
import requests
import random,unittest
from selenium.webdriver.support.wait import WebDriverWait
from common.driver import Driver
# option=webdriver.ChromeOptions()
# '''bilibili应该有反爬机制，每次只要浏览器无头，就会有元素找不到'''
# option.add_argument('--headless')
# option.add_argument('--disable-gpu')
# option.add_experimental_option('excludeSwitches', ['enable-automation'])
# driver=webdriver.Chrome(chrome_options=option,executable_path=chromedriver_path)
class Test(unittest.TestCase):
    def  setUp(self) -> None:
        assemble = Driver()
        self.driver = assemble.get_driver()
        self.driver.get('https://www.bilibili.com')
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//input[@class="nav-search-keyword"]').clear()
        self.driver.find_element_by_xpath('//input[@class="nav-search-keyword"]').send_keys('【公主连结】天秤座B1')
        a=self.driver.current_window_handle
        #截取当前网页handle
        self.driver.find_element_by_xpath('//div[@class="nav-search-btn"]').click()
        # driver.quit()
        b=self.driver.window_handles
        def switch(a):
            #判断当前网页handle与之前是否相同，不相同就切换到新的网页
            for i in b:
                if i==a:
                    pass
                else:
                    self.driver.switch_to_window(i)
        switch(a)
    def zhou(self):
        link=self.driver.find_elements_by_xpath("//a[@class='img-anchor']")
        #定位到所有需要的视频连接
        n=0
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}
        globals()['a']=headers
        '''把headers添加到全局变量'''
        for j in link:
            url=j.get_attribute('href')
            #获取url
            m=requests.get(url,headers)
            soup=BeautifulSoup(m.content,'html.parser')
            h=soup.find_all('div',class_='info')
            k=soup.find_all('h1',class_='video-title')
            patten=re.search('<h1 class=\"video-title\" title=\"(.+?)\">',str(k[0]),re.S)
            pa=patten.group(1)
            li={"<",">","《","》","@","#","$","%","^","&","*","(",")","!","[","]","【","】","（","）",":","："}
            for i in li:
                pa=pa.replace(i,'')
                #吧特殊符号去除
            if not '台服'in pa:
                if not '日服' in pa:
                    if not "A" in pa:
                        if str(random.randint(0,9)) in pa:
                            if len(pa) >40:
                                with open(os.path.join('d:\\公主链接作业','%s.txt')%(pa),'a',encoding='utf-8') as f:
                                    f.write(str(h[0]))
                                    n+=1
                                    print("已经爬虫%s个，文件名%s"%(n,(pa))+".txt")
    def test_xiayiye(self):
        n=0
        try:
            for s in range(100):
                n+=1
                print('第%s页'%n)
                self.zhou()
                self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
                time.sleep(2)
                self.driver.find_element_by_xpath('//li[@class="page-item next"]').click()
        except:
            print('没有下一页了')
        print(globals()['a'])
    def tearDown(self) -> None:
        self.driver.quit()
if __name__ == '__main__':
    unittest.main()