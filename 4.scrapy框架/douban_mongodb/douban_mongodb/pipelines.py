# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings

class DoubanMongodbPipeline(object):
    def __init__(self):
        # 导入配置文件的变量
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        dbname = settings['MONGODB_DBNAME']
        sheetname = settings['MONGODB_SHEETNAME']

        self.client = pymongo.MongoClient(host=host,port=port)  # 创建连接
        db = self.client[dbname]  # 指定数据库
        self.mysheet = db[sheetname]  # 指定sheet表名

    def process_item(self, item, spider):
        self.mysheet.insert(item)
        return item

    def close_spider(self,spider):
        self.client.close()

