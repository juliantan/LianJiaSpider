# -*- coding: utf-8 -*-
import scrapy


class LjspiderSpider(scrapy.Spider):
    name = "LjSpider"
    allowed_domains = ["sz.lianjia.com"]
    start_urls = ['http://sz.lianjia.com/']

    def parse(self, response):
        for sel in response.xpath('//div[@class="fc-main clear"]/div[@class="fl citys-l"]/ul/li'):
            print sel

