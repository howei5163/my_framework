#coding:utf-8
import configparser
import os


# config 配置文件读取器
class ConfigReader:
    # 依据 [module] 来读取 config 文件
    def read(self, module):
        """
        读取 ini 配置文件
        :param module: 配置文件的模块参数
        :return: 返回具体某个参数的值
        """
        # 配置文件路径
        self.config_absolute_path = os.path.abspath(os.path.dirname(__file__))[
                                    :os.path.abspath(os.path.dirname(__file__)).find("my_Framework") + len(
                                        "my_Framework")] + '/config/config.ini'
        # 创建配置文件管理者
        self.config_manager = configparser.ConfigParser()
        # 以 utf-8 编码方式读取配置文件
        self.config_manager.read(self.config_absolute_path, encoding="utf-8")
        # 返回读取配置文件内容字典
        return dict(self.config_manager.items(module))

    # 返回配置文件的绝对路径
    def get_config_absolute_path(self):
        return self.config_absolute_path