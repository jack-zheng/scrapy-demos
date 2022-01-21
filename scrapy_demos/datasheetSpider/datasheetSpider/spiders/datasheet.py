import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

'''
德州仪器生产的元器件使用手册信息收集
'''
class DatasheetSpider(CrawlSpider):
    name = 'datasheet'
    allowed_domains = ['datasheet.eeworld.com.cn']
    start_urls = ['http://datasheet.eeworld.com.cn/manufacturer/texas-instruments.html']

    rules = (
        # 匹配手册地址
        Rule(LinkExtractor(allow=r'/part/\w+,texas-instruments,\d+\.html'), callback='parse_item'),
    )

    # 从页面提取所需的信息
    def parse_item(self, response):
        item = {}
        item['name'] = response.xpath("//div[contains(@class,'detail-down')]/div[@class='down-right']//dd[1]/var/text()").get()
        item['type'] = response.xpath("//div[contains(@class,'detail-down')]/div[@class='down-right']//dd[2]/var//a/text()").extract()
        item['description'] = response.xpath("//div[@class='detail-bd']//p[1]/text()").get()
        print(item)
