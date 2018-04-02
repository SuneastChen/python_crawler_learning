# _*_ coding:utf-8 _*_
# !/usr/bin/python

import os
import scrapy
from doutu.items import DoutuItem

try:
    os.makedirs(r'.\imgs')
except:
    pass


class Doutu(scrapy.Spider):
    name = 'doutu'
    allowed_domains = ['doutula.com']  # 定义域名范围
    start_urls = ['http://www.doutula.com/photo/list/?page={}'.format(i) for i in range(80, 90)]

    # 默认调用parse()此方法
    def parse(self, response):  # response 是上面网址请求到的源代码
        for content in response.xpath('//*[@id="pic-detail"]/div/div[1]/div[1]/ul/li/div/div/a'):
            item = DoutuItem()  # 实例化容器
            # print(content)
            item['img_url'] = content.xpath('./img/@data-original').extract_first()  
            item['name'] = content.xpath('./p/text()').extract_first()

            yield item


