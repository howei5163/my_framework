#coding=utf-8
import requests
from jiekouauto.check_res import check_res
def send(method,url,data,headers,id,yuqi):
    '''
    发送请求
    :param method:请求方式
    :param url: 接口地址
    :param data: 请求参数
    :param headers: 请求头
    :param id :用例id
    :param yuqi: 预期结果
    :return:
    '''
    li = {}
    try:
        if method.lower() == 'get':
            r = requests.get(url, params=data, headers=headers)
            print('状态码：%s'%r.status_code)
            result = check_res(r.text, yuqi)
            li[id] = result
            li['实际结果']=r.text
            li['返回状态吗']=r.status_code
            # print(r.text)
        elif method.lower() == 'post':
            r = requests.post(url, data=data, headers=headers)
            print('状态码：%s'%r.status_code)
            result = check_res(r.text, yuqi)
            li[id] = result
            li['实际结果'] = r.text
            li['返回状态吗'] = r.status_code
        else:
            print('接口类型不是post或get')
            li[id]=False
    except Exception as a:
        print('[%s]用例接口调用失败：%s' % (id,a))
        li[id]=False
    return li