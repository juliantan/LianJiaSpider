# -*- coding: utf-8 -*-

# Scrapy settings for LianJiaSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'LianJiaSpider'

SPIDER_MODULES = ['LianJiaSpider.spiders']
NEWSPIDER_MODULE = 'LianJiaSpider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'LianJiaSpider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
  'Accept-Encoding':'gzip, deflate, sdch',
  'Accept-Language': 'zh-CN,zh;q=0.8',
  'Cache-Control':'max-age=0',
  'Connection':'keep-alive',
  'Cookie':'lianjia_uuid=8da3e7ad-f750-4b09-98e8-2615b3eff765; UM_distinctid=15c0000593030b-03a0e7c7e03987-3141775c-1fa400-15c00005931540; gr_user_id=714f9b7f-d9c1-440d-afcb-ab9995b9d4ab; ubta=2299869246.3523830438.1494648713677.1494650793503.1494650799351.5; sample_traffic_test=controlled_65; select_city=440300; all-lj=78917a1433741fe7067e3641b5c01569; logger_session=92de8e13676c93ff572866ccc6c5aeb2; CNZZDATA1255849469=1202742388-1494643447-http%253A%252F%252Fbzclk.baidu.com%252F%7C1494822949; _smt_uid=59168741.4b34d155; CNZZDATA1254525948=1799562724-1494643774-http%253A%252F%252Fbzclk.baidu.com%252F%7C1494821990; CNZZDATA1255633284=1054439621-1494647254-http%253A%252F%252Fbzclk.baidu.com%252F%7C1494821081; CNZZDATA1255604082=1711868508-1494646236-http%253A%252F%252Fbzclk.baidu.com%252F%7C1494820661; _gat=1; _gat_global=1; _gat_new_global=1; _ga=GA1.2.788780226.1494648644; _gid=GA1.2.1934049455.1494825684; _gat_dianpu_agent=1; lianjia_ssid=868d0aca-04f0-4e3d-8383-fbe6ff262a84',
  'Host':'sz.lianjia.com',
  'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.2669.400 QQBrowser/9.6.10990.400'	
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'LianJiaSpider.middlewares.LianjiaspiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'LianJiaSpider.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'LianJiaSpider.pipelines.LianjiaspiderPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
