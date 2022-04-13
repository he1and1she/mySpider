# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from scrapy.pipelines.images import ImagesPipeline
from scrapy.pipelines.images import ImagesPipeline
import scrapy

class DownLoadPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        pageSize = 14
        item['num'] = item['pageNum']*pageSize+item['num']
        for img_url in item['image_urls']:
            yield scrapy.Request(img_url,meta={'directory':item['directory'],'num':str(item['num'])},dont_filter=True)
            item['num']+=1

    def file_path(self, request, response=None, info=None):
        # 提取url前面名称作为图片名。
        iid = request.meta['num']
        directoy = request.meta['directory']
        return u'{}/{}.jpg'.format(directoy,iid)