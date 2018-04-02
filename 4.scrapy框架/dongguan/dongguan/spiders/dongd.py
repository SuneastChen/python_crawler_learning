# -*- coding: utf-8 -*-
import scrapy


class DongdSpider(scrapy.Spider):
    name = 'dongd'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/report?page=%d' % i for i in range(0,700,30)]

    def parse(self,response):
        for new in response.xpath('//a[@class="news14"]/@href').extract():
            yield scrapy.Request(new,callback=self.parse_item)

    def parse_item(self, response):
        i = {}
        i['title'] = response.xpath('//div[@class="pagecenter p3"]//strong[@class="tgray14"]/text()').extract()[0].split()[0]
        i['number'] = response.xpath('//div[@class="pagecenter p3"]//strong[@class="tgray14"]/text()').extract()[0].split()[-1].split(':')[-1]
        i['content'] = response.xpath('string(//div[@class="c1 text14_2"])').extract()[0].split()
        return i


