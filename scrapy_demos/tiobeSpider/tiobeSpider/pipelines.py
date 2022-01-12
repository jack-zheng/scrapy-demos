# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class TiobespiderPipeline:
    def process_item(self, item, spider):
        print(" ------------ < in pipeline > ------------ ")
        print(item)
        return item

class ExternalPipeline:
    def process_item(self, item, spider):
        print(" ------------ < external > ------------ ")
        print(item)
        return item