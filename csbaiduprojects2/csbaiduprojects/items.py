# -*- coding: utf-8 -*-
# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CsbaiduprojectsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 列表页url
    list_url = scrapy.Field()
    # 名称
    name = scrapy.Field()
    # 评分
    grade = scrapy.Field()
    # 描述
    describe = scrapy.Field()
    # 点评数量
    commentNum = scrapy.Field()
    # 最佳季节
    season = scrapy.Field()
    # 提示\建议
    suggest = scrapy.Field()
    # 图片详情跳转链接链接
    bimgUrl = scrapy.Field()
    # 图片详情链接
    bimgUrl_list = scrapy.Field()
    # 行程url
    journeyUrl = scrapy.Field()
    # 形成总数
    journeyNum = scrapy.Field()
    # 标题
    title = scrapy.Field()
    # 关键字
    keyword = scrapy.Field()
    # 路线1
    firstPath = scrapy.Field()
    # 路线2
    secondPath = scrapy.Field()
    # 评论区姓名、时间、评论内容、有用数、回复数）
    # 评论姓名
    commentName = scrapy.Field()
    # 评论时间
    commentTime = scrapy.Field()
    # 评论内容
    commentContent = scrapy.Field()
    # 评论有用数
    commentUsneNum = scrapy.Field()
    # 评论回复数
    commentReply = scrapy.Field()
    #路线列表
    journey_path_List = scrapy.Field()
    def insert_mongo(self):

        commentList = [{
            'name': self['commentName'],
            'publishtime': self['commentTime'],
            'replynums': self['commentReply'],
            'available': self['commentUsneNum'],
            'content': self['commentContent'],
        }]
        params = {
            '评论': self['grade'],
            '目的地名称': self['name'],
            '简介': self['describe'],
            '行程总数': self['journeyNum'],
            '路线列表': self['journey_path_List'],
            'url': self['journeyUrl'],
            '评论总数': self['commentNum'],
            '评论列表': commentList,
            'list_url': self['list_url'],
            '提示': self['suggest'],
            'bimgUrl': self['bimgUrl'],
            '美图页面完整链接': self['bimgUrl_list'],

        }
        print(params)
        return params
