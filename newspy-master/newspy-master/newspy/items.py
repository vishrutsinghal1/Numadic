# -*- coding: utf-8 -*-
import scrapy


class ArticleItem(scrapy.Item):
    title = scrapy.Field()
    description = scrapy.Field()
    section = scrapy.Field()
    text = scrapy.Field()
    author = scrapy.Field()
    url = scrapy.Field()
    keywords = scrapy.Field()

