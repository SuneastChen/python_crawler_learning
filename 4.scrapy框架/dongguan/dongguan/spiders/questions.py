# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class QuestionsSpider(CrawlSpider):
    name = 'questions'
    allowed_domains = ['sun0769.com']
    start_urls = ['http://wz.sun0769.com/html/top/report.shtml']

    rules = (
        #提取页数的url,若没有callback函数,默认follow为true,只会提取url,请求,返回的响应不作处理
        Rule(LinkExtractor(allow=r'/question/report\?page=\d+?'),follow=True), 
        #提取详情的url,请求,交给parse_item处理,处理完后,不需要再根据规则提取url了
        Rule(LinkExtractor(allow=r'/question/201711/'), callback='parse_item', follow=False), 
    )

    def parse_item(self, response):
        i = {}
        i['title'] = response.xpath('//div[@class="pagecenter p3"]//strong[@class="tgray14"]/text()').extract()[0].split()[0]
        i['number'] = response.xpath('//div[@class="pagecenter p3"]//strong[@class="tgray14"]/text()').extract()[0].split()[-1].split(':')[-1]
        i['content'] = response.xpath('string(//div[@class="c1 text14_2"])').extract()[0].split()
        return i
