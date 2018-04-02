# _*_ coding:utf-8 _*_
# !/usr/bin/python

import os
import scrapy
from doutu.items import DoutuItem
import requests

class Doutu(scrapy.Spider):
    name = 'doutu'
    allowed_domains = ['doutula.com']  # 定义域名范围
    start_urls = ['http://www.doutula.com/photo/list/?page={}'.format(i) for i in range(1, 5)]

    # 默认调用parse()此方法
    def parse(self, response):  # response 是上面网址请求到的源代码
        items_list = []
        for content in response.xpath('//a[@class="col-xs-6 col-sm-3"]'):
            item = DoutuItem()  # 实例化容器
            item['img_url'] = content.xpath('./img/@data-original').extract_first()
            item['name'] = content.xpath('./p/text()').extract_first()
        #     items_list.append(item)
        # print(items_list)

            # try:
            #     filename = 'imgs\{}'.format(item['name']) + item['img_url'][-4:]  # 图片路径
            #     if not os.path.exists(filename):
            #         headers = {'User-Agent': "'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'"}
            #         r = requests.get(item['img_url'], headers=headers)
            #         with open(filename,'wb') as f:
            #             f.write(r.content)
            #         print('保存成功!')

            # except Exception as e:
            #     print(e)


            yield item


