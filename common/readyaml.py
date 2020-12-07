#coding=utf-8
import yaml,os,sys,io
from common.path import *
from ruamel import yaml
'''pip install ruamel.yaml'''

def Readyaml(filename):
    with open(filename,'r',encoding='utf-8') as f:
        return yaml.load(str(f.read()),Loader=yaml.Loader)
def writeyaml(filename,data,type='w'):
    with open(filename,type,encoding='utf-8') as f:
        yaml.dump(data,f,allow_unicode=True,Dumper=yaml.RoundTripDumper)
if __name__ == '__main__':
    a=Readyaml(os.path.join(data_path,'shuju.yaml'))
    # print(a['user'],a['nb1']['user'])
    print(a)
    # writeyaml(os.path.join(data_path,'shuju.yaml'),a,'a')
