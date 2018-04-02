# -*- coding: utf-8 -*-
import scrapy


class ProxySpider(scrapy.Spider):
    name = 'proxy'
    allowed_domains = ['www.ipdizhichaxun.com']
    start_urls = ['http://www.ipdizhichaxun.com/']

    def parse(self, response):
        print(response.text)

