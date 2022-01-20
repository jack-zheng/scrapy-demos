import scrapy
from copy import deepcopy

'''
Suning 的页面改版了，而且比较杂乱，找了一下和以前类似的 孔夫子旧书网 作为联系对象
'''
class KongfzSpider(scrapy.Spider):
    name = 'kongfz'
    allowed_domains = ['kongfz.com']
    start_urls = ['http://kongfz.com/']

    def parse(self, response):
        groups = response.xpath("//div[@class='cagetory-box']/div[contains(@class, 'list-group')]")
        for group in groups:
            item = {}
            item['group'] = group.xpath("./div[contains(@class, 'item-header')]/a[contains(@class, 'title')]/text()").get()
            category_list = group.xpath("./div//a[@class='item-title']")
            for cate in category_list:
                item['href'] = cate.xpath("./@href").get()
                item['category'] = cate.xpath("./text()").get()
                # 进去子类型页面
                print(item)
                yield scrapy.Request(
                    item['href'],
                    callback=self.parse_book_list_detail,
                    meta= { "item": deepcopy(item) }
                )

    def parse_book_list_detail(self, response):
        item = response.meta['item']
        book_list = response.xpath(".//div[@class='result-list']/div")
        for book in book_list:
            item['name'] = book.xpath(".//div[@class='title']/a/text()").get()
            item['quality'] = book.xpath(".//div[contains(@class, 'quality')]/text()").get()
            item['user'] = book.xpath(".//div[@class='text on-line']/a[@class='user-info-link']/text()").get()
            item['user_href'] = book.xpath(".//div[@class='text on-line']/a[@class='user-info-link']/@href").get()
            # 查询卖家信誉
            # 程序运行中有时会在拿用户信息的时候抛错，稍微查看了一下，收藏鉴赏栏目中的书籍是没有一些基本信息的
            # 懒得改了，基本目的已经达到
            yield scrapy.Request(
                item['user_href'],
                callback=self.get_seller_score,
                meta={ "item": deepcopy(item) }
            )
    
    def get_seller_score(self, response):
        item = response.meta['item']
        item['registry_date'] = response.xpath(".//table//tr[last()-1]/td[2]/text()").get()
        print(item)

