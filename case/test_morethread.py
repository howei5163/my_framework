import unittest,time
from selenium import  webdriver
from common.path import *
class Test_morethread(unittest.TestCase):
    def setUp(self) -> None:
        option=webdriver.ChromeOptions()
        option.add_argument('headless')
        self.driver=webdriver.Chrome(chrome_options=option,executable_path=chromedriver_path)

    def test_case_01(self):
        start=time.strftime('%H:%M:%S')
        print(start)
        self.driver.get('https://www.baidu.com/')
        title=self.driver.title
        try:
            assert title=='百度一下，你就知道'
            print('成功')
        except:
            print('失败')
        end=time.strftime('%H:%M:%S')
        print(end)
    @unittest.skip
    def test_case_02(self):
        start = time.strftime('%H:%M:%S')
        print(start)
        self.driver.get('https://www.baidu.com/')
        title=self.driver.title
        try:
            assert title=='百度一下，你就知道'
            print('成功')
        except:
            print('失败')
            raise
        end = time.strftime('%H:%M:%S')
        print(end)
    @unittest.skip('该用例测试跳过功能是否生效')
    def test_case_03(self):
        '''该用例测试跳过功能是否生效'''
        start=time.strftime('%H:%M:%S')
        print(start)
        self.driver.get('https://www.baidu.com/')
        title=self.driver.title
        try:
            assert title=='百度一下，你就知道'
            print('成功')
        except:
            print('失败')
        end=time.strftime('%H:%M:%S')
        print(end)
    def test_case_04(self):
        start=time.strftime('%H:%M:%S')
        print(start)
        self.driver.get('https://www.baidu.com/')
        title=self.driver.title
        try:
            self.assertEquals( title,'百度一下，你就知道',msg='标题不一样')
            print('成功')
        except:
            print('失败')
        end=time.strftime('%H:%M:%S')
        print(end)
    def test_case_05(self):
        start=time.strftime('%H:%M:%S')
        print(start)
        self.driver.get('https://www.baidu.com/')
        title=self.driver.title
        try:
            assert title=='百度一下，你就知道'
            print('成功')
        except:
            print('失败')
        end=time.strftime('%H:%M:%S')
        print(end)
    def tearDown(self) -> None:
        self.driver.quit()
if __name__ == '__main__':
    unittest.main()