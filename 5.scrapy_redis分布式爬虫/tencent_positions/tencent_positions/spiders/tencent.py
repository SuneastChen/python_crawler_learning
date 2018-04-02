# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from scrapy_redis.spiders import RedisCrawlSpider

from tencent_positions.items import TencentPositionsItem


class TencentSpider(RedisCrawlSpider):
    name = 'tencent'
    allowed_domains = ['tencent.com']

    def __init__(self,*arg,**kwargs):
        domains = kwargs.pop('domain','')
        self.allowed_domains = filter(None, domain.split(','))
        super().__init__(*arg,**kwargs)





    # start_urls = ['http://hr.tencent.com/position.php?amp;start=0&start=0#a']
    redis_key = 'tencent:start_urls'

    rules = (
        Rule(LinkExtractor(allow=r'start=\d+'), callback='parse_item', follow=True),
    )   # (正则匹配对象, 交给parse_item函数处理, 是否跟进链接)
    # 页面内容根据正则对象匹配到url的对象列表, 依次发送请求返回的response,交给parse_item函数处理,跟进链接直到匹配不到url了

    def parse_item(self, response):
        item = TencentPositionsItem()
        for tr in response.xpath('//tr[@class="even"] | //tr[@class="odd"]'):
            item['position'] = tr.xpath('./td[1]/a/text()').extract()[0]
            item['p_class'] = tr.xpath('./td[2]/text()').extract()[0]
            item['number'] = tr.xpath('./td[3]/text()').extract()[0]
            item['addr'] = tr.xpath('./td[4]/text()').extract()[0]
            item['publish_t'] = tr.xpath('./td[5]/text()').extract()[0]
            yield item
