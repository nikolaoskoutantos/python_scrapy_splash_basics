# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import logging
import pymongo

class MongoDBPipeline(object):
    collection_name = "coins_collection"
    
    def open_spider(self , spider):
        logging.warning("SPIDER OPENED FROM PIPELINE => OK")
        
        self.client = pymongo.MongoClient("mongodb+srv://user_nik:FaZtYSOMzpQxY9Gx@cluster0.6eraw.mongodb.net/coins?retryWrites=true&w=majority")
        self.db = self.client["coins"]

    def close_spider(self  ,spider):
        logging.warning("SPIDER CLOSED FROM PIPELINE => OK")
        self.client.close()


    def process_item(self, item, spider):
        self.db[self.collection_name].insert_one(item)
        return item
