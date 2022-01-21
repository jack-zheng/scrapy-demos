import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class Cn163Spider(CrawlSpider):
    name = 'cn163'
    allowed_domains = ['cn163.net']
    start_urls = ['https://cn163.net/archives/tag/netflix/']

    rules = (
        Rule(LinkExtractor(allow=r'archives/\d+/'), callback='parse_item'),
        # 翻页规则
        Rule(LinkExtractor(allow=r'archives/tag/netflix/page/\d+/'), follow=True),
    )

    def parse_item(self, response):
        item = {}
        item['name'] = response.xpath("//h1[@class='entry-title']/text()").get()
        item['date'] = response.xpath("//span[@class='my-date']/text()").get()
        # item['content'] = response.xpath('//div[@class="single-content"]//p[1]/text()').get()
        print(item)
