# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import requests
import os
class DoutuPipeline(object):
    def process_item(self, item, spider):
        try:
            filename = '.\imgs\{}'.format(item['name']) + item['img_url'][-4:]  # 图片路径
            if not os.path.exists(filename):
                headers = {'User-Agent': "'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'"}
                r = requests.get(item['img_url'], headers=headers)
                with open(filename,'wb') as f:
                    f.write(r.content)
                print('保存成功!')

        except Exception as e:
            print(e)
        return item
