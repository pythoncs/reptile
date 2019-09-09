# @Time    : 18-9-3 下午3:44
# @Author  : cuishu
# @Site    : 
# @File    : movies.py
# @Software: PyCharm
# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from yijiulingwu.items import YijiulingwuMovieItem



class CsyjlwSpider(CrawlSpider):
    name = 'movies'
    allowed_domains = ['1905.com']
    start_urls = [
        'http://www.1905.com/video/search/lst/t158e1d0o2.html',
    ]

    rules = (
        Rule(LinkExtractor(allow=r'http://www.1905.com/video/search/lst/t158e1d0o2p\d+.html',restrict_xpaths='//div[@class="listComponent pagination"]'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        # print(response.url)
        item = YijiulingwuMovieItem()
        li_list = response.xpath('//ul[@class="listCon clearfix clearfix_smile"]/li')
        for li in li_list:
            # 封面
            item['face'] = li.xpath('./div[@class="pic-pack-outer"]/a/img/@src').extract_first()
            # 标题
            item['title'] = li.xpath('.//h3/a/text()').extract_first()
            # 完整的详情链接
            item['detail_url'] = li.xpath('.//h3/a/@href').extract_first()
            # 时长
            item['time'] = li.xpath('.//div[@class="pic-pack-outer"]/a//span[@class="txt"]/span[@class="inner_txt"]/text()').extract_first()
            yield item