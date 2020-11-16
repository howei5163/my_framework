#coding=utf-8
from unittest import mock
import requests,unittest
import urllib3
class Jiekou():
    '''mock一般用在第三方接口无法调用的情况，或者开发接口还没有做完的时候'''
    def jiekou(self,url,params,headers):
        urllib3.disable_warnings()
        r=requests.get(url=url,params=params,headers=headers,verify=False)
        return r.status_code
    def send_requests(self):
        url = 'https://api.ioser.net/api/get_phone_info'
        params = {"phone": 31531513553,
                  "access_token": "6hDyzeQknSytd8E3gtSaSKGy4uSAmx1s"}
        headers = {"Accept": "*/*",
                   "Accept-Encoding": "gzip, deflate, br",
                   "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                   "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
                   "X-Requested-With": "XMLHttpRequest"}
        r=self.jiekou(url,params,headers)
        return r

class Testjiekou(unittest.TestCase):
    def setUp(self) -> None:
        self.jiekou=Jiekou()
    def test_success_requests(self):
        self.jiekou.jiekou=mock.Mock(return_value=200)
        '''把接口返回结果模拟成200'''
        r=self.jiekou.send_requests()
        self.assertEquals(r,200)
    @unittest.skip
    def test_fail_requests(self):
        self.jiekou.jiekou=mock.Mock(return_value=404,side_effect=self.jiekou.jiekou)
        '''吧接口返回结果模拟成404,side_effect参数会覆盖return_value，用真实数据进行测试'''
        r=self.jiekou.send_requests()
        self.assertEquals(r,404)
if __name__ == '__main__':
    unittest.main()