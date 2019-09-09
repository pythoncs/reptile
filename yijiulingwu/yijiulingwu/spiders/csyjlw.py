# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from yijiulingwu.items import YijiulingwuHuayuItem



class CsyjlwSpider(CrawlSpider):
    name = 'csyjlw'
    allowed_domains = ['1905.com']
    start_urls = [
        'http://www.1905.com/film/filmnews/ch/',
    ]

    rules = (
        Rule(LinkExtractor(allow=r'http://www.1905.com/film/filmnews/ch/\d+.shtml',restrict_xpaths='//div[@id="paging"]'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        # print(response.url)
        item = YijiulingwuHuayuItem()
        li_list = response.xpath('//ul[@class="pic-event-over"]/li')
        for li in li_list:
            # 封面
            item['face'] = li.xpath('./a[@class="pic-url"]/img/@src').extract_first()
            # 时间
            item['date'] = li.xpath('.//div[@class="rel-other clear"]/span[@class="timer fl"]/text()').extract_first()
            # 标题
            item['title'] = li.xpath('.//div[@class="pic-pack-inner"]/h3/a/text()').extract_first()
            # 简介
            item['desc'] = li.xpath('.//div[@class="pic-pack-inner"]/p/text()').extract_first()
            # 相关明星
            item['starts'] = ','.join(li.xpath('.//div[@class="rel-other clear"]//a/text()').extract())
            # 详情链接
            item['detail_url'] = li.xpath('.//div[@class="pic-pack-inner"]/h3/a/@href').extract_first()
            yield item
