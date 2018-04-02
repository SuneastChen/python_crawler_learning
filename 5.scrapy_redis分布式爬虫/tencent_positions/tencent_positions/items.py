# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentPositionsItem(scrapy.Item):
    # define the fields for your item here like:
    position = scrapy.Field()
    p_class = scrapy.Field()
    number = scrapy.Field()
    addr = scrapy.Field()
    publish_t = scrapy.Field()

