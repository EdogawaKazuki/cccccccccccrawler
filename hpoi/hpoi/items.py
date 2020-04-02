# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HpoiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class MetaDataItem(scrapy.Item):
    title = scrapy.Field()
    item_type = scrapy.Field()
    attribute = scrapy.Field()
    link = scrapy.Field()
    pic_location = scrapy.Field()
    intro = scrapy.Field()
