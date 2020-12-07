#coding=utf-8
import requests
from bs4 import BeautifulSoup
from common.readexcel import Readexcel,write_excel,othersave
from common.path import *
import os,unittest,json,traceback,time,random,re
from common.readtxt import readtxt
from ddt import ddt,data
from jiekouauto.send_request import send
from common.imgbase64 import imgbase64
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
        params=eval((self.panduan(data).replace((re.search('\"icrInCode\": \"(.+?)\"',str(self.panduan(data)),re.S).group(1)),self.suiji(data))))
        params['data']=json.dumps(params['data'])
        xiugai = data['请求数据'].split(',')
        for i in xiugai:
            if i =='':
                '''如果请求数据中没有数据，不修改'''
                pass
            else:
                i=i.split('=')
                j=i[0].strip("''").strip('""')
                k=i[1].strip("''").strip('""')
                '''用用例中的数据替换掉读取的数据'''
                if j=='image'.strip("''"):
                    '''如果是有限的图片地址，需要先转为base64格式'''
                    if imgbase64(k)==None:
                        params['data']=json.loads(params['data'])
                        params['data'][j]=k
                        params['data']=json.dumps(params['data'])
                    else:
                        params['data']=json.loads((params['data']))
                        params['data'][j]=imgbase64(k)
                        params['data']=json.dumps(params['data'])
                else:
                    if j in params['data']:
                        '''先将json转换为字典格式'''
                        params['data']=json.loads(params['data'])
                        params['data'][j]=k
                        params['data']=json.dumps(params['data'])
                    else:
                        params[j]=k
        yuqi=data['预期结果']
        msg=data['用例描述']
        id=data['用例id']
        if (headers is not None and headers.strip()!=''):
            '''将数据转换为字典类型'''
            headers=eval(headers)
        print('用例描述：%s'%msg)
        li=send(method,url,params,headers,id,yuqi)
        write_excel(os.path.join(data_path,'数据.xls'),'用例',li)
        '''将测试结果写入excel'''
    def panduan(self,data):
        if data['卡证类型']=='身份证反面':
            params=readtxt(os.path.join(data_path,'身份证反面'))
        elif data['卡证类型']=='身份证正面':
            params=readtxt(os.path.join(data_path,'身份证正面'))
        elif data['卡证类型']=='银行卡':
            params=readtxt(os.path.join(data_path,'银行卡'))
        return params
    def suiji(self,data):
        if data['卡证类型']=='身份证反面':
            number='测试-0102-'+str(time.strftime('%y-%m-%d-%H-%M-%S'))+str(random.randint(0,9))
        elif data['卡证类型']=='身份证正面':
            number='测试-0102-'+str(time.strftime('%y-%m-%d-%H-%M-%S'))+str(random.randint(0,9))
        elif data['卡证类型'] == '银行卡':
            number = '测试-0102-' + str(time.strftime('%y-%m-%d-%H-%M-%S')) + str(random.randint(0, 9))
        print('任务号：%s'%number)
        return number
    @classmethod
    def tearDownClass(cls) -> None:
        '''将excel另存'''
        # othersave(os.path.join(data_path,'数据.xls'),'接口测试结果')
        print('接口测试结束')
if __name__ == '__main__':
    unittest.main(verbosity=2)
