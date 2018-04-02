# -*- coding: utf-8 -*-
import scrapy


class Log3zhihuSpider(scrapy.Spider):
    name = 'log3zhihu'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['https://www.zhihu.com/#signin']
    headers = {
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Referer:https": "//www.zhihu.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0"
    }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, meta={'cookiejar': 1}, callback=self.post_login)


    def post_login(self, response):
        xsrf = response.xpath('//input[@name="_xsrf"]/@value')[0].extract()
        print(xsrf)
        return scrapy.FormRequest.from_response(
            response,
            meta={'cookejar': response.meta['cookiejar']},
            headers=self.headers,
            formdata={'_xsrf': xsrf, 'email': '15161580934', 'password': 'zhihu789'},
            callback=self.after_login
        )

    def after_login(self, response):
        print(response.text)