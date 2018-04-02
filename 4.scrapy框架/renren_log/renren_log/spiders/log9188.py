# -*- coding: utf-8 -*-
import scrapy


class Log9188Spider(scrapy.Spider):
    name = 'log9188'
    allowed_domains = ['wwww.9188.com']
    start_urls = []

    def start_requests(self):
        log_url = 'http://www.9188.com/user/newlogin.go'
        yield scrapy.FormRequest(
            url=log_url,
            formdata={'uid': '天狼911', 'pwd': 'caipiao', 'yzm': ''},
            callback=self.parse_page
        )

    def parse_page(self, response):
        print(response.text)
