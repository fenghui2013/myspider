import random, urllib2, re, time

from scrapy import log
import settings

AVAILABLE_PROXY_LIST = []

def init_proxy():
    print "+++++++++++++++++++++++++init_proxy"
    global AVAILABLE_PROXY_LIST
    pattern = re.compile(r'<td>(\d+\.\d+\.\d+\.\d+)</td><td>(\d+)</td>')

    for i in xrange(10):
        try:
            req_url = "http://www.proxy.com.ru/list_%d.html" % (i+1)
            req = urllib2.Request(req_url)
            res = urllib2.urlopen(req).read()
            temp_list = pattern.findall(res)
            for temp in temp_list:
                AVAILABLE_PROXY_LIST.append('http://'+':'.join(temp))
        except Exception, e:
            continue

def get_proxy():
    print "+++++++++++++++++++++++++get_proxy"
    global AVAILABLE_PROXY_LIST
    p = None
    while True:
        if len(AVAILABLE_PROXY_LIST) > 0:
            p = random.choice(AVAILABLE_PROXY_LIST)
            break
        time.sleep(1)
    return p

def update_proxy(p):
    print "+++++++++++++++++++++++++update_proxy"
    global AVAILABLE_PROXY_LIST
    
    print p
    if p in AVAILABLE_PROXY_LIST:
        AVAILABLE_PROXY_LIST.remove(p)
    log.msg("AVAILABLE_PROXY_LIST length: %d" % len(AVAILABLE_PROXY_LIST))
    if len(AVAILABLE_PROXY_LIST) < settings.AVAILABLE_PROXY_LIST_MIN:
        init_proxy()
