# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class MyspiderItem(scrapy.Item):
    keyword = scrapy.Field()
    url = scrapy.Field()
    crawl_time = scrapy.Field()
    content = scrapy.Field()
