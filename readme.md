# comicSpider
1. 这是一个使用python实现的comic爬虫项目
2. 使用了scrapy爬虫框架
2. 章节解析代码如下：
```python
imgUrls = response.xpath("//ul[@id='detail-list-select']/li/a")
for imgUrl in imgUrls:
    yield{
        'charterName':imgUrl.xpath("./text()").extract_first(),
        'url':self.comic_url+imgUrl.xpath("./@href").extract_first()
    }
```
![爬虫](https://upload-images.jianshu.io/upload_images/13090773-7eb67c8bbc9bc093.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

## 下载时间
0:31 - 02:48:30

## 正添加根据读取配置文件进行爬虫功能
