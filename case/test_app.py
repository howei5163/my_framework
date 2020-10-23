# -*- encoding=utf8 -*-
__author__ = "侯伟"
import unittest,os
from airtest.core.api import *
from airtest.aircv import * #airtest截图库
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.cli.parser import cli_setup
import logging
logger=logging.getLogger("airtest")
logger.setLevel(logging.ERROR)
project_path = os.path.join("e:\\new_jiekou")
app_path = os.path.join(project_path, "case")
report_path = os.path.join(project_path, "report")
applog_path=os.path.join(project_path,'applog')
# def setUpModule():
#     connect_device('Android//127.0.0.1:5037/emulator-5554')
#     start_app('')
# script content
class Testapp(unittest.TestCase):
    def setUp(self) -> None:
        self.poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
        if not cli_setup():
            auto_setup(app_path, devices=["Android://127.0.0.1:5037/emulator-5554"], logdir=applog_path)
        start_app('com.tencent.mtt.x86')
        ST.SNAPSHOT_QUALITY = 75  # 设置全局的截图压缩精度
        if G.DEVICE.display_info['orientation'] in [1,3]:
            '''判断当前手机是横屏还是竖屏，并获取当前分辨率，相对坐标=绝对坐标/width or height'''
            '''touch使用绝对坐标，poco使用相对坐标'''
            self.height=G.DEVICE.display_info['wigth']
            self.width=G.DEVICE.display_info['height']
        else:
            self.height=G.DEVICE.display_info['height']
            self.width=G.DEVICE.display_info['width']
        self.screen=G.DEVICE.snapshot()  #调用举报截图函数
    @unittest.skip('app用例单独测试')
    def test_app(self):
        self.poco(name='android.view.View').wait_for_appearance()
        self.poco(name='android.view.View').click()
        self.poco(text="搜索或输入网址").click()
        text("测试",enter=False)
        screen=aircv.crop_image(self.screen,(27,98,902,197))
        self.poco.swipe([0.5,0.5],[0.1,0.1])
        # try_log_screen(screen) #报错局部截图到log文件中
        # 生成测试报告
        dev=device()
        dev.swipe_along([[959, 418],[1157, 564],[1044, 824],[751, 638],[945, 415]])
        '''长距离多点滑动'''
        dev.pinch(in_or_out='in', center=None, percent=0.5)
        '''双指向内捏合动作，向外的话in改成out'''
        from airtest.report.report import simple_report
        simple_report(__file__,logpath=applog_path,output=(os.path.join(report_path,'%s.html')%(time.strftime('%Y-%m-%d-%H-%M-%S')))) #用airtest的方法生成报告,徐填写log.txt的位置，以及输出报告的位置
    def tearDown(self) -> None:
        stop_app('com.tencent.mtt.x86')
        '''每次结束后关闭APP'''


if __name__ == '__main__':
    unittest.main()














