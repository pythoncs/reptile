# -*- coding: utf-8 -*-

# Scrapy settings for zkzhihu project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'zkzhihu'

SPIDER_MODULES = ['zkzhihu.spiders']
NEWSPIDER_MODULE = 'zkzhihu.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'zkzhihu (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
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
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
    'cookie':'__DAYU_PP=vAfrqi6AbJB22Nybu7AZ37ff9fa2828d; _zap=1040198d-67e9-41b2-b989-586fac52cc18; _xsrf=lkWlMjdHSE1O2L3P6cN3dm1QWLbWtOtt; q_c1=af8ac78b947d4a409291de1092074427|1534936800000|1521856045000; d_c0="ACCnY-JqGA6PThFaxqYPyyGx9zhPC1RJ8fc=|1534936800"; capsion_ticket="2|1:0|10:1535014744|14:capsion_ticket|44:YzZjZWZjMzUwNjRjNGFiM2JlN2Q3OWQ0Yzk2M2U5MTA=|0da9cd29dcb6b8bca93dd8ee52f1390a38e53478f1d666869669bc1abf2dffbf"; z_c0="2|1:0|10:1535014794|4:z_c0|92:Mi4xSUlyR0N3QUFBQUFBSUtkajRtb1lEaVlBQUFCZ0FsVk5pc1ZyWEFDdlhQNXB4V1JrMnc3VFRFVDhaUEU1TFU4Y3BR|c0d468f11bf9441ace2bf7bd54474a42b4544db3b56fb24abe6afcefb590d7d1"; tgw_l7_route=56f3b730f2eb8b75242a8095a22206f8',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'zkzhihu.middlewares.ZkzhihuSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'zkzhihu.middlewares.ZkzhihuDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'zkzhihu.pipelines.ZkzhihuPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

MYSQLHOST = '127.0.0.1'
MYSQLPORT = 3306
MYSQL_DB = 'zhihu_db'
MYSQLUSER = 'root'
MYSQLPWD = '1227bing'

