from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy import log, signals
from myspider.spiders.wangyi import WangyiSpider
from myspider.spiders.sohu import SohuSpider
from myspider.spiders.shequ_baidutieba import ShequBaidutiebaSpider
from myspider.spiders.shequ_tianya import ShequTianyaSpider
from scrapy.utils.project import get_project_settings

settings = get_project_settings()
if settings['LOG_ENABLED']:
    log.start(logfile=settings['LOG_FILE'], loglevel=settings['LOG_LEVEL'], logstdout=settings['LOG_STDOUT'])

#wangyi spider start
settings.set('JOBDIR', settings['WANGYI_JOBDIR'])
wangyi_settings = settings
wangyi_spider = WangyiSpider()
wangyi_crawler = Crawler(wangyi_settings)
#wangyi_crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
wangyi_crawler.configure()
wangyi_crawler.crawl(wangyi_spider)
wangyi_crawler.start()

#sohu spider start
settings.set('JOBDIR', settings['SOHU_JOBDIR'])
sohu_settings = settings
sohu_spider = SohuSpider()
sohu_crawler = Crawler(sohu_settings)
#sohu_crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
sohu_crawler.configure()
sohu_crawler.crawl(sohu_spider)
sohu_crawler.start()

#shequ_tianya spider start
settings.set('JOBDIR', settings['SHEQUTIANYA_JOBDIR'])
shequtianya_settings = settings
shequtianya_spider = ShequTianyaSpider()
shequtianya_crawler = Crawler(shequtianya_settings)
#shequtianya_crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
shequtianya_crawler.configure()
shequtianya_crawler.crawl(shequtianya_spider)
shequtianya_crawler.start()


#shequ_baidutieba spider start
settings.set('JOBDIR', settings['SHEQUBAIDUTIEBA_JOBDIR'])
baidutieba_settings = settings
shequbaidutieba_spider = ShequBaidutiebaSpider()
shequbaidutieba_crawler = Crawler(baidutieba_settings)
#shequbaidutieba_crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
shequbaidutieba_crawler.configure()
shequbaidutieba_crawler.crawl(shequbaidutieba_spider)
shequbaidutieba_crawler.start()

reactor.run()
