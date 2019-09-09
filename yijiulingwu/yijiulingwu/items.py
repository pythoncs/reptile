# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YijiulingwuHuayuItem(scrapy.Item):
    # 封面
    face = scrapy.Field()
    # 时间
    date = scrapy.Field()
    # 标题
    title = scrapy.Field()
    # 简介
    desc = scrapy.Field()
    # 相关明星
    starts = scrapy.Field()
    # 详情链接
    detail_url = scrapy.Field()

    def insert_sql(self):
        sql = 'insert into huayu values (0,%s,%s,%s,%s,%s,%s)'
        params = [self['face'],self['date'],self['title'],self['desc'],self['starts'],self['detail_url']]
        return sql,params

class YijiulingwuHaolaiwuItem(scrapy.Item):
    # 封面
    face = scrapy.Field()
    # 时间
    date = scrapy.Field()
    # 标题
    title = scrapy.Field()
    # 简介
    desc = scrapy.Field()
    # 相关明星
    starts = scrapy.Field()
    # 详情链接
    detail_url = scrapy.Field()

    def insert_sql(self):
        sql = 'insert into haolaiwu values (0,%s,%s,%s,%s,%s,%s)'
        params = [self['face'],self['date'],self['title'],self['desc'],self['starts'],self['detail_url']]
        return sql,params


class YijiulingwuMovieItem(scrapy.Item):

    # 封面
    face = scrapy.Field()
    # 标题
    title = scrapy.Field()
    # 完整的详情链接
    detail_url = scrapy.Field()
    # 时长
    time = scrapy.Field()

    def insert_sql(self):
        sql = 'insert into movie values (0,%s,%s,%s,%s)'
        params = [self['face'],self['title'],self['detail_url'],self['time']]
        return sql,params
