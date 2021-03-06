[toc]
注：此框架用例都是随便写的（毕竟实际项目的用例不能传到网上） 
 python + selenium + unittest + PageObject(PO 思想) + BeautifulReport(页面美观) or HTMLTestRunner_cn(使用方便)  + ddt(数据驱动) + log 日志 + 多浏览器支持（尚未实现，目前只有谷歌） + ini 文件读取+接口框架

# 1.框架注意点-使用前必看！
- 项目完全依靠参数化构建，见文件`/config/config.ini`
- `case` 中存放测试用例，测试用例需要以 test 打头,不是test开头是为了测试框架能否正确识别不要的用例，测试用例是随便写的
- `page`中存放 PO 对象，PO 对象中的测试点方法名需要以 test 开头，并且通过下划线加数字形式进行执行排序
- `config`中的谷歌驱动对应浏览器 86.0.424 版本的，对于其他版本的浏览器还需要自行更新驱动文件
- `/config/config.ini`中的键名参数不能大写，因为读取`.ini`的键名必以小写读出！
- 项目名一定要是`my_Framework`，其下目录名或文件名不要使用同名，当 ci/cd 集成时其上目录名要不要使用此名，因为代码中根据此名寻找路径，同名文件寻找路径会出现异常
- 建议用谷歌和火狐驱动，ie 似乎元素定位不一样
- 用例test_1用了po模型编写，其他用例没有使用，可以对比看出test_1用例很简洁

# 2.所需依赖
本人使用的是 python 3.6
```
本地库的版本已导出至requirements.txt中
使用pip install -r requirements.txt 安装即可

......

```

# 3.项目结构
```
my_Framework
        - case（测试用例脚本）
        - common（共用方法）
        - data（数据驱动）
        - locator（页面对应的元素定位）
        - page（页面类）
        - report（输出报告）
        - logs（log 日志报告）
        - img（测试截图）
        - jiekouauto（接口框架）
        - config（配置文件,driver驱动，driver不一定适合所有人的浏览器版本，最好根据自己版本进行下载）
        - case （测试用例）
        - README.md（项目介绍 md）
        - run_all.py（执行用例）
        - lianxi(存放了一些本人在学习中的记录，用框架时直接删掉就行，对整体框架没有任何影响)
        - venv(没啥用用时直接删掉即可)
```

# 4.可以拓展补充的地方
1. 目前只有BeautifulReport可以达到多线程报告聚合，但报告内容会有些乱，这个目前技术能力有限无法解决
2. 可添加读取 csv,xls,yml,txt 等多种文件的工具类方便读取数据（目前只有excal,ini,txt 文件读取）
3. 连接 oracle,sqlserver 等多种类型数据库的拓展实现
4. 可以考虑把HTMLTestRunner_cn进行二次开发，使其也可以多线程报告聚合
5. 可以考虑修改 config.ini 中的路径参数，不用每个路径后必添 "/"，也可智能识别路径，同时注意使用到这几个路径参数的工具类代码也需要修改
6. 目前除谷歌其他浏览器参数不全，如果有兴趣可以进行补全
7. 配置文件中可添加浏览器版本信息，目前是没有这项参数的。若添加了，之后再在 driver 装载器中补全代码即可
8. 目前好多代码都在run_all.py中，如果觉得乱可以单独整理出来
9. 可以用log把代码里的print都替换了，这样就会即保存到日志，又可以输出到控制台
10. 接口框架目前只有简单的雏形，还可以进行优化
11. 其他......



