# -*- coding: utf-8 -*-
import re
from scrapy import log

#PATTERN = re.compile(ur'[\u4e00-\u9fa5]+[\u0000-\u00ff\u2000-\u20ff\u3002]{0,10}[\u4e00-\u9fa5]+')
PATTERN = re.compile(ur'[\u4e00-\u9fa5]+[\w]*[\u4e00-\u9fa5]+')

def _get_encoding(response):
    charset_list = response.xpath('//meta/@content/text()').extract()
    if len(charset_list) > 0:
        charset = charset_list[0].split('=')[1]
        return charset
    charset_list = response.xpath('//meta/@charset').extract()
    if len(charset_list) > 0:
        return charset_list[0]
    return None

def _parse_page_utf8(page):
    page = unicode(page, 'utf-8')
    content_list = PATTERN.findall(page)
    return '\n'.join(content_list).encode('utf-8')

def _parse_page_gbk(page):
    page = unicode(page, 'gbk')
    content_list = PATTERN.findall(page)
    return '\n'.join(content_list).encode('utf-8')

def parse_page(response):
    charset = _get_encoding(response)
    log.msg('%s*************%s' % (response.url, charset))
    if charset == 'gb2312' or charset == 'gbk':
        return _parse_page_gbk(response.body)
    if charset == 'utf-8':
        return _parse_page_utf8(response.body)

    try:
        return _parse_page_utf8(response.body)
    except Exception, e:
        try:
            return _parse_page_gbk(response.body)
        except Exception, e:
            return None
