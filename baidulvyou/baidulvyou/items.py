# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BaidulvyouItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #图片src
    imgSrc = scrapy.Field()
    #新建路径
    imgPath = scrapy.Field()
    #标题
    title = scrapy.Field()
    #作者头像src
    authorImg = scrapy.Field()
    #作者
    author = scrapy.Field()
    #点赞
    like = scrapy.Field()
    #内容
    content = scrapy.Field()
    #浏览量
    views = scrapy.Field()
    #评论数量
    commentNum = scrapy.Field()
    #评论
    comment = scrapy.Field()

    def insert_mongo(self):
        params = {
            'imgsrc':self.imgSrc,
            'imgpath':self.imgPath,
            'title':self.title,
            'authorimag':self.authorImg,
            'author':self.author,
            'like':self.like,
            'content':self.content,
            'views':self.views,
            'commentnum':self.commentNum,
            'comment':self.comment,

        }
        return params
    def insert_mysql(self):
        sql = 'inset into baiduly values (0,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        params = [self.imgSrc,self.imgPath,self.title,self.authorImg,self.author,self.like,self.content,self.views,self.commentNum,self.comment]
        return sql,params
        pass
