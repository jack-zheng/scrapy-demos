import scrapy
from scrapy_redis.spiders import RedisSpider


class DangdangSpider(RedisSpider):
    name = 'dangdang'
    redis_key = "dangdang"
    allowed_domains = ['book.dangdang.com']

    def parse(self, response):
        # item = {}
        # primary_cates = response.xpath("//div[@class='level_one']")
        # for primary in primary_cates:
        #     item['primary'] = primary.xpath("/dl//text()")
        # print(item)
        print(response.text)
