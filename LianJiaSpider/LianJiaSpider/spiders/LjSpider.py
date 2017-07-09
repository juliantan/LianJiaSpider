# -*- coding: utf-8 -*-
import scrapy
import urllib
from lxml import etree
from LianJiaSpider.items import LianjiaspiderItem

class LjspiderSpider(scrapy.Spider):
    name = "LjSpider"
    allowed_domains = ["lianjia.com"]
    areas = ['bj','gz','sz','zs','fs']

    urlpages = []
    pagenum = 2

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
        self.pagenum = 2
        url = response.url
        self.urlpages.append(url)
        while(self.testurl(url + "/pg" + str(self.pagenum)) != []):
            print "urlpage:",url + "/pg" + str(self.pagenum)
            self.urlpages.append(url+"/pg"+str(self.pagenum))
            self.pagenum = self.pagenum + 1
        for urlpage in self.urlpages:
            # print "urlpage:",urlpage
            yield scrapy.Request(urlpage,callback=self.parse_loupaninfo)
        self.urlpages = []

    def testurl(self,url):
        html = urllib.urlopen(url).read()
        etreehtml = etree.HTML(html)
        return etreehtml.xpath("//div[@class='page-box house-lst-page-box']")

    def parse_loupaninfo(self,response):
        print "response.url:",response.url
        item = LianjiaspiderItem()
        lis = response.xpath('//ul[@class="house-lst"]/li')
        for li in lis:
            item['area'] = li.xpath('//div[@class="fl l-txt"]/a[@href="/loupan/"]/text()').extract()
            item['loupanName'] = li.xpath('./div[@class="info-panel"]/div[@class="col-1"]/h2/a/text()').extract()
            item['address'] = li.xpath('./div[@class="info-panel"]/div[@class="col-1"]/div[@class="where"]/span/text()').extract()
            item['doorModel'] = li.xpath('./div[@class="info-panel"]/div[@class="col-1"]/div[@class="area"]').xpath('string(.)').extract()
            item['state'] = li.xpath('./div[@class="info-panel"]/div[@class="col-1"]/div[@class="type"]/span[1]/text()').extract()
            item['houseType'] = li.xpath('./div[@class="info-panel"]/div[@class="col-1"]/div[@class="type"]/span[2]/text()').extract()
            item['price'] = li.xpath('./div[@class="info-panel"]/div[@class="col-2"]/div/div[@class="average"]').xpath('string(.)').extract()
            item['areaurl'] = li.xpath('//div[@class="fl l-txt"]/a[1]/@href').extract()
            item['loupanurl'] = li.xpath('./div[@class="info-panel"]/div[@class="col-1"]/h2/a/@href').extract()
            yield item













