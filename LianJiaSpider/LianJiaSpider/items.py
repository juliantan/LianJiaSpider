# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    loupanName = scrapy.Field() #楼盘名称
    address = scrapy.Field() #地址
    doorModel = scrapy.Field()  #户型
    state = scrapy.Field()  #销售状态
    houseType = scrapy.Field()  #楼盘类型
    price = scrapy.Field()  #价格


