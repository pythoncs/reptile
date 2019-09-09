# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

class CsjobbolePipeline(object):

    def __init__(self,mongo_db,mongoport,mongohost):
        self.client = pymongo.MongoClient(mongohost,mongoport)
        self.db = self.client[mongo_db]

    @classmethod
    def from_settings(cls,settings):
        mongohost = settings['MONGOHOST']
        mongoport = settings['MONGOPORT']
        mongo_db = settings['MONGO_DB']
        return cls(mongo_db,mongoport,mongohost)

    def process_item(self, item, spider):

        self.db[item.get_collection_name()].insert(dict(item))

        return item

    def close_spider(self,spider):

        self.client.close()
