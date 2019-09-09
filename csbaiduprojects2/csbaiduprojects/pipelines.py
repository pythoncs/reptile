
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from csbaiduprojects.items import *
# client = pymongo.MongoClient('localhost',27017)
# db = client.css
# coec = db.csss
import time


class CsbaiduprojectsPipeline(object):

    def __init__(self,MONGODBHOST,MONGODBPORT,MONGODB_DB):
        time.sleep(2)
        self.client = pymongo.MongoClient(MONGODBHOST,MONGODBPORT,connect=False)
        self.db = self.client[MONGODB_DB]
        self.info = self.db.cslvyou


    @classmethod
    def from_settings(cls,settings):
        MONGODBHOST = settings['MONGODBHOST']
        MONGODBPORT = settings['MONGODBPORT']
        MONGODB_DB = settings['MONGODB_DB']
        return cls(MONGODBHOST,MONGODBPORT,MONGODB_DB)

    def open_spider(self, spider):
        print('爬虫启动的时候会走一次')

    def process_item(self, item, spider):
        print('准备添加数据库')
        params = item.insert_mongo()
        self.info.insert(params)
        return item

    def close_spider(self,spider):
        print('结束')
        self.client.close()
