# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from collectips.settings import DBKWARGS

class CollectipsPipeline(object):
    def __init__(self):
        # DBKWARGS = spider.settings.get('DBKWARGS')  # 引入setgings的DBKWARGS变量
        self.con = pymysql.connect(**DBKWARGS)
        self.cur = self.con.cursor()    

    def process_item(self, item, spider):

        self.con.select_db('test')  # 需要先选择数据库
        lis = (item['IP'], item['PORT'], item['TYPE'], item['POSITION'], item['SPEED'], item['LAST_CHECK_TIME'])
        sql = ('insert into proxy (IP,PORT,TYPE,POSITION,SPEED,LAST_CHECK_TIME) '
               'values ("%s","%s","%s","%s",%s,"%s");' % lis)
        print(sql)
        try:
            self.cur.execute(sql)
        except Exception as e:
            print('执行sql语句发生异常:', e)
            self.con.rollback()
        else:
            self.con.commit()
        return item   # 告诉引擎,item处理完了,可以给我下一个item

    def close_spider(self,spider): 
        self.cur.close()
        self.con.close()





















