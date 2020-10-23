#coding=utf-8
from bs4 import BeautifulSoup
from common.path import *
from selenium import webdriver
import os,re,requests,time
from common.driver import Driver
from tomorrow import threads
class Dowload_img():
    def __init__(self):
        ass=Driver()
        self.driver=ass.get_driver()

    def get_page_source(self,page,name):
        '''
        :param page:要下拉多少页
        :param name: 要下载的图片类别
        :return:
        '''
        print('开始时间%s' % (time.strftime('%Y-%m-%d %H:%M:%S')))
        # option=webdriver.ChromeOptions()
        # option.add_argument('headless')
        # driver=webdriver.Chrome(chrome_options=option,executable_path=chromedriver_path)
        self.driver.get('https://www.baidu.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        print(self.driver.title)
        self.driver.find_element_by_id('kw').send_keys(name)
        self.driver.find_element_by_id('su').click()
        self.driver.find_element_by_xpath('//div[@id="s_tab"]/div/a[3]').click()
        self.driver.find_element_by_id('kw').clear()
        self.driver.find_element_by_id('kw').send_keys(name)
        self.driver.find_element_by_xpath('//div[@id="search"]/form/span[2]').click()

        for i in range(page):
            '''利用JS操作滚动条下拉几次，可以显示更多的源码'''
            self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(1)
        a=self.driver.page_source
        soup=BeautifulSoup(a,'html.parser')#如果是xml就改成xml.parser
        list=soup.find_all(class_='main_img img-hover')
        #定位单一元素
        # list=soup.find_all('img',{'class':'main_img img-hover'})
        #定位img标签下的class元素
        return list
    @threads(6,timeout=0.1)
    def img_list(self,page,name,filename,g):
        '''
        :param list:
        :param filename: 存放图片的地址
        :param g: 每次要下载多少张图片
        :return: 本次下载的图片列表
        '''
        list=self.get_page_source(page,name)
        li = []
        n=0
        head = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'
        }
        if not os.path.exists(filename):os.mkdir(filename)
        '''如果没有该文件夹就建一个'''
        for l in list:
            patten = re.search('u=([\d]+)', l['data-imgurl'], re.S)
            try:
                if not '%s.jpg'%patten.group(1) in os.listdir(filename):
                    '''不需要重复的图片'''
                    n += 1
                    with open(os.path.join(filename,'%s.jpg'%patten.group(1)),'wb') as f:
                        r=requests.get(url=l['data-imgurl'],headers=head)
                        f.write(r.content)
                        li.append(patten.group(1))
                        if n==g:
                            break
            except:
                print('%s拷贝时出问题'%patten.group())
        print('%s文件夹中共有%s张图片' % (filename,len(os.listdir(filename))))
        print('本次共爬%s张图片' % n)
        self.driver.quit()
        print('结束时间%s'%time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        return li


if __name__ == '__main__':
    li=['动漫美女','美图','风景','游戏美图','美女','新游戏','动漫新番']
    for name in li:
            dowload = Dowload_img()
            # list=dowload.get_page_source(30,name)
            dowload.img_list(1,name,os.path.join(img_path,name),50)