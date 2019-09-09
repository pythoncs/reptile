# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZkzhihuQuestionItem(scrapy.Item):
    # 问题ID
    question_id = scrapy.Field()
    # 问题标签
    tags = scrapy.Field()
    # 标题
    title = scrapy.Field()
    # 简介
    excerpt_new = scrapy.Field()
    # 关注数量
    follower_count = scrapy.Field()
    # 回答数
    answer_count = scrapy.Field()
    # 问题作者id
    author_id = scrapy.Field()

    def insert_sql(self):
        sql = 'INSERT INTO questioninfo VALUES (0,%s,%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE author_id = %s'
        params = [self['question_id'],self['tags'],self['title'],self['excerpt_new'],self['follower_count'],self['answer_count'],self['author_id'],self['author_id']]
        return sql,params
class ZkzhihuUserItem(scrapy.Item):
    # 用户id
    author_id = scrapy.Field()
    # 用户昵称
    author_name = scrapy.Field()
    # 获得赞同数(成就)
    voteup_count = scrapy.Field()
    # 教育经历
    education = scrapy.Field()
    # 现居住地址
    location = scrapy.Field()
    # 所在行业
    business = scrapy.Field()
    # 回答数
    answer_count = scrapy.Field()
    # 提问数
    question_count = scrapy.Field()
    # 文章数
    articles_count = scrapy.Field()
    # 个人简介
    author_profile = scrapy.Field()

    def insert_sql(self):
        sql = 'INSERT INTO userinfo VALUES (0,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        params = [self['author_id'], self['author_name'], self['voteup_count'], self['education'], self['location'],
                  self['business'], self['answer_count'], self['question_count'], self['articles_count'], self['author_profile']]
        return sql, params

class ZkzhihuAnswersItem(scrapy.Item):
    # 答案id
    anwser_id = scrapy.Field()
    # 答案的内容
    content = scrapy.Field()
    # 答案作者id
    author_id = scrapy.Field()
    # 问题的id
    question_id = scrapy.Field()
    # 赞同数
    voteup_count = scrapy.Field()
    # 评论数
    comment_count = scrapy.Field()

    def insert_sql(self):
        sql = 'INSERT INTO answerinfo VALUES (0,%s,%s,%s,%s,%s,%s)'
        params = [self['anwser_id'], self['content'], self['author_id'], self['question_id'], self['voteup_count'],
                  self['comment_count']]
        return sql, params