# -*- coding: utf-8 -*-
import scrapy
from collectips.items import CollectipsItem
import re

class XiciSpider(scrapy.Spider):
    name = 'xici'
    allowed_domains = ['xicidaili.com']
    start_urls = ['http://www.xicidaili.com/']

    def start_requests(self):
        reqs = []
        for i in range(1, 2):
            req = scrapy.Request('http://www.xicidaili.com/nn/%s' % i)
            reqs.append(req)

        return reqs

    def parse(self, response):
        ip_table = response.xpath('//table[@id="ip_list"]')  # 得到xpath对象列表,即使只有一个
        trs_list = ip_table[0].xpath('tr')

        for ip in trs_list[1:]:
            pre_item = CollectipsItem()
            pre_item['IP'] = ip.xpath('td[2]/text()')[0].extract()
            pre_item['PORT'] = ip.xpath('td[3]/text()').extract_first()
            pre_item['POSITION'] = ip.xpath('string(td[4])').extract_first().strip()
            pre_item['TYPE'] = ip.xpath('td[6]/text()')[0].extract()
            speed = ip.xpath('td[7]/div[@class="bar"]/@title').extract_first()
            pre_item['SPEED'] = re.search('\d+\.\d*', speed).group()
            pre_item['LAST_CHECK_TIME'] = ip.xpath('td[10]/text()')[0].extract()
            yield pre_item

















