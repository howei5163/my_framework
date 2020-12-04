#百度首页元素定位
from selenium.webdriver.common.by import By
class BaiduMainlocator:
    #百度首页input定位
    search_input=(By.ID,"kw")

    #百度首页搜索键定位
    search_button=(By.XPATH,"//input[@id='su']")

    #百度首页url
    baidu_url='https://www.baidu.com/'