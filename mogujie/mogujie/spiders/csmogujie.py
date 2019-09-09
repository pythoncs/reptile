# -*- coding: utf-8 -*-
import scrapy
import json,re
from mogujie.items import MogujieItem
"""
找到分类接口 遍历出来每个分类下的接口 回调 加id page

response 获取相应数据


"""


class CsmogujieSpider(scrapy.Spider):
    name = 'csmogujie'
    allowed_domains = ['mogujie.com']
    start_urls = [
        'http://mce.mogucdn.com/jsonp/multiget/3?callback=jQuery21107327081886013955_1532602742248&pids=109499%2C109520%2C109731%2C109753%2C110549%2C109779%2C110548%2C110547%2C109757%2C109793%2C109795%2C110563%2C110546%2C110544&appPlat=pc&_=1532602742252']

    def parse(self, response):

        result = response.text
        string = result[41:-1]
        content = json.loads(string)
        dataList = content['data']
        for data in dataList:
            list = dataList[data]
            for data in list['list']:
                title = data['title']
                action = data['link']
                pattern = re.compile('.*?/book/(.*?)/(\d+).*?')
                keyWord = re.findall(pattern,action)
                # print(keyWord)
                for i in range(1,100):
                    url = 'http://list.mogujie.com/search?callback=jQuery21105976718573746134_1532594954788&_version=8193&ratio=3%3A4&cKey=15&page='+ str(i) +'&sort=pop&ad=0&fcid='+keyWord[0][1]+'&action='+keyWord[0][0]
                    yield scrapy.Request(url,callback=self.get_data,meta={'title':title})

    def get_data(self,response):
        item = MogujieItem()
        categoryName = response.meta['title']
        result = response.text
        string = result[45:-2]
        content = json.loads(string)
        dataList = content['result']['wall']['docs']
        list = []
        for data in dataList:
            title = data['title']
            price = data['price']
            orgPrice = data['orgPrice']
            likes = data['cfav']
            imgLink = data['link']
            dict = {
                categoryName:{
                    'title':title,
                    'price':price,
                    'orgPrice':orgPrice,
                    'likes':likes,
                    'imgLink':imgLink
                }
            }
            list.append(dict)
        item['category'] = list
        yield item


