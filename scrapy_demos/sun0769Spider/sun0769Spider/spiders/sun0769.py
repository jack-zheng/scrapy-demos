import scrapy
from sun0769Spider.items import SunItem

class Sun0769Spider(scrapy.Spider):
    name = 'sun0769'
    allowed_domains = ['sun0769.com']
    start_urls = ['https://wz.sun0769.com/political/index/politicsNewest?id=1&page=1']
    host = "https://wz.sun0769.com"

    def parse(self, response):
        li_list = response.xpath("//li[@class='clear']")
        for li in li_list:
            item = SunItem()
            item['title'] = li.xpath(".//span[@class='state3']//a/text()").get()
            item['href'] = self.host + li.xpath(".//span[@class='state3']//a/@href").get()
            item['publish_date'] = li.xpath(".//span[last()]/text()").get()
            # detail info
            yield scrapy.Request(
                item['href'],
                callback=self.parse_detail,
                meta= {"item": item}
            )
        # 翻页，2022-01-19 网站有 bug, 100 页之后不能显示，直接跳到第一页了 （；￣ェ￣）
        # 只为了示范，拿前五页的数据就行了
        next_url = self.host + response.xpath("//a[contains(@class, 'prov_rota')]/@href").get()
        if next_url is not None and "page=3" not in next_url:
            yield scrapy.Request(
                next_url,
                callback=self.parse
            )


    def parse_detail(self, response):
        item = response.meta["item"]
        item['content'] = response.xpath("//div[@class='details-box']/pre/text()").get()
        item['content_img'] = response.xpath("//div[contains(@class,'details-img-list')]//img/@src").extract()
        yield item