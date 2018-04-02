# -*- coding: utf-8 -*-
import scrapy
from douban_mongodb.items import DoubanMongodbItem

class Top250Spider(scrapy.Spider):
    name = 'top250'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250?start=%d'% i for i in range(0,251,25)]

    def parse(self, response):
        units_list = response.xpath('//div[@class="info"]')
        for u in units_list:
            # i = DoubanMongodbItem()
            i = {}
            i['title'] = u.xpath('string(./div[@class="hd"]/a/span[1])').extract()[0]
            i['introduce'] = u.xpath('string(./div[@class="bd"]/p[2])').extract()[0].strip()
            i['score'] = u.xpath('.//div[@class="star"]/span[2]/text()').extract()[0]
            i['url'] = u.xpath('./div[@class="hd"]/a/@href').extract()[0]
            yield i
