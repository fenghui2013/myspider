from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware
from scrapy.contrib.downloadermiddleware.retry import RetryMiddleware
from scrapy import log
from proxy import *
from useragent import *

class MyUserAgentMiddleware(UserAgentMiddleware):
    def __init__(self, user_agent=''):
        self.user_agent = user_agent

    def process_request(self, request, spider):
        request.headers['User-Agent'] = get_useragent()
        return None

class MyHttpProxyMiddleware(object):
    def __init__(self):
        pass

    def process_request(self, request, spider):
        request.meta['proxy'] = get_proxy()
        return None

class MyRetryMiddleware(RetryMiddleware):
    def __init__(self, settings):
        pass

    def process_exception(self, request, exception, spider):
        #update proxy list, del unavailable proxy
        log.msg("retry***%s" % request.url)
        if 'proxy' in request.meta.keys():
            update_proxy(request.meta['proxy'])
        return request

    def process_response(self, request, response, spider):
        return response
