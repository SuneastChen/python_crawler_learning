# -*- coding: utf-8 -*-
import scrapy


class Logren2Spider(scrapy.Spider):
    name = 'logren2'
    allowed_domains = ['renren.com']
    start_urls = []

    def start_requests(self):
        log_url = 'http://www.renren.com/PLogin.do'   # 人人网老登陆接口
        yield scrapy.FormRequest(
            url=log_url,
            formdata={'email': '15161580934', 'password': 'renren789.'},
            callback=self.parse
        )

    def parse(self, response):
        print(response.url)
        print(response.status)
        print(response.text)
        # 给url_list,再yield Resquest(url,callback)处理
