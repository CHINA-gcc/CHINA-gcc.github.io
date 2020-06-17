# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class ScrapyDemoPipeline:
    """scrapy.cfg 启用管道组件"""
    def process_item(self, item, spider):
        # with open
        return item

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        pass
