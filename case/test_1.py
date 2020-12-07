#coding=utf-8
import traceback  #使用后可以定位到具体的错误位置
import unittest,os
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException  #该包用于找不到元素
from common import logger
import ddt,time,threading
from selenium.webdriver.support.wait import WebDriverWait  #显性等待
from selenium.webdriver.support import expected_conditions as EC
from common.readexcel import Readexcel
from BeautifulReport import BeautifulReport
from common.path import *
from selenium.webdriver.common.by import By
from page.baidu_main_page import BaiduMainPage
from common.driver import Driver
import random
log = logger.load_my_logging_cfg()
'''该用例主要是演示调用excal的用法'''
@ddt.ddt
class DataDrivenDDT1(unittest.TestCase,BaiduMainPage):
    @classmethod
    def setUpClass(cls) -> None:
        # Chrome_path=chromedriver_path
        # option = webdriver.ChromeOptions()
        # option.add_argument('--headless') #设置谷歌无头浏览器
        # option.add_argument("--start-maximized") #设置谷歌浏览器打开就是最大的
        # option.add_experimental_option('excludeSwitches',['enable-automation'])
        # #反爬虫识别，如果不开这个，在进行登录的时候部分网站会让输入验证码等一些麻烦的识别操作
        # # option.add_argument("--disable-infobars")
        # #浏览器打开时会有一个浏览正在受到自动化软件控制，上面的代码可以去掉，不过无头浏览器加不加这个都行，反正也看不见么
        # # option.add_argument('--no-sandbox')
        # #以最高权限启动
        #
        # cls.driver = webdriver.Chrome(chrome_options=option,executable_path=Chrome_path)
        print('test_1开始测试')
        # cls.assembler=Driver()
        # cls.driver=cls.assembler.get_driver()
        # cls.mysql=cls.assembler.get_mysql()
    def setUp(self):
        self.assembler = Driver()
        self.driver = self.assembler.get_driver()
        self.mysql = self.assembler.get_mysql()
        # url = "http://www.baidu.com"
        self.jump_to()
        self.imgs=[]
        self.addCleanup(self.cleanup)  #每次执行完自动删除图片
    def add_imgs(self):  #如果用HTMLTestRunner_cn截图的话得写这个方法
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True

    def save_img(self,img_name):
        '''BeautifulReport截图方法'''
        self.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(img_path), img_name))
    def cleanup(self):
        '''清除图片'''
        pass
    @ddt.data(*Readexcel(os.path.join(data_path,'shuju.xlsx')))
    @ddt.unpack
    # @BeautifulReport.add_test_img('百度首页访问截图','测试成功后截图','测试失败后截图1','测试失败后截图2','测试失败后截图3')
    def test_dataDrivenByDDT1(self, testdata, expectdata):
        '''搜索testdata内容后，看expectdata内容在不在当前页面源码中'''
        self.save_img('百度首页访问截图')
        #调用数据库
        try:
            # WebDriverWait(self.driver,20).until(lambda driver:self.driver.find_element_by_id("kw"))
            # self.driver.find_element_by_id("kw").send_keys(testdata)
            self.search(testdata)
            # WebDriverWait(self.driver,20,0.5).until(EC.title_is("百度一下，你就知道")) #判断标题是否某个值，返回布尔值
            WebDriverWait(self.driver,EC.title_is('百度一下，你就知道'))
            self.add_imgs()
            time.sleep(3)
            self.add_imgs()
            self.assertTrue(expectdata in self.driver.page_source)
        except NoSuchElementException as e:
            self.add_imgs()
            log.error(u"查找的页面元素不存在，异常堆栈信息:" + str(traceback.format_exc()))
            print(u"查找的页面元素不存在，异常堆栈信息:" + str(traceback.format_exc()))
            # self.save_img('测试失败后截图1')
            raise
            #这里如果不释放异常的话，HTMLTestRunner_cn的用例失败重跑功能不会执行
        except AssertionError as e:
            self.add_imgs()
            print(u"搜索 '%s',期望出现 '%s' ,失败" % (testdata, expectdata))
            log.error(u"搜索 '%s',期望出现 '%s' ,失败" % (testdata, expectdata))
            print('异常报错：%s'%traceback.format_exc())
            # self.save_img('测试失败后截图2')
            raise

        except Exception as e:
            self.add_imgs()
            print(u"未知错误，错误信息：" + str(traceback.format_exc()))
            log.error(u"未知错误，错误信息：" + str(traceback.format_exc()))
            # self.save_img('测试失败后截图3')
            raise
        else:
            self.add_imgs()
            print(u"搜索 '%s',期望出现 '%s' ,通过" % (testdata, expectdata))
            log.info(u"搜索 '%s',期望出现 '%s' ,通过" % (testdata, expectdata))
            # self.save_img('测试成功后截图')
    def tearDown(self):
        '''每次结束后关闭浏览器'''
        self.assembler = Driver()
        self.assembler.disassemble_driver()
    @classmethod
    def tearDownClass(cls) -> None:
        print('test_1测试结束')


if __name__ == '__main__':
    unittest.main()