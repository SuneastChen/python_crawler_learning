# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst

class QItemLoader(ItemLoader):      #继承itemloader,自定义类
    default_output_processor = TakeFirst()  # 默认输出第一个值

def process_v(value):
    return value.split()[-1].split(':')[-1]

class DongguanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field(input_processor=MapCompose(lambda x: x.split()[0]))
    number = scrapy.Field(input_processor=MapCompose(process_v))
    content = scrapy.Field(input_processor=MapCompose(lambda x: x.split()))
    
