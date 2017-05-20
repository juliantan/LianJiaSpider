# -*- coding: utf-8 -*-
import scrapy
from LianJiaSpider.items import LianjiaspiderItem

class LjspiderSpider(scrapy.Spider):
    name = "LjSpider"
    allowed_domains = ["lianjia.com"]
    areas = ['sz','bj']

    def start_requests(self):
        urls = []
        for area in self.areas:
            url = 'http://'+area+'.lianjia.com/'
            url = scrapy.Request(url)
            urls.append(url)
            print url
        return urls

    def parse(self, response):
        lisleft = response.xpath('//div[@class="nav typeUserInfo"]/ul/li[2]')
        url_fang = lisleft.xpath('./a/@href').extract()[0]+'loupan'
        yield scrapy.Request(url_fang,callback=self.parse_loupan)

    def parse_loupan(self,response):
        print 'response.url:',response.url
        item = LianjiaspiderItem()
        lis = response.xpath('//ul[@class="house-lst"]/li')
        for li in lis:
            item['loupanName'] = li.xpath('./div[@class="info-panel"]/div[@class="col-1"]/h2/a/text()').extract()
            item['address'] = li.xpath('./div[@class="info-panel"]/div[@class="col-1"]/div[@class="where"]/span/text()').extract()
            item['doorModel'] = li.xpath('./div[@class="info-panel"]/div[@class="col-1"]/div[@class="area"]/text()').extract()
            item['state'] = li.xpath('./div[@class="info-panel"]/div[@class="col-1"]/div[@class="type"]/span[1]/text()').extract()
            item['houseType'] = li.xpath('./div[@class="info-panel"]/div[@class="col-1"]/div[@class="type"]/span[2]/text()').extract()
            item['price'] = li.xpath('./div[@class="info-panel"]/div[@class="col-2"]/div/div[@class="average"]/text()').extract()
            yield item

        nextPage = response.xpath('//div[@comp-module="page"]')
        print 'nextPage:',nextPage











