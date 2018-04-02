# -*- coding: utf-8 -*-
import scrapy

from collectips.items import CollectipsItem,IPItemLoader
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
            item = CollectipsItem()  # 创建item实例
            item_loader = IPItemLoader(item=CollectipsItem(), response=scrapy.http.HtmlResponse(ip.extract()))   # 用自定义的itemloader取列表的第一个元素
            # print(scrapy.http.HtmlResponse(ip.extract()))
            item_loader.add_xpath('IP', '/tr/td[2]/text()')
            item_loader.add_xpath('PORT', '/tr/td[3]/text()')
            item_loader.add_xpath('POSITION', '/tr/string(td[4])')
            item_loader.add_xpath('TYPE', '/tr/td[6]/text()')
            item_loader.add_xpath('SPEED', '/tr/td[7]/div[@class="bar"]/@title')
            item_loader.add_xpath('LAST_CHECK_TIME', '/tr/td[10]/text()')

            item = item_loader.load_item()    # 取出item
            print(ip.xpath('td[2]/text()')[0].extract())
            # pre_item['IP'] = ip.xpath('td[2]/text()')[0].extract()
            # pre_item['PORT'] = ip.xpath('td[3]/text()').extract_first()
            # pre_item['POSITION'] = ip.xpath('string(td[4])').extract_first().strip()
            # pre_item['TYPE'] = ip.xpath('td[6]/text()')[0].extract()
            # speed = ip.xpath('td[7]/div[@class="bar"]/@title').extract_first()
            # pre_item['SPEED'] = re.search('\d+\.\d*', speed).group()
            # pre_item['LAST_CHECK_TIME'] = ip.xpath('td[10]/text()')[0].extract()
            yield item
















