# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from doutu.settings import IMAGES_STORE


class DoutuPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        img_url = item['img_url']
        yield scrapy.Request(img_url)

    def item_completed(self, results, item, info):
        img_old_name = [x['path'] for ok, x in results if ok]
        # os.rename(image_jname[0], './full/'+item['name']+image_jname[0][-4:])
        global IMAGES_STORE
        os.rename(os.path.join(IMAGES_STORE, img_old_name[0]), os.path.join(IMAGES_STORE, item['name'] + item['img_url'][-4:]))
        return item


