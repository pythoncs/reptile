# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from csjobbole.items import CsjobboleItem,CsjobboleMessageItem
from scrapy_redis.spiders import RedisSpider

# class JobbolewSpider(RedisSpider):

class JobbolewSpider(CrawlSpider):
    name = 'jobbolew'
    allowed_domains = ['jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts/']
    # redis_key = 'JobbolewSpider:start_urls'
    rules = (
        Rule(LinkExtractor(allow=r'',restrict_xpaths='//ul[@id="main-nav-menu"]',deny='http://blog.jobbole.com/'), follow=True),
        Rule(LinkExtractor(allow=r'',restrict_xpaths='//div[@class="navigation margin-20"]'),callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = CsjobboleItem()
        # print(response.url)
        #当前分类
        item['category'] = ''.join(response.xpath('//div[@class="breadcrumb-wrapper"]/text()').extract()).replace('\n','').replace('>','')
        #列表下每一个li
        liList = response.xpath('//div[@id="archive"]//div[@class="post floated-thumb"]')
        # print(liList)
        for li in liList:
            #图片链接
            item['imgUrl'] = li.xpath('.//div[@class="post-thumb"]/a/img/@src').extract_first('暂无')
            #标题
            item['title'] = li.xpath('.//div[@class="post-meta"]/p/a/text()').extract_first('暂无')
            #时间
            item['time'] = li.xpath('.//div[@class="post-meta"]/p/text()').extract()[1].strip()
            #类型
            item['desc'] = li.xpath('.//div[@class="post-meta"]/p//a[2]/text()').extract_first('暂无')
            #描述
            item['describe'] = li.xpath('.//div[@class="post-meta"]/span[@class="excerpt"]/p/text()').extract_first('暂无')
            #阅读更多接口
            readMore = li.xpath('.//span[@class="read-more"]/a/@href').extract_first('暂无')

            yield scrapy.Request(readMore,callback=self.get_detail_data,meta={'item':item})

    def get_detail_data(self,response):
        item = CsjobboleItem()
        # print(response.url)
        #原文出处
        item['provenance'] = response.xpath('//div[@class="entry"]//div[@class="copyright-area"]/a/text()').extract_first('暂无')
        #内容
        item['content'] = ','.join(response.css('div.entry p::text').extract()).replace('\n','')
        #点赞量
        item['likes'] = response.xpath('//div[@class="post-adds"]/span[@data-post-id="114241"]/h10/text()').extract_first('暂无')

        #热门文章_周
        item['hotArticleW'] = ','.join(response.xpath('//div[@id="tab1"]//div[@class="post-meta  no-thumb"]//p/a/text()').extract())
        #热门文章_月
        item['hotArticleM'] = ','.join(response.xpath('//div[@id="tab2"]//div[@class="post-meta  no-thumb"]//p/a/text()').extract())
        #热门标签
        item['hotTags'] = ','.join(response.xpath('//div[@id="tab3"]/p//a/text()').extract())

        # 业界热点资讯 图片链接
        item['consult'] = response.xpath('//div[@class="grid-4 floated-thumb"]//div[@class="post-thumb"]/a/img/@src').extract()
        # print(consult)

        #咨询详情信息
        consultInfo = response.xpath('//div[@class="grid-4 floated-thumb"]//div[@class="post-meta"]')
        consultInfoList = []
        for info in consultInfo:
            #标题
            consultTitle = info.xpath('./p/a/text()').extract_first()
            #时间
            consultTime = info.xpath('./p/text()').extract()[1].strip().replace('·','')
            #点赞数
            consultLikes = info.xpath('./p/text()').extract()[2].strip().replace('·','')
            #评论
            consultComment = info.xpath('./p//a[2]/text()').extract_first('暂无')
            dict = {
                'consultTitle':consultTitle,
                'consultTime':consultTime,
                'consultLikes':consultLikes,
                'consultComment':consultComment
            }
            consultInfoList.append(dict)
        item['consultInfo'] = consultInfoList
        #咨询 更多链接
        # consultMoreUrl = response.xpath('//div[@id="sidebar"]/h3/span/a/@href').extract_first('')
        # http: // top.jobbole.com / category / news /
        consultMoreUrl = 'http://top.jobbole.com/category/news/'
        yield scrapy.Request(consultMoreUrl,callback=self.get_consult_detail)
        yield item


    def get_consult_detail(self,response):
        item = CsjobboleMessageItem()
        # print(response.url)
        #咨询详情列表
        consultlt = response.xpath('//div[@class="left-content"]/ul[@class="list-posts"]//li[@class="media"]')
        for lt in consultlt:
            #顶起
            item['jackUpNum'] = lt.xpath('./a/span/text()').extract_first('')
            #资讯标题
            item['messageTitle'] = lt.xpath('./div[@class="media-body"]/h3/a/text()').extract_first('')
            #时间
            item['messageTime'] = lt.xpath('./div[@class="media-body"]/p/span/text()').extract_first('')
            #评论量与标签
            messageCommentNumTags = ','.join(lt.css('div.media-body p span a::text').extract())
            if len(messageCommentNumTags) == 0:
                item['messageCommentNumTags'] = '暂无'
            else:
                item['messageCommentNumTags'] = messageCommentNumTags
            # print(item['messageCommentNumTags'])
        #下一页
        nextPage = response.xpath('//li[@id="pagination-next-page"]/a/@href').extract_first('')
        if len(nextPage) > 0:
            yield scrapy.Request(nextPage,callback=self.get_consult_detail,meta={'item':item})
        else:
            print('没有下一页了')

        yield item
