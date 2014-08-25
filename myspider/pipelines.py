# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo


class MyspiderPipeline(object):
    def process_item(self, item, spider):
        return item

class MongodbPipeline(object):
    conn = pymongo.Connection('127.0.0.1', 27017)
    xinwen_coll = None
    shequ_coll = None
    def open_spider(self, spider):
        self.xinwen_coll = self.conn['spider']['xinwen']
        self.shequ_coll = self.conn['spider']['shequ']

    def close_spider(self, spider):
        self.conn.disconnect()

    def process_item(self, item, spider):
        if item is not None:
            if 'xinwen' == item['keyword']:
                self.xinwen_coll.save(dict(item))
            elif 'shequ' == item['keyword']:
                self.shequ_coll.save(dict(item))
