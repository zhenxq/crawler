# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DaomubijiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    book_name = scrapy.Field()
    capture_name = scrapy.Field()
    caputre_url = scrapy.Field()
