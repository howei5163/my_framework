#coding=utf-8
import os,base64
from common.path import *
def imgbase64(image_bytes):
    '''将图片转为base64'''
    try:
        with open(image_bytes,'rb')as fb:
            img=fb.read()
            base64_bytes=base64.b64encode(img)
            image=base64_bytes.decode('utf-8')
        return image
    except:
        return None