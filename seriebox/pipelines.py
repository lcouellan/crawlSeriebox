# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

from scrapy.conf import settings
from scrapy.exceptions import DropItem
from scrapy import log


class SerieboxPipeline(object):
    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            self.collection.insert(dict(item))
            log.msg("Série ajoutée dans la base",
                    level=log.DEBUG, spider=spider)
        return item

    def __init__(self):
    	connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def from_crawler(cls, crawler):
        return cls(
            connection=crawler.settings.get('MONGODB_SERVER', 'MONGODB_PORT');
            db=crawler.settings.get('MONGO_DATABASE', 'MONGODB_COLLECTION')
        )

    def open_spider(self, spider):
        self.connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        self.db = self.connection[settings['MONGODB_DB']]

    def close_spider(self, spider):
        self.connection.close()