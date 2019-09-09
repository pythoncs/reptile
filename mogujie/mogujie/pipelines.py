# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

class MogujiePipeline(object):

    def __init__(self,mongo_db,mongohost,mongoport):
        self.client = pymongo.MongoClient(mongohost,mongoport)
        self.db = self.client[mongo_db]
        self.col = self.db.csmgj

    @classmethod
    def from_settings(cls,settings):
        mongohost = settings['MONGODBHOST']
        mongoport = settings['MONGODBPORT']
        mongo_db = settings['MONGODB_DB']
        return cls(mongo_db,mongohost,mongoport)
        pass


    def process_item(self, item, spider):
        self.col.insert(dict(item))
        return item
