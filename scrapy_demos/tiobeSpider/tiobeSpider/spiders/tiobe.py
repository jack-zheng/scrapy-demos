import scrapy


class TiobeSpider(scrapy.Spider):
    name = 'tiobe'
    allowed_domains = ['tiobe.com']
    start_urls = ['https://www.tiobe.com/tiobe-index/']

    def parse(self, response):
        # 提取 top 20 排行表格
        trs = response.xpath("//table[contains(@class, 'table-top20')]/tbody//tr")
        for sub in trs:
            item = {}
            item["order"] = sub.xpath("./td[2]/text()").extract_first()
            item["name"] = sub.xpath("./td[5]/text()").extract_first()
            yield item
