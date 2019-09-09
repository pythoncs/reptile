# @Time    : 18-7-29 下午5:46
# @Author  : cuishu
# @Site    : 
# @File    : index.py
# @Software: PyCharm
# -*- coding: utf-8 -*-
import scrapy
from csjobbole.items import CsjobboleIndexItem



class BaidulySpider(scrapy.Spider):
    name = 'index'
    allowed_domains = ['jobbole.com']
    start_urls = ['http://blog.jobbole.com/']

    def parse(self, response):
        item = CsjobboleIndexItem()
        # print(response.url)
        #热点关注左侧
        hotPayBlock = response.xpath('//div[@id="widgets-homepage-fullwidth"]//div[@class="container"][1]')
        #热点关注大图——左
        item['hotPayImg'] = hotPayBlock.xpath('./div[@class="grid-4 the-latest"]/div[@class="post-thumb"]/a/img/@src').extract_first('error')
        #热点关注标题-左
        item['hotPayTitle'] = hotPayBlock.xpath('./div[@class="grid-4 the-latest"]//div[@class="post-title"]/a/h4/text()').extract_first('')
        #热点关注时间
        item['hotPayTime'] = hotPayBlock.xpath('./div[@class="grid-4 the-latest"]//div[@class="post-meta"]/p/text()').extract_first().replace('·','').strip()
        #热点关注标签
        item['hotPayTags'] = hotPayBlock.xpath('./div[@class="grid-4 the-latest"]//div[@class="post-meta"]/p//a[1]/text()').extract_first('')
        #热点关注评论
        item['hotPayComment'] = hotPayBlock.xpath('./div[@class="grid-4 the-latest"]//div[@class="post-meta"]/p//a[2]/text()').extract_first()
        #热点关注描述
        item['hotPayDesc'] = ','.join(hotPayBlock.xpath('./div[@class="grid-4 the-latest"]//div[@class="post-excerpt"]//p[1]/text()').extract())

        #热点关注右侧
        hotPayR = hotPayBlock.xpath('.//div[@class="grid-4 floated-thumb"]')
        hotPayInfoR = []
        for h in hotPayR:
            #右侧关注图片
            hotPayImgR = h.xpath('./div[@class="post-thumb"]/a/img/@src').extract_first()
            # 热点关注标题-右
            hotPayTitleR = h.xpath('./div[@class="post-meta"]/p/a/text()').extract_first()
            #热点关注时间
            hotPayTimeR = h.xpath('./div[@class="post-meta"]/p/text()').extract()[1].replace('·','').strip()
            #热点关注标签
            hotPayTagsR = h.xpath('./div[@class="post-meta"]/p//a[2]/text()').extract_first()
            #热点关注评论
            hotPayCommentR = h.xpath('./div[@class="post-meta"]/p//a[3]/text()').extract_first('暂无')
            dict = {
                'hotPayImgR':hotPayImgR,
                'hotPayTitleR':hotPayTitleR,
                'hotPayTimeR':hotPayTimeR,
                'hotPayTagsR':hotPayTagsR,
                'hotPayCommentR':hotPayCommentR
            }
            hotPayInfoR.append(dict)
        item['hotPayInfoR'] = hotPayInfoR

        #最新文章
        newArticle = response.xpath('//div[@id="widgets-homepage-fullwidth"]//div[@class="container"][2]')
        naAll = newArticle.xpath('.//div[@class="grid-4"][1]//div[@class="floated-thumb"]')
        articleInfo = []
        for n in naAll:
            # 最新文章图片
            naImgSrc = n.xpath('./div[@class="post-thumb"]/a/img/@src').extract_first('')
            #最新文章标题
            naTitle = n.xpath('.//div[@class="post-meta"]/p//a[1]/text()').extract_first('')
            #最新文章时间
            naTime = n.xpath('.//div[@class="post-meta"]/p/text()').extract()[1].replace('·','').strip()
            #最新文章标签
            naTages = n.xpath('.//div[@class="post-meta"]/p//a[2]/text()').extract_first('')
            dict = {
                'naImgSrc':naImgSrc,
                'naTitle':naTitle,
                'naTime':naTime,
                'naTages':naTages
            }
            articleInfo.append(dict)
        item['articleInfo'] = articleInfo

        #热评文章
        hotarticleInfo = []
        hotarticle = newArticle.xpath('.//div[@class="grid-4"][2]//div[@class="floated-thumb"]')
        for h in hotarticle:
            # 热评文章图片
            haImg = h.xpath('./div[@class="post-thumb"]/a/img/@src').extract_first('')
            # 热评文章标题
            haTitle = h.xpath('.//div[@class="post-meta"]/p//a[1]/text()').extract_first('')
            # 热评文章时间
            haTime = h.xpath('.//div[@class="post-meta"]/p/text()').extract()[1].replace('·','').strip()
            # 热评文章标签
            haTages = h.xpath('.//div[@class="post-meta"]/p//a[2]/text()').extract_first('')
            # 热评文章评论
            hacomment = h.xpath('.//div[@class="post-meta"]/p//a[3]/text()').extract_first('')
            dict = {
                'haImg':haImg,
                'haTitle':haTitle,
                'haTime':haTime,
                'haTages':haTages,
                'hacomment':hacomment
            }
            hotarticleInfo.append(dict)
        item['hotarticleInfo'] = hotarticleInfo

        # web前端左侧
        webBlock = response.xpath('//div[@id="widgets-homepage-fullwidth"]//div[@class="container"][3]')
        # web前端大图——左
        item['webImg'] = webBlock.xpath('./div[@class="grid-4 the-latest"]/div[@class="post-thumb"]/a/img/@src').extract_first(
            'error')
        # web前端标题-左
        item['webTitle'] = webBlock.xpath(
            './div[@class="grid-4 the-latest"]//div[@class="post-title"]/a/h4/text()').extract_first('')
        # web前端时间
        item['webTime'] = webBlock.xpath(
            './div[@class="grid-4 the-latest"]//div[@class="post-meta"]/p/text()').extract_first().replace('·',
                                                                                                           '').strip()
        # web前端标签
        item['webTags'] = webBlock.xpath(
            './div[@class="grid-4 the-latest"]//div[@class="post-meta"]/p//a[1]/text()').extract_first('')
        # web前端描述
        item['webDesc'] = ','.join(webBlock.xpath('./div[@class="grid-4 the-latest"]//div[@class="post-excerpt"]//p[1]/text()').extract())

        # web前端右侧
        webR = webBlock.xpath('.//div[@class="grid-4 floated-thumb"]')
        webInfoR = []
        for h in webR:
            # 右侧关注图片
            webImgR = h.xpath('./div[@class="post-thumb"]/a/img/@src').extract_first()
            # web前端标题-右
            webTitleR = h.xpath('./div[@class="post-meta"]/p/a/text()').extract_first()
            # web前端时间
            webTimeR = h.xpath('./div[@class="post-meta"]/p/text()').extract()[1].replace('·', '').strip()
            # web前端标签
            webTagsR = h.xpath('./div[@class="post-meta"]/p//a[2]/text()').extract_first()

            dict = {
                'webImgR': webImgR,
                'webTitleR': webTitleR,
                'webTimeR': webTimeR,
                'webTagsR': webTagsR
            }
            webInfoR.append(dict)
        item['webInfoR'] = webInfoR

        # python开发左侧
        pythonDevelopBlock = response.xpath('//div[@id="widgets-homepage-fullwidth"]//div[@class="container"][4]')
        # python开发大图——左
        item['pythonDevelopImg'] = pythonDevelopBlock.xpath(
            './div[@class="grid-4 the-latest"]/div[@class="post-thumb"]/a/img/@src').extract_first('error')
        # python开发标题-左
        item['pythonDevelopTitle'] = pythonDevelopBlock.xpath(
            './div[@class="grid-4 the-latest"]//div[@class="post-title"]/a/h4/text()').extract_first('')
        # python开发时间
        item['pythonDevelopTime'] = pythonDevelopBlock.xpath(
            './div[@class="grid-4 the-latest"]//div[@class="post-meta"]/p/text()').extract_first().replace('·',
                                                                                                           '').strip()
        # python开发标签
        item['pythonDevelopTags'] = pythonDevelopBlock.xpath(
            './div[@class="grid-4 the-latest"]//div[@class="post-meta"]/p//a[1]/text()').extract_first('')
        # python开发描述
        item['pythonDevelopDesc'] = ','.join(pythonDevelopBlock.xpath(
            './div[@class="grid-4 the-latest"]//div[@class="post-excerpt"]//p[1]/text()').extract())
        # python开发评论
        item['pythonDevelopComment'] = pythonDevelopBlock.xpath(
            './div[@class="grid-4 the-latest"]//div[@class="post-meta"]/p//a[2]/text()').extract_first()


        # python开发右侧
        pythonDevelopR = pythonDevelopBlock.xpath('.//div[@class="grid-4 floated-thumb"]')
        pythonDevelopInfoR = []
        for h in pythonDevelopR:
            # 右侧开发图片
            pythonDevelopImgR = h.xpath('./div[@class="post-thumb"]/a/img/@src').extract_first()
            # python开发标题-右
            pythonDevelopTitleR = h.xpath('./div[@class="post-meta"]/p/a/text()').extract_first()
            # python开发时间
            pythonDevelopTimeR = h.xpath('./div[@class="post-meta"]/p/text()').extract()[1].replace('·', '').strip()
            # python开发标签
            pythonDevelopTagsR = h.xpath('./div[@class="post-meta"]/p//a[2]/text()').extract_first()

            dict = {
                'pythonDevelopImgR': pythonDevelopImgR,
                'pythonDevelopTitleR': pythonDevelopTitleR,
                'pythonDevelopTimeR': pythonDevelopTimeR,
                'pythonDevelopTagsR': pythonDevelopTagsR,
            }
            pythonDevelopInfoR.append(dict)
        item['pythonDevelopInfoR'] = pythonDevelopInfoR

        # 安卓开发左侧
        androidBlock = response.xpath('//div[@id="widgets-homepage-fullwidth"]//div[@class="container"][5]')
        # 安卓开发大图——左
        item['androidImg'] = androidBlock.xpath(
            './div[@class="grid-4 the-latest"]/div[@class="post-thumb"]/a/img/@src').extract_first('error')
        # 安卓开发标题-左
        item['androidTitle'] = androidBlock.xpath(
            './div[@class="grid-4 the-latest"]//div[@class="post-title"]/a/h4/text()').extract_first('')
        # 安卓开发时间
        item['androidTime'] = androidBlock.xpath(
            './div[@class="grid-4 the-latest"]//div[@class="post-meta"]/p/text()').extract_first().replace('·',
                                                                                                           '').strip()
        # 安卓开发标签
        item['androidTags'] = androidBlock.xpath(
            './div[@class="grid-4 the-latest"]//div[@class="post-meta"]/p//a[1]/text()').extract_first('')
        # 安卓开发评论
        item['androidComment'] = androidBlock.xpath(
            './div[@class="grid-4 the-latest"]//div[@class="post-meta"]/p//a[2]/text()').extract_first()
        # 安卓开发描述
        item['androidDesc'] = ','.join(
            androidBlock.xpath('./div[@class="grid-4 the-latest"]//div[@class="post-excerpt"]//p[1]/text()').extract())


        # 安卓开发右侧
        androidR = androidBlock.xpath('.//div[@class="grid-4 floated-thumb"]')
        androidInfoR = []
        for a in androidR:
            # 右侧关注图片
            androidImgR = a.xpath('./div[@class="post-thumb"]/a/img/@src').extract_first()
            # 安卓开发标题-右
            androidTitleR = a.xpath('./div[@class="post-meta"]/p/a/text()').extract_first()
            # 安卓开发时间
            androidTimeR = a.xpath('./div[@class="post-meta"]/p/text()').extract()[1].replace('·', '').strip()
            # 安卓开发标签
            androidTagsR = a.xpath('./div[@class="post-meta"]/p//a[2]/text()').extract_first()
            # 安卓开发评论
            androidCommentR = a.xpath('./div[@class="post-meta"]/p//a[3]/text()').extract_first('暂无')
            dict = {
                'androidImgR': androidImgR,
                'androidTitleR': androidTitleR,
                'androidTimeR': androidTimeR,
                'androidTagsR': androidTagsR,
                'androidCommentR': androidCommentR
            }
            androidInfoR.append(dict)
        item['androidInfoR'] = androidInfoR

        #ios开发左侧
        iosBlock = response.xpath('//div[@id="widgets-homepage-fullwidth"]//div[@class="container"][6]')
        #ios开发大图——左
        item['iosImg'] = iosBlock.xpath('./div[@class="grid-4 the-latest"]/div[@class="post-thumb"]/a/img/@src').extract_first('error')
        #ios开发标题-左
        item['iosTitle'] = iosBlock.xpath('./div[@class="grid-4 the-latest"]//div[@class="post-title"]/a/h4/text()').extract_first('')
        #ios开发时间
        item['iosTime'] = iosBlock.xpath('./div[@class="grid-4 the-latest"]//div[@class="post-meta"]/p/text()').extract_first().replace('·','').strip()
        #ios开发标签
        item['iosTags'] = iosBlock.xpath('./div[@class="grid-4 the-latest"]//div[@class="post-meta"]/p//a[1]/text()').extract_first('')
        #ios开发评论
        item['iosComment'] = iosBlock.xpath('./div[@class="grid-4 the-latest"]//div[@class="post-meta"]/p//a[2]/text()').extract_first()
        #ios开发描述
        item['iosDesc'] = ','.join(iosBlock.xpath('./div[@class="grid-4 the-latest"]//div[@class="post-excerpt"]//p[1]/text()').extract())


        #ios开发右侧
        iosR = iosBlock.xpath('.//div[@class="grid-4 floated-thumb"]')
        iosInfoR = []
        for i in iosR:
            #右侧关注图片
            iosImgR = i.xpath('./div[@class="post-thumb"]/a/img/@src').extract_first()
            # ios开发标题-右
            iosTitleR = i.xpath('./div[@class="post-meta"]/p/a/text()').extract_first()
            #ios开发时间
            iosTimeR = i.xpath('./div[@class="post-meta"]/p/text()').extract()[1].replace('·','').strip()
            #ios开发标签
            iosTagsR = i.xpath('./div[@class="post-met"]/p//a[2]/text()').extract_first()
            #ios开发评论
            iosCommentR = i.xpath('./div[@class="post-meta"]/p//a[3]/text()').extract_first('暂无')
            dict = {
                'iosImgR':iosImgR,
                'iosTitleR':iosTitleR,
                'iosTimeR':iosTimeR,
                'iosTagsR':iosTagsR,
                'iosCommentR':iosCommentR
            }
            iosInfoR.append(dict)
        item['iosInfoR'] = iosInfoR

        # 精选工具资源
        selectedTool = response.xpath(
            '//div[@id="widgets-homepage-fullwidth"]//div[@class="container"][7]')
        stAll = selectedTool.xpath('.//div[@class="grid-4"][1]//div[@class="floated-thumb"]')
        toolInfo = []
        for s in stAll:
            # 精选工具资源图片
            stImgSrc = s.xpath('./div[@class="post-thumb"]/a/img/@src').extract_first('')
            # 精选工具资源标题
            stTitle = s.xpath('.//div[@class="post-meta"]/p//a[1]/text()').extract_first('')
            # 精选工具资源评论数量
            stComment = s.xpath('.//div[@class="post-meta"]/p//a[3]/text()').extract_first('暂无')
            # 精选工具资源标签
            stTages = s.xpath('.//div[@class="post-meta"]/p//a[2]/text()').extract_first('')
            dict = {
                'stImgSrc': stImgSrc,
                'stTitle': stTitle,
                'stComment': stComment,
                'stTages': stTages
            }
            toolInfo.append(dict)
        item['toolInfo'] = toolInfo

        # 更多资源
        resourcesMoreInfo = []
        resourcesMore = selectedTool.xpath('.//div[@class="grid-4"][2]//div[@class="floated-thumb"]')
        for r in resourcesMore:
            # 更多资源图片
            haImg = r.xpath('./div[@class="post-thumb"]/a/img/@src').extract_first('')
            # 更多资源标题
            haTitle = r.xpath('.//div[@class="post-meta"]/p//a[1]/text()').extract_first('')
            # 更多资源标签
            haTages = r.xpath('.//div[@class="post-meta"]/p//a[2]/text()').extract_first('')
            # 更多资源评论
            hacomment = r.xpath('.//div[@class="post-meta"]/p//a[3]/text()').extract_first('暂无')
            dict = {
                'haImg': haImg,
                'haTitle': haTitle,
                'haTages': haTages,
                'hacomment': hacomment
            }
            resourcesMoreInfo.append(dict)
        item['resourcesMoreInfo'] = resourcesMoreInfo

        #小组话题
        teamTopic = response.xpath('//div[@id="sidebar"]//div[@class="container"][1]')
        #小组话题全部图片
        item['teamTopicImg'] = teamTopic.xpath('./div[@class="grid-4 floated-thumb"]//div[@class="author-thumb"]/a/img/@src').extract()
        #小组话题块
        teamTopicInfo = []
        teamTopicBlock = teamTopic.xpath('./div[@class="grid-4 floated-thumb"]//div[@class="post-meta"]')
        for t in teamTopicBlock:
            #小组话题标题
            teamTopicTitle = t.xpath('./p/a/text()').extract_first('')
            #小组话题作者
            teamTopicAuthor = t.xpath('./p//a[2]/text()').extract_first('')
            #小组话题发起数
            teamTopicspons = t.xpath('./p/text()').extract()[2].replace('•','').replace('\n','').replace(' ','')

            dict = {
                'teamTopicTitle':teamTopicTitle,
                'teamTopicAuthor':teamTopicAuthor,
                'teamTopicspons':teamTopicspons
            }
            teamTopicInfo.append(dict)
        item['teamTopicInfo'] = teamTopicInfo

        yield item