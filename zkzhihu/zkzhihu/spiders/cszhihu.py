# -*- coding: utf-8 -*-
import scrapy
import requests
import json, re
from zkzhihu.items import ZkzhihuQuestionItem, ZkzhihuAnswersItem, ZkzhihuUserItem


class CszhihuSpider(scrapy.Spider):
    name = 'cszhihu'
    allowed_domains = ['zhihu.com']

    start_urls = [
        'https://www.zhihu.com/api/v3/feed/topstory?action_feed=True&limit=7&session_token=0c3140e26767bca09e2b6353d57d2f8e&action=down&after_id=' + str(
            i) + '&desktop=true' for i in range(6, 30, 7)]

    def start_requests(self):
        item = ZkzhihuQuestionItem()
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
            'Referer': 'https://www.zhihu.com/',
            'cookie': '__DAYU_PP=vAfrqi6AbJB22Nybu7AZ37ff9fa2828d; _zap=1040198d-67e9-41b2-b989-586fac52cc18; _xsrf=lkWlMjdHSE1O2L3P6cN3dm1QWLbWtOtt; q_c1=af8ac78b947d4a409291de1092074427|1534936800000|1521856045000; d_c0="ACCnY-JqGA6PThFaxqYPyyGx9zhPC1RJ8fc=|1534936800"; capsion_ticket="2|1:0|10:1535014744|14:capsion_ticket|44:YzZjZWZjMzUwNjRjNGFiM2JlN2Q3OWQ0Yzk2M2U5MTA=|0da9cd29dcb6b8bca93dd8ee52f1390a38e53478f1d666869669bc1abf2dffbf"; z_c0="2|1:0|10:1535014794|4:z_c0|92:Mi4xSUlyR0N3QUFBQUFBSUtkajRtb1lEaVlBQUFCZ0FsVk5pc1ZyWEFDdlhQNXB4V1JrMnc3VFRFVDhaUEU1TFU4Y3BR|c0d468f11bf9441ace2bf7bd54474a42b4544db3b56fb24abe6afcefb590d7d1"; tgw_l7_route=56f3b730f2eb8b75242a8095a22206f8',
        }
        for url in self.start_urls:
            response = requests.get(url, headers=headers).text
            result = json.loads(response)

            try:
                for data in result['data']:
                # data = result['data'][0]
                    # 问题id
                    try:
                        item['question_id'] = data['target']['question']['id']
                    except:
                        item['question_id'] = '无'
                    # 问题标签
                    item['tags'] = '/'.join([i['reason_text'] for i in data['uninterest_reasons']])
                    # 标题
                    item['title'] = data['target']['question']['title']
                    # 简介
                    item['excerpt_new'] = data['target']['excerpt_new']
                    # 关注数量
                    item['follower_count'] = data['target']['question']['follower_count']
                    # 回答数
                    item['answer_count'] = data['target']['question']['answer_count']
                    # 问题作者id
                    item['author_id'] = data['target']['question']['author']['id']

                    Answer_url = 'https://www.zhihu.com/api/v4/questions/' + str(item[
                                                                                     'question_id']) + '/answers?include=data%5B*%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%3Bdata%5B*%5D.mark_infos%5B*%5D.url%3Bdata%5B*%5D.author.follower_count%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=&limit=3&sort_by=default'

                    # yield item
                    yield scrapy.Request(Answer_url, headers=headers, callback=self.parse_detail,
                                     meta={'item': item})

                # print(item)
            except Exception as error:
                print(error)

    def parse_detail(self, response):
        # print(response.url)
        # print(response.status)
        item = ZkzhihuAnswersItem()
        detail_response = response.text
        result = json.loads(detail_response)
        # print(result['data'][0]['author']['name'])
        question_item = response.meta['item']
        try:
            for data in result['data']:
                # 用户id
                item['author_id'] = data['author']['id']
                # 答案id
                item['anwser_id'] = data['id']
                # 答案的内容
                matching = re.compile('([\u4e00-\u9fa5]+)')
                content = re.findall(matching, data['content'])
                item['content'] = str(content).replace('\n','')
                # 问题的id
                item['question_id'] = data['question']['id']
                # 赞同数
                item['voteup_count'] = data['voteup_count']
                # 评论数
                item['comment_count'] = data['comment_count']

                User_url = 'https://api.zhihu.com/people/' + str(item['author_id'])
                yield scrapy.Request(User_url, callback=self.parse_userInfo, dont_filter=True,
                                     meta={'question_item': question_item, 'answer_item': item})
                # print(item)
        except Exception as error:
            print(error)

    def parse_userInfo(self, response):
        # print(response.status)
        result = json.loads(response.text)
        question_item = response.meta['question_item']
        answer_item = response.meta['answer_item']
        item = ZkzhihuUserItem()
        try:
            # 用户id
            item['author_id'] = result['id']
            # 用户昵称
            item['author_name'] = result['name']
            # 获得赞同数(成就)
            item['voteup_count'] = result['voteup_count']
            # 教育经历
            try:
                item['education'] = result['education'][0]['name']
            except:
                item['education'] = '无'
            # 现居住地址
            try:
                item['location'] = result['location'][0]['name']
            except:
                item['location'] = '无'
            # 所在行业
            item['business'] = result['business']['name']
            # 回答数
            item['answer_count'] = result['answer_count']
            # 提问数
            item['question_count'] = result['question_count']
            # 文章数
            item['articles_count'] = result['articles_count']
            # 个人简介
            item['author_profile'] = result['description'].replace('\n', '')

            yield question_item
            yield answer_item
            yield item
        except Exception as error:
            print('error')
