#coding=utf-8
import traceback  #使用后可以定位到具体的错误位置
import unittest,os
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException  #该包用于找不断元素
from common import logger
import ddt,time
from common.readtxt import Readtxt
from common.path import *
from common.path import *
log = logger.load_my_logging_cfg()
'''该用例主要是眼熟调用txt文件的用法'''
@ddt.ddt
class DataDrivenDDT2(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        option.add_argument("--start-maximized")
        # 默认浏览器最大化
        # option.add_argument("disable-infobars")
        '''浏览器打开时会有一个浏览正在受到自动化软件控制，上面的代码可以去掉，
        不过无头浏览器加不加这个都行，反正也看不见吗'''
        cls.driver = webdriver.Chrome(chrome_options=option,executable_path=chromedriver_path)
        cls.driver.maximize_window()
    def setUp(self):
        # 在python3.x 中，如果在这里初始化driver ，因为3.x版本 unittest 运行机制不同，会导致用例失败后截图失败
        self.imgs=[]
        self.addCleanup(self.cleanup) # 每次执行完自动删除图片
    def add_imgs(self):
        #想要report报告中有截图就加入此模块
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True
    def cleanup(self):
        '''清除图片'''
        pass
    @ddt.data(*Readtxt(os.path.join(data_path,'shuju.txt')))
    @ddt.unpack
    # @unittest.skip
    # 跳过用例
    def test_dataDrivenByDDT2(self, testdata, expectdata):
        url = "http://www.baidu.com"
        self.driver.get(url)
        self.driver.implicitly_wait(30)
        scroll_width = 1600
        scroll_height = 1500
        self.driver.set_window_size(scroll_width, scroll_height)
        #规定截图大小
        self.add_imgs()
        try:
            self.driver.find_element_by_id("kw").send_keys(testdata)
            self.driver.find_element_by_id("su").click()
            self.add_imgs()
            time.sleep(3)
            self.add_imgs()
            self.assertTrue(expectdata in self.driver.page_source)
        except NoSuchElementException as e:
            self.add_imgs()
            log.error(u"查找的页面元素不存在，异常堆栈信息:" + str(traceback.format_exc()))
            print(u"查找的页面元素不存在，异常堆栈信息:" + str(traceback.format_exc()))
            raise
        except AssertionError as e:
            self.add_imgs()
            print(u"搜索 '%s',期望出现 '%s' ,失败" % (testdata, expectdata))
            log.error(u"搜索 '%s',期望出现 '%s' ,失败" % (testdata, expectdata))
            raise
        except Exception as e:
            self.add_imgs()
            print(u"未知错误，错误信息：" + str(traceback.format_exc()))
            log.error(u"未知错误，错误信息：" + str(traceback.format_exc()))
            raise
        else:
            self.add_imgs()
            print(u"搜索 '%s',期望出现 '%s' ,通过" % (testdata, expectdata))
            log.info(u"搜索 '%s',期望出现 '%s' ,通过" % (testdata, expectdata))
    def test_002(self):
        '''这条用例是为了测试失败后用例会不会重跑'''
        a,b=3,5
        assert a+b==9
        print('成功')
        log.info('成功')
    def tearDown(self):
        pass
    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()



if __name__ == '__main__':
    unittest.main()