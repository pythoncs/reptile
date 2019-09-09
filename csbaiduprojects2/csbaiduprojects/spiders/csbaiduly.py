# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from csbaiduprojects.items import *
from scrapy_redis.spiders import RedisCrawlSpider

item = CsbaiduprojectsItem()
imageList = []


class CsbaidulySpider(RedisCrawlSpider):
    name = 'csbaiduly'
    allowed_domains = ['lvyou.baidu.com']
    # start_urls = ['https://lvyou.baidu.com/scene/t-all_s-all_a-all_l-all?rn=12&pn=0']
    redis_key = 'baiduSpider:start_urls'
    # ----------------------------------------------------------------------------------------------------写完改成True
    rules = (
        Rule(LinkExtractor(allow=r'', restrict_xpaths='//span[@class="pagelist"]'), callback='parse_item',
             follow=False),
        Rule(LinkExtractor(allow=r'/zhongguo/', restrict_xpaths='//div[@class="img-wrap"]'), callback='lyDetail',
             follow=False),

    )

    def parse_item(self, response):
        # 列表页url
        item['list_url'] = response.url
        # yield item

    def lyDetail(self, response):
        # item = CsbaiduprojectsItem()
        # 名称
        item['name'] = response.xpath('//span[@class="main-name clearfix"]/a/text()').extract_first('')
        block = response.xpath('//div[@class="main-info-wrap"]')
        # 评分
        item['grade'] = block.xpath('./div[@class="main-score"]/text()').extract()[1].replace('\n', '')
        # 描述
        item['describe'] = block.xpath('.//div[@class="main-desc"]/p[@class="main-desc-p"]/text()').extract()[
            0].replace('\n', '')
        # 点评数量
        item['commentNum'] = block.xpath('.//div[@class="main-score"]/a/text()').extract_first('')
        # 最佳季节
        item['season'] = block.xpath('.//div[@class="main-intro"]/span[1]/span/text()').extract_first('').replace('\n',
                                                                                                                  '')
        # 提示\建议
        item['suggest'] = block.xpath('.//div[@class="main-intro"]/span[2]/span/text()').extract_first('')
        # 图片详情跳转链接链接
        item['bimgUrl'] = 'https://lvyou.baidu.com' + response.xpath(
            '//a[@class="pic-more more-pic-tip clearfix"]/@href').extract_first('')
        # 行程url
        item['journeyUrl'] = 'https://lvyou.baidu.com' + response.xpath(
            '//a[@id="J_line-more-href"]/@href').extract_first('')
        journey = response.xpath(
            '//a[@id="J_line-more-href"]/text()').extract()
        a = response.xpath('//a[@id="J_line-more-href"]/span/text()').extract()[0]
        item['journeyNum'] = journey[0] + a + journey[1]
        commentall = response.xpath('//div[@class="main-remark-wrap"]')
        # print(commentall)
        # 评论姓名
        item['commentName'] = commentall.xpath('.//div[6]//div[@class="ri-avatar-wrap"]/a[2]/text()').extract()[0]
        # 评论时间
        item['commentTime'] = commentall.xpath('.//div[6]//div[@class="ri-time"]/text()').extract_first('').replace(
            '\n', '')
        # 评论内容
        item['commentContent'] = commentall.xpath('.//div[6]//div[@class="ri-remarktxt"]/text()').extract_first(
            '').replace('\n', '')
        # 评论有用数
        item['commentUsneNum'] = \
        commentall.xpath('.//div[6]//a[@class="ri-dig ri-dig-available"]/span/text()').extract()[0]
        # 评论回复数
        item['commentReply'] = commentall.xpath('.//div[6]//a[@class="ri-comment"]/span/text()').extract()[0]

        # print($item)
        # yield item
        yield scrapy.Request(item['bimgUrl'], callback=self.beautiful_image)
        yield scrapy.Request(item['journeyUrl'], callback=self.journey)

    def beautiful_image(self, response):
        try:
            # 图片详情链接
            image_list = response.xpath('//ul[@class="photo-list nslog-area"]//img/@src').extract()
            for i in image_list:
                imageList.append({'image': i})
            item['bimgUrl_list'] = imageList
            # print(item['bimgUrl_list'])
            # 下一页
            next_page = response.xpath('//a[@class="photo-frame nslog"]/@href').extract_first('')
            if len(next_page) > 0:
                next_page_url = 'https://lvyou.baidu.com/zhongguo' + next_page
                yield scrapy.Request(next_page_url, callback=self.beautiful_image)
        except Exception as error:
            print(error)

    def journey(self, response):
        # item = CsbaiduprojectsItem()
        journey_list = []
        block = response.xpath('//ul[@pb-show-id="lv4873954"]//li')
        for li in block:
            # 标题
            title = li.xpath('.//div[@class="plan-title-box"]/a/text()').extract_first('')
            # 关键字
            keyword = li.xpath('.//div[@class="key-word"]//span/text()').extract()
            if len(keyword) > 0:
                item['keyword'] = keyword
            else:
                item['keyword'] = '无'
            # 路线1
            firstPath = '--->'.join(li.xpath('.//div[@class="day-dest"][1]//span/text()').extract())
            # 路线2
            secondPath = '--->'.join(li.xpath('.//div[@class="day-dest"][2]//span/text()').extract())
            dict = {
                'title': title,
                'keyword': keyword,
                'firstPath': firstPath,
                'secondPath': secondPath
            }
            journey_list.append(dict)
        item['journey_path_List'] = journey_list


