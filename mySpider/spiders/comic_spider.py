import scrapy

from mySpider.items import MyspiderItem
from copy import deepcopy
from scrapy.utils.project import get_project_settings

class ComicSpider(scrapy.Spider):
    name = 'comic_spider'
    settings = get_project_settings()
    allowed_domains = ['www.szcdmj.com']
    # start_urls = ['https://www.szcdmj.com/szcbook/3234']
    start_urls = ['https://www.szcdmj.com/szcbook/67621']
    comic_url = 'https://www.szcdmj.com'
    # allowed_domains = settings.get('allowed_domains')
    # start_urls = settings.get('start_urls')
    # comic_url = settings.get('comic_url')

    def parse(self, response):
        # ImgDirXpath = self.settings.get('ImgDirXpath')
        # charterUrls = response.xpath(ImgDirXpath)
        charterUrls = response.xpath("//ul[@id='detail-list-select']/li/a")
        item = MyspiderItem()
        item['image_urls'] = []
        item['pageNum'] = 0
        item['num'] = 0

        for charterUrl in charterUrls:
            item['directory']=charterUrl.xpath("./text()").extract_first()
            parentUrl = self.comic_url+charterUrl.xpath("./@href").extract_first()
            yield scrapy.Request(parentUrl,
                callback=self.parse_page,
                meta={"item": deepcopy(item)}
            )
    def parse_page(self,response):
        item=response.meta['item']
        yield scrapy.Request(response.url,
                callback=self.parse_img,
                meta={"item": deepcopy(item)},
                dont_filter=True
            )
        # NextPageXpath = self.settings.get('NextPageXpath')
        # nextPage = response.xpath(NextPageXpath).extract_first()
        nextPage = response.xpath("//div[@class='fanye'][2]/a[3]/@href").extract_first()
        if nextPage is not None : 
            item['pageNum'] += 1 
            yield scrapy.Request(self.comic_url+nextPage,
                callback=self.parse_page,
                meta={"item":deepcopy(item)}
            )
    def parse_img(self,response):
        imgs=[]
        item = response.meta['item']
        # imageXpath = self.settings.get('imageXpath')
        # imgUrls=response.xpath().extract(imageXpath)
        imgUrls=response.xpath("//div[@class='comicpage']/div/img[@class='lazy']/@data-original").extract()
        for imgUrl in imgUrls:
            imgs.append(imgUrl)
        item['image_urls'] = imgs
        yield item