#coding=utf-8
import requests
from bs4 import BeautifulSoup
from common.readexcel import Readexcel,write_excel,othersave
from common.path import *
import os,unittest,json,traceback
from ddt import ddt,data
from jiekouauto.send_request import send
@ddt
class Testtianqi(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        case=Readexcel(os.path.join(data_path,'数据.xls'),'用例')
        print('接口测试开始,共%s条用例'%len(case))
    @data(*Readexcel(os.path.join(data_path,'数据.xls'),'用例'))
    def test_tianqi(self,data):
        url=data['请求url']
        method=data['请求方式']
        headers=data['请求头']
        params=data['请求数据']
        yuqi=data['预期结果']
        msg=data['用例描述']
        id=data['用例id']
        if (headers is not None and headers.strip()!=''):
            '''将数据转换为字典类型'''
            headers=eval(headers)
        if (params is not None and params.strip()!=''):
            params=eval(params)
        li=send(method,url,params,headers,id,yuqi)
        write_excel(os.path.join(data_path,'数据.xls'),'用例',li,'yes')
        '''将测试结果写入excel'''

    @classmethod
    def tearDownClass(cls) -> None:
        '''将excel另存'''
        othersave(os.path.join(data_path,'数据.xls'),'接口测试结果')
        print('接口测试结束')
if __name__ == '__main__':
    unittest.main(verbosity=2)
