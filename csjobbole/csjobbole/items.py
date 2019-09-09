# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CsjobboleItem(scrapy.Item):
    #分类
    category = scrapy.Field()
    #图片
    imgUrl = scrapy.Field()
    # 标题
    title = scrapy.Field()
    # 时间
    time = scrapy.Field()
    # 类型
    desc = scrapy.Field()
    # 描述
    describe = scrapy.Field()

    # 原文出处
    provenance = scrapy.Field()
    # 内容
    content = scrapy.Field()
    # 点赞量
    likes = scrapy.Field()
    # 热门文章_周
    hotArticleW = scrapy.Field()
    # 热门文章_月
    hotArticleM = scrapy.Field()
    # 热门标签
    hotTags = scrapy.Field()
    # 业界热点资讯 图片链接
    consult = scrapy.Field()
    # 咨询详情信息
    consultInfo = scrapy.Field()
    def get_collection_name(self):
        return 'detail'

class CsjobboleMessageItem(scrapy.Item):

    # 顶起
    jackUpNum = scrapy.Field()
    # 资讯标题
    messageTitle = scrapy.Field()
    # 时间
    messageTime = scrapy.Field()
    # 评论量与标签
    messageCommentNumTags = scrapy.Field()

    def get_collection_name(self):
        return 'message'


class CsjobboleIndexItem(scrapy.Item):
    # 热点关注大图——左
    hotPayImg = scrapy.Field()
    # 热点关注标题-左
    hotPayTitle = scrapy.Field()
    # 热点关注时间
    hotPayTime = scrapy.Field()
    # 热点关注标签
    hotPayTags = scrapy.Field()
    # 热点关注评论
    hotPayComment = scrapy.Field()
    # 热点关注描述
    hotPayDesc = scrapy.Field()

    # 热点关注右侧
    hotPayInfoR = scrapy.Field()
    # 最新文章
    articleInfo = scrapy.Field()
    # 热评文章标题
    hotarticleInfo = scrapy.Field()


    # web前端大图——左
    webImg = scrapy.Field()
    # web前端标题-左
    webTitle = scrapy.Field()
    # web前端时间
    webTime = scrapy.Field()
    # web前端标签
    webTags = scrapy.Field()
    # web前端描述
    webDesc = scrapy.Field()
    #web前端
    webInfoR = scrapy.Field()

    # python开发大图——左
    pythonDevelopImg = scrapy.Field()
    # python开发标题-左
    pythonDevelopTitle = scrapy.Field()
    # python开发时间
    pythonDevelopTime = scrapy.Field()
    # python开发标签
    pythonDevelopTags = scrapy.Field()
    # python开发描述
    pythonDevelopDesc = scrapy.Field()
    # python开发评论
    pythonDevelopComment = scrapy.Field()
    #python开发
    pythonDevelopInfoR = scrapy.Field()

    # 安卓开发大图——左
    androidImg = scrapy.Field()
    # 安卓开发标题-左
    androidTitle = scrapy.Field()
    # 安卓开发时间
    androidTime = scrapy.Field()
    # 安卓开发标签
    androidTags = scrapy.Field()
    # 安卓开发评论
    androidComment = scrapy.Field()
    # 安卓开发描述
    androidDesc = scrapy.Field()
    #安卓开发
    androidInfoR = scrapy.Field()

    # ios开发大图——左
    iosImg = scrapy.Field()
    # ios开发标题-左
    iosTitle = scrapy.Field()
    # ios开发时间
    iosTime = scrapy.Field()
    # ios开发标签
    iosTags = scrapy.Field()
    # ios开发评论
    iosComment = scrapy.Field()
    # ios开发描述
    iosDesc = scrapy.Field()

    #ios开发
    iosInfoR = scrapy.Field()
    #精选工具资源
    toolInfo = scrapy.Field()
    #更多资源
    resourcesMoreInfo = scrapy.Field()

    # 小组话题全部图片
    teamTopicImg = scrapy.Field()
    #小组话题
    teamTopicInfo = scrapy.Field()

    def get_collection_name(self):
        return 'index'
