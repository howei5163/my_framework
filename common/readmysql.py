#coding=utf-8
import pymysql
from common.readConfig import ConfigReader
'''封装一些MySQL的操作方法,一些方法可根据项目进行修改'''
class Mysql:
    #   获取连接方法
    def get_db_conn(self):
        conn = pymysql.connect(host=ConfigReader().read("mysql")["host"],
                               port=ConfigReader().read("mysql")["port"],
                               user=ConfigReader().read("mysql")["user"],
                               passwd=ConfigReader().read("mysql")["passwd"],
                               db=ConfigReader().read("mysql")["db"],
                               charset=ConfigReader().read("mysql")["charset"])  # 如果查询有中文，需要指定测试集编码

        return conn
    # 封装数据库查询操作
    def select_sql(self,sql):
        conn = self.get_db_conn()  # 获取连接
        cur = conn.cursor()  # 建立游标
        cur.execute(sql)  # 执行sql
        result = cur.fetchall()  # 获取所有查询结果
        cur.close()  # 关闭游标
        conn.close()  # 关闭连接
        return result  # 返回结果

    # 封装更改数据库操作,每次更改数据库后都要调用
    def change_sql(self,sql):
        conn = self.get_db_conn()  # 获取连接
        cur = conn.cursor()  # 建立游标
        try:
            cur.execute(sql)  # 执行sql
            conn.commit()  # 提交更改
        except Exception as e:
            conn.rollback()  # 回滚
        finally:
            cur.close()  # 关闭游标
            conn.close()  # 关闭连接

    def close_mysql(self):
        conn=self.get_db_conn()
        cur=conn.cursor()
        cur.close()
        conn.close()

    # 封装常用数据库操作,查询名字
    def select_user(self,table,user):
        # 注意sql中''号嵌套的问题
        sql = "select * from {} where name = '{}'".format(table,user)
        result = self.select_sql(sql)
        return True if result else False


    def add_user(self,table,name, password):
        sql = "insert into {} (name, passwd) values ('{}','{}')".format(table,name, password)
        self.change_sql(sql)


    def del_user(self,table,name):
        sql = "delete from {} where name='{}'".format(table,name)
        self.change_sql(sql)