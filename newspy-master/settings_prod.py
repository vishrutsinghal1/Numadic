# -*- coding: utf-8 -*-
BOT_NAME = 'newspy'
SPIDER_MODULES = ['newspy.spiders']
NEWSPIDER_MODULE = 'newspy.spiders'
ROBOTSTXT_OBEY = True
ITEM_PIPELINES = {
    'newspy.pipelines.MongoDBPipeline': 100
}
DOWNLOAD_DELAY = 2
MONGODB_SERVER = 'localhost'
MONGODB_PORT = 27017
MONGODB_USER = 'admin'
#MONGODB_PASS = 'e6h65J6I4vilmjS'
MONGODB_DB = 'scrapy'
MONGODB_COLLECTION = 'news'
