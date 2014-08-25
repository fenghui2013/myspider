# -*- coding: utf-8 -*-

# Scrapy settings for myspider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'myspider'

SPIDER_MODULES = ['myspider.spiders']
NEWSPIDER_MODULE = 'myspider.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'myspider (+http://www.yourdomain.com)'

#concurrency setting
CONCURRENT_REQUESTS = 100
#CONCURRENT_REQUESTS_PER_DOMAIN = 2

#download setting
DOWNLOAD_TIMEOUT = 10
#DOWNLOAD_DELAY = 0

#mem setting
MEMUSAGE_LIMIT_MB = 512
#disk queue setting
JOBDIR = None
WANGYI_JOBDIR = '/tmp/jobdir/wangyi'
SOHU_JOBDIR = '/tmp/jobdir/sohu'
SHEQUTIANYA_JOBDIR = '/tmp/jobdir/shequtianya'
SHEQUBAIDUTIEBA_JOBDIR = '/tmp/jobdir/shequbaidutieba'

#breadth-first setting
DEPTH_PRIORITY = 1
SCHEDULER_DISK_QUEUE = 'scrapy.squeue.PickleFifoDiskQueue'
SCHEDULER_MEMORY_QUEUE = 'scrapy.squeue.FifoMemoryQueue'

#pipeline setting
ITEM_PIPELINES = {
    'myspider.pipelines.MongodbPipeline': 0,
}

#downloader middleware setting
DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
    'myspider.middleware_downloader.MyUserAgentMiddleware': 400,
    'scrapy.contrib.downloadermiddleware.retry.RetryMiddleware': None,
    'myspider.middleware_downloader.MyRetryMiddleware': 501,
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': None,
    'myspider.middleware_downloader.MyHttpProxyMiddleware': 750,
}

#log setting
LOG_ENABLED = True
LOG_ENCODING = 'utf-8'
LOG_FILE = '/tmp/myspider.log'
LOG_LEVEL = 'DEBUG'
LOG_STDOUT = True

#useragent init
from useragent import *
init_useragent()

#proxy init
from proxy import *
init_proxy()
#proxy setting
AVAILABLE_PROXY_LIST_MIN = 10
