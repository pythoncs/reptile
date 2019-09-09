# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from zkzhihu.items import ZkzhihuUserItem,ZkzhihuAnswersItem,ZkzhihuQuestionItem

class ZkzhihuPipeline(object):

    def __init__(self,mysqlhost, mysqlport, mysql_db, mysqluser, mysqlpwd):
        self.client = pymysql.Connect(host=mysqlhost,port=mysqlport,user=mysqluser,password=mysqlpwd,database=mysql_db,charset='utf8')
        self.cur = self.client.cursor()

    @classmethod
    def from_settings(cls,settings):
        mysqlhost = settings['MYSQLHOST']
        mysqlport = settings['MYSQLPORT']
        mysql_db = settings['MYSQL_DB']
        mysqluser = settings['MYSQLUSER']
        mysqlpwd = settings['MYSQLPWD']
        return cls(mysqlhost, mysqlport, mysql_db, mysqluser, mysqlpwd)

    def process_item(self, item, spider):
        # 问题
        if isinstance(item,ZkzhihuQuestionItem):
            sql,params = item.insert_sql()
            self.cur.execute(sql,params)
            self.client.commit()
            return item
        # 回答
        if isinstance(item,ZkzhihuAnswersItem):
            sql,params = item.insert_sql()
            self.cur.execute(sql,params)
            self.client.commit()
            return item
        # 用户
        if isinstance(item,ZkzhihuUserItem):
            sql,params = item.insert_sql()
            self.cur.execute(sql,params)
            self.client.commit()
            return item

    def close_spider(self,spider):
        self.cur.close()
        self.client.close()