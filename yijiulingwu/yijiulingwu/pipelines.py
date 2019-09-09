# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from yijiulingwu.items import YijiulingwuHaolaiwuItem,YijiulingwuHuayuItem,YijiulingwuMovieItem

class YijiulingwuPipeline(object):

    def __init__(self,MYSQLHOST,MYSQLPORT,MYSQL_DB,MYSQLUSER,MYSQLPWD):
        self.client = pymysql.Connect(host=MYSQLHOST,port=MYSQLPORT,database=MYSQL_DB,user=MYSQLUSER,password=MYSQLPWD,charset='utf8')
        self.cur = self.client.cursor()

    @classmethod
    def from_settings(cls,settings):
        MYSQLHOST = settings['MYSQLHOST']
        MYSQLPORT = settings['MYSQLPORT']
        MYSQL_DB = settings['MYSQL_DB']
        MYSQLUSER = settings['MYSQLUSER']
        MYSQLPWD = settings['MYSQLPWD']
        return cls(MYSQLHOST,MYSQLPORT,MYSQL_DB,MYSQLUSER,MYSQLPWD)


    def process_item(self, item, spider):

        if isinstance(item,YijiulingwuHuayuItem):
            sql,params = item.insert_sql()
            self.cur.execute(sql,params)
            self.client.commit()
            return item

        if isinstance(item,YijiulingwuHaolaiwuItem):
            sql,params = item.insert_sql()
            self.cur.execute(sql,params)
            self.client.commit()
            return item

        if isinstance(item,YijiulingwuMovieItem):
            sql,params = item.insert_sql()
            self.cur.execute(sql,params)
            self.client.commit()
            return item

    def close_spider(self,spider):
        self.cur.close()
        self.client.close()
