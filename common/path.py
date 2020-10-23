import os
from common.readConfig import ConfigReader
u'''这里存放路径'''
project_path=os.path.dirname(os.path.abspath(__file__))[:os.path.dirname(os.path.abspath(__file__)).find('my_Framework')+len('my_Framework')]
report_path=project_path+ConfigReader().read('project')['report_path']
logs_path=project_path+ConfigReader().read('project')['logs_path']
case_path=project_path+ConfigReader().read('project')['case_path']
data_path=project_path+ConfigReader().read('project')['data_path']
chromedriver_path=project_path+ConfigReader().read('driver')['chromedriver_path']
firefoxdriver_path=project_path+ConfigReader().read('driver')['firefoxdriver_path']
img_path=project_path+ConfigReader().read('project')['img_path']
if __name__ == '__main__':
    print(project_path)
    print(report_path)
    print(logs_path)
    print(case_path)
    print(data_path)
    print(chromedriver_path)
    print(firefoxdriver_path)
    print(img_path)