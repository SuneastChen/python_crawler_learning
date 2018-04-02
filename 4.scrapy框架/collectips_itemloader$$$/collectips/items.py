# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst
import re

class IPItemLoader(ItemLoader):      #继承itemloader,自定义类
    default_output_processor = TakeFirst()  # 默认输出第一个值

def re_speed(value):
    return re.search('\d+\.\d*', value).group()

class CollectipsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    IP = scrapy.Field()
    PORT = scrapy.Field()
    POSITION = scrapy.Field(
        input_processor=MapCompose(lambda x : x.strip(),))
    TYPE = scrapy.Field()
    SPEED = scrapy.Field(
        input_processor=MapCompose(re_speed,))
    LAST_CHECK_TIME = scrapy.Field()
