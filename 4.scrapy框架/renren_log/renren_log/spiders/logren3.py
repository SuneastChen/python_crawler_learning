# -*- coding: utf-8 -*-
import scrapy


class Logren3Spider(scrapy.Spider):
    name = 'logren3'
    allowed_domains = ['www.renren.com']
    start_urls = ['http://www.renren.com/SysHome.do']   # 人人网最新登陆接口界面

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={'email': '15161580934', 'password': 'renren789.'},
            callback = self.after_login
        )

    def after_login(self,response):
        return scrapy.Request('http://www.renren.com/842465956/profile',callback=self.parse_page)

    def parse_page(self,response):
        print(response.text)