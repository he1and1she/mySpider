# Scrapy settings for mySpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'mySpider'

SPIDER_MODULES = ['mySpider.spiders']
NEWSPIDER_MODULE = 'mySpider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'mySpider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
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
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
  'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.37'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'mySpider.middlewares.MyspiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'mySpider.middlewares.MyspiderDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'mySpider.pipelines.DownLoadPipeline': 300,
}

IMAGES_STORE  = './images/家庭教师'
# import os
# project_dir=os.path.abspath(os.path.dirname(__file__))
# IMAGES_STORE=os.path.join(project_dir,'images')   #漫画存储在项目根目录下的images文件夹下

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
AUTOTHROTTLE_START_DELAY = 1
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

#需要设置的一些变量

####爬一人之下的配置
allowed_domains = 'www.szcdmj.com'  #允许爬的域名
start_urls = 'https://www.szcdmj.com/szcbook/67621'  #爬虫开始链接
comic_url = 'https://www.szcdmj.com'  #url前缀
ImgDirXpath = "//ul[@id='detail-list-select']/li/a"  #对应漫画目录规则
NextPageXpath = "//div[@class='fanye'][2]/a[3]/@href" #下一页规则
imageXpath = "//div[@class='comicpage']/div/img[@class='lazy']/@data-original" #漫画图片规则
#####
# allowed_domains = 'www.cocomanhua.com'  #允许爬的域名
# start_url = 'https://www.cocomanhua.com/17484/'  #爬虫开始链接
# comic_url = 'https://www.cocomanhua.com/'  #url前缀
# ImgDirXpath = "//li[@class='fed-padding fed-col-xs6 fed-col-md3 fed-col-lg3']/a[@class='fed-btns-info fed-rims-info fed-part-eone']"  #对应漫画目录规则
# NextPageXpath = "//div[@class='fanye'][2]/a[3]/@href" #下一页规则
# imageXpath = "//div[@class='comicpage']/div/img[@class='lazy']/@data-original" #漫画图片规则