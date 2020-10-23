"""
logging配置
"""

import os,time
import logging.config
from common.readConfig import ConfigReader
# 定义三种日志输出格式 开始

standard_format = '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]' \
                  '[%(levelname)s][%(message)s]' #其中name为getlogger指定的名字

simple_format = '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'

id_simple_format = '[%(levelname)s][%(asctime)s] %(message)s'

# 定义日志输出格式 结束
#项目地址
# logs = os.path.dirname(os.path.abspath(__file__))  # log文件的目录，这么定的话日志会存放在logger.py所在的文件夹
logs=ConfigReader().read("project")["logs_path"]
#定位项目地址下，名字为logs的文件夹
logfile_name = '%s.log'%time.strftime('%Y_%m_%d')# log文件名

# 如果不存在定义的日志目录就创建一个
if not os.path.isdir(logs):
    os.mkdir(logs)

# log文件的全路径
logfile_path = os.path.join(logs, logfile_name)

# log配置字典
LOGGING_DIC = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': standard_format
        },
        'simple': {
            'format': simple_format
        },
    },
    'filters': {},
    'handlers': {
        #打印到终端的日志
        'console': {
            'level': ConfigReader().read("log")["console_level"],
            'class': 'logging.StreamHandler',  # 打印到屏幕
            'formatter': 'simple'
        },
        #打印到文件的日志,收集info及以上的日志
        'default': {
            'level': ConfigReader().read("log")["default_level"],
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件
            'formatter': 'standard',
            'filename': logfile_path,  # 日志文件
            'maxBytes': 1024*1024*5,  # 日志大小 5M
            'backupCount': 5,
            'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        },
    },
    'loggers': {
        #logging.getLogger(__name__)拿到的logger配置
        '': {
            'handlers': ['default', 'console'],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
            'level': ConfigReader().read("log")["handlers_level"],
            'propagate': True,  # 向上（更高level的logger）传递
        },
    },
}


def load_my_logging_cfg():
    logging.config.dictConfig(LOGGING_DIC)  # 导入上面定义的logging配置
    logger = logging.getLogger(__name__)  # 生成一个log实例
    # logger.info('It works!')  # 记录该文件的运行状态
    return logger
if __name__ == '__main__':
    load_my_logging_cfg().info('sss')
    load_my_logging_cfg().error('错误')
    load_my_logging_cfg().warning('警告')
    load_my_logging_cfg().debug('调试')
    load_my_logging_cfg().critical('严重警告')


