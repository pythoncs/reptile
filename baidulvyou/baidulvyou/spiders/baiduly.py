# -*- coding: utf-8 -*-
import scrapy
import json
from baidulvyou.items import *

class BaidulySpider(scrapy.Spider):
    name = 'baiduly'
    allowed_domains = ['baidu.com']
    start_urls = ['https://lvyou.baidu.com/search/ajax/searchnotes?format=ajax&type=0&pn='+str(i) for i in range (5,151)]

    def parse(self, response):
        item = BaidulvyouItem()
        # print(response.status)
        html = response.text
        html = json.loads(html)

        data_dict = html['data']
        notes_list = data_dict['notes_list']

        for dict in notes_list:

            #标题
            item['title'] = dict['title']
            #图片
            item['imgSrc'] = dict['avatar_small']
            # 作者头像src
            item['authorImg'] = dict['last_post']['avatar_small']
            # 作者
            item['author'] = dict['user_nickname']
            # 点赞
            item['like'] = dict['recommend_count']
            # 内容
            item['content'] = dict['content'].replace('&nbsp;\\u3000','')
            # 浏览量
            item['views'] = dict['view_count']
            # 评论数量
            item['commentNum'] = dict['common_posts_count']
            # 评论
            item['comment'] = dict['last_post']['content'].replace('\n<p><br /></p>','')
            print(item)
            yield item


        pass