#coding=utf-8
import time
def runtime(func):
    def wrapper(*args,**kwargs):
        '''两个参数代表函数的参数'''
        start=time.time()
        print('开始时间%s'%(time.strftime('%Y-%m-%d %H:%M:%S')))
        f=func(*args,**kwargs)#原函数
        end=time.time()
        print('运行时长:%.4f秒'%(end-start))
        #小数点后4位
        return f
    return wrapper


class Runtime():
    def __init__(self,func):
        self.func=func
    def __call__(self, *args, **kwargs):
        start = time.time()
        print('开始时间%s' % (time.strftime('%Y-%m-%d %H:%M:%S')))
        f = self.func(*args, **kwargs)  # 原函数
        end = time.time()
        print('运行时长:%.4f秒' % (end - start))
        # 小数点后4位
        return f