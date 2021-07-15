# -*- coding: utf-8 -*-
import pymongo
from pymongo import MongoClient
from pymongo.errors import OperationFailure
from scrapy import settings
import ssl
import logging


class NewspyPipeline(object):
    def process_item(self, item, spider):
        return item


class MongoDBPipeline(object):
    def __init__(self):
        connection = pymongo.MongoClient('localhost', 27017
            #settings['MONGODB_SERVER'],
                                 #settings['MONGODB_PORT'],
                                 #username=settings['MONGODB_USER'],
                                 #password=settings['MONGODB_PASS'],
                                 #ssl=True,
                                 #ssl_cert_reqs=ssl.CERT_NONE
        )
        db = connection['scrapy']
        collection = db['news']

    def process_item(self, item, spider):
        if item['url'] is not None and item['text'] is not None:
            try:
                self.collection.update_one({'url': item['url']}, {'$set': dict(item)}, upsert=True)
            except OperationFailure as e:
                logging.log(logging.ERROR, 'Failed to save to MongoDB: ' + e.details)
        return item
