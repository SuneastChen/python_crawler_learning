# -*- coding: utf-8 -*-
import scrapy


class ViewSpider(scrapy.Spider):
    name = 'view'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        pass
