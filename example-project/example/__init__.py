
from scrapy import cmdline

spider = 'dmoz'

cmdline.execute(('scrapy crawl %s' % spider).split())
