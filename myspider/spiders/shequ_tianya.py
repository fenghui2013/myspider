# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule

from myspider.items import MyspiderItem
from myspider.parse_page import *

from datetime import datetime


class ShequTianyaSpider(CrawlSpider):
    name = 'shequ_tianya'
    allowed_domains = ['tianya.cn']
    start_urls = ['http://bbs.tianya.cn/']

    rules = (
        #Rule(LinkExtractor(allow=r'[\w]$'), callback='parse_item'),
        #Rule(LinkExtractor(allow=r'/$')),
        Rule(LinkExtractor(allow=r'html$'), callback='parse_item'),
        Rule(LinkExtractor(allow=''), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        my_item = MyspiderItem()
        my_item['keyword'] = 'shequ'
        my_item['url'] = response.url
        my_item['content'] = parse_page(response)
        my_item['crawl_time'] = datetime.utcnow()
        return my_item
