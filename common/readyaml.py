#coding=utf-8
import yaml,os
from common.path import *
def Readyaml(filename):
    with open(filename,'r',encoding='utf-8') as f:
        return yaml.load(str(f.read()))

if __name__ == '__main__':
    a=Readyaml(os.path.join(data_path,'shuju.yaml'))
    # print(a['user'],a['nb1']['user'])
    print(a)
