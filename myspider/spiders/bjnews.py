# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule

from myspider.items import MyspiderItem

from datetime import datetime


class BjnewsSpider(CrawlSpider):
    name = 'bjnews'
    allowed_domains = ['bjnews.com.cn']
    start_urls = ['http://www.bjnews.com.cn/']

    rules = (
        #Rule(LinkExtractor(allow='\.html'), callback='parse_item'),
        #Rule(LinkExtractor(allow='/$'), follow=True),
        Rule(LinkExtractor(allow=r'html$'), callback='parse_item'),
        Rule(LinkExtractor(allow=''), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        my_item = MyspiderItem()
        my_item['keyword'] = "xinwen"
        my_item['url'] = response.url
        date_list = response.xpath('//span[contains(@class, "date")]/text()').extract()
        if len(date_list) > 0:
            my_item['web_time'] = date_list[0]
        else:
            return None
        my_item['crawl_time'] = datetime.now()
        content_list = response.xpath('//p/text()').extract()
        my_item['content'] = ''.join(content_list)
        return my_item
