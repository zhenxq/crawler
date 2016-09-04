# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.conf import settings
import pymongo

class DaomubijiPipeline(object):
    def __init__(self):
        host = settings["MONGODB_HOST"]
        port = int(settings["MONGODB_PORT"])
        client = pymongo.MongoClient(host=host,port=port)
        tdb = client[settings["MONGODB_DBNSME"]]#client.Mydb
        self.mongo_book = tdb[settings["MONGODB_DOCNAME"]]

    def process_item(self, item, spider):
        self.mongo_book.insert(dict(item)) #注意数据u需要转换为dict(item)
        return item
