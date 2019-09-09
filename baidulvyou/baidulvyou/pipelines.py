# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
import os
import pymongo
import pymysql
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy.utils.project import get_project_settings
from baidulvyou.items import *
image_store = get_project_settings().get('IMAGES_STORE')
class JobboleImagePipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        image_url = item['imgSrc']
        yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        print('下载图片')

        path =[dict['path'] for status,dict in results if status]
        if not path:
            raise DropItem('图片路径不存在')
        else:
            os.rename(image_store+'/'+path[0],image_store+'/'+item['title']+'.jpg')
            item['image_path'] = image_store+'/'+item['title']+'jpg'

        return item

class BaidulvyouPipeline(object):

    def __init__(self,mongodbhost,mongodbport,mongodb_db,mysqlhost,mysqlport,mysqluser,mysqlpwd,mysqldb):
        self.client = pymongo.MongoClient(mongodbhost,mongodbport)
        self.db = self.client[mongodb_db]
        self.info = self.db.baiduly

        self.mysql_client = pymysql.Connect(mysqlhost,mysqlport,mysqluser,mysqlpwd,mysqldb,charset='utf8')
        self.cursor = self.mysql_client.cursor()

    @classmethod
    def from_settings(cls,settings):
        mongodbhost = settings['mongodbhost']
        mongodbport = settings['mongodbport']
        mongodb_db = settings['mongodb_db']

        mysqlhost = settings['mysqlhost']
        mysqlport = settings['mysqlport']
        mysqluser = settings['mysqluser']
        mysqlpwd = settings['mysqlpwd']
        mysqldb = settings['mysqldb']
        return cls(mongodbhost,mongodbport,mongodb_db,mysqlhost,mysqlport,mysqluser,mysqlpwd,mysqldb)

    def process_item(self, item, spider):
        if isinstance(item,BaidulvyouItem):
            params = item.insert_mongo()
            self.info.insert(params)
        if isinstance(item,BaidulvyouItem):
            sql,params = item.insert_mysql()
            self.cursor.execute(sql,params)
        return item

    def close_spider(self, spider):

        self.client.close()
        self.mysql_client.close()
        self.cursor.close()