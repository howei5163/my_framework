from page.page_base import Page
from locator.baidu_main import BaiduMainlocator

#百度首页页面类
class BaiduMainPage(Page,):
    #百度首页进入页面
    def jump_to(self,baidu_url=BaiduMainlocator.baidu_url):
        self.driver.get(baidu_url)

    #搜索数据
    def search(self,value):
        '''
        在百度首页输入框输入内容后，点击搜索
        :param value: 输入想搜索的内容
        :return: 返回输入内容后点击搜索的操作
        '''

        self.input(BaiduMainlocator.search_input,value)
        self.click_element(BaiduMainlocator.search_button)
