# coding:utf-8
import unittest
from selenium import webdriver
import ddt,os
from common.path import *
from common.readexcel import Readexcel
from tomorrow import threads
from common.logger import load_my_logging_cfg
log=load_my_logging_cfg()
@ddt.ddt
class Test_yuansu(unittest.TestCase):
    '''该用例是为了尝试截取单个元素'''
    @classmethod
    def setUpClass(cls) -> None:
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        option.add_argument("--start-maximized")
        #默认浏览器最大化
        # option.add_argument("disable-infobars")
        '''浏览器打开时会有一个浏览正在受到自动化软件控制，上面的代码可以去掉，
        不过无头浏览器加不加这个都行，反正也看不见吗'''
        cls.driver = webdriver.Chrome(chrome_options=option)

    @ddt.data(*Readexcel(os.path.join(data_path,'yuansu.xlsx')))
    @ddt.unpack
    def test_yuansu(self,element):
        '''测试截图单个元素'''
        self.driver.get('http://www.baidu.com/')
        self.driver.maximize_window()
        self.ele=self.driver.find_element_by_id(element)
        self.add_imgs(self.ele)
        print('图片已截图')
        log.info('已截图')
    def setUp(self):
        # 在python3.x 中，如果在这里初始化driver ，因为3.x版本 unittest 运行机制不同，会导致用例失败后截图失败
        self.imgs=[]
        self.addCleanup(self.cleanup)  #每次执行完自动删除图片
    def add_imgs(self,ele):
        self.imgs.append(self.ele.screenshot_as_base64)
        return True
    def cleanup(self):
        '''清除图片'''
        pass
    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
if __name__ == '__main__':
    unittest.main()