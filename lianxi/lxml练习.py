#coding=utf-8
from lxml import etree
#requests 请求跳过ssl验证时会弹出警告，加以下两行代码可取消
import urllib3
urllib3.disable_warnings()

htmldemo = '''
<meta charset="UTF-8"> <!-- for HTML5 -->
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<html><head><title>yoyo ketang</title></head>
<body>
<b><!--Hey, this in comment!--></b>
<p class="title"><b>yoyoketang</b></p>
<p class="yoyo">这里是我的微信公众号：yoyoketang
<a href="http://www.cnblogs.com/yoyoketang/tag/fiddler/" class="sister" id="link1">fiddler教程</a>,
<a href="http://www.cnblogs.com/yoyoketang/tag/python/" class="sister" id="link2">python笔记</a>,
<a href="http://www.cnblogs.com/yoyoketang/tag/selenium/" class="sister" id="link3">selenium文档</a>;
快来关注吧！</p>
<p class="story">...</p>
'''

demo=etree.HTML(htmldemo)
t=etree.tostring(demo,encoding='utf-8',pretty_print=True)
#要打印html内容，可以用etree.tostring方法，pretty_print=True是以标准格式输出
# print(t.decode('utf-8'))

texts=demo.xpath('//p[@class="yoyo"]')
#返回一个列表，和BS4的findall方法差不多
t=texts[0].text
print(texts[0].attrib)
#打印元素属性，返回字典格式
for i in texts:
    print(etree.tostring(i,encoding='utf-8',pretty_print=True).decode('utf-8'))

t1=texts[0].xpath('//a[@id="link2"]')
#继续定位该元素的子节点
print(t1[0].text)
print([i.text for i in texts[0]])

print(t1[0].tag)
#获取当前节点标签名

print(t1[0].get('class'))
#获取某个元素属性

print([i.text for i in t1[0].iter()])
#iter()获取所有子节点
print(t1[0].xpath('text()'))
#获取当前节点下所有文本
print(t1[0].xpath('.//text()'))
#获取本节点和子节点所有文本
print(t1[0].getparent().tag)
#获取父节点