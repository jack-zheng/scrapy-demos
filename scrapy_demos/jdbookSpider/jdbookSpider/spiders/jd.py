import json
import scrapy
from copy import deepcopy


class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['jd.com']
    start_urls = ['https://pjapi.jd.com/book/sort?source=bookSort']

    def start_requests(self):
        # 新版的 API 需要指定两个属性
        headers={"referer":"https://book.jd.com/", "authority":"pjapi.jd.com"}
        yield scrapy.Request(
            self.start_urls[0],
            callback=self.parse,
            headers=headers
        )

    def parse(self, response):
        json_data = json.loads(response.text)
        book_list_template = "https://list.jd.com/list.html?cat=%d,%d,%d"
        for category in json_data['data']:
            item = {}
            cate_1 = category['fatherCategoryId']
            item['cate1'] = category['categoryName']
            for sub in category['sonList']:
                cate_2 = sub['fatherCategoryId']
                item['cate2'] = sub['categoryName']
                print(book_list_template %(cate_1, cate_2, sub['categoryId']))
                yield scrapy.Request(
                    book_list_template %(cate_1, cate_2, sub['categoryId']),
                    callback=self.parse_book_list,
                    meta = {"item": deepcopy(item)}
                )
    
    def parse_book_list(self, response):
        item = response.meta['item']
        print(response.text)
        # book_list = response.xpath("//div[@id='J_goodsList']/ul/li")
        # for book in book_list:
            # item['img'] = book.xpath("//div[@class='p-img']/a/@href").get()
            # item['price'] = book.xpath("//div[@class='p-price']//i/text()").get()
            # item['title'] = book.xpath("//div[@class='p-name']//em/text()").get()
            # item['author'] = book.xpath("//div[@class='p-bookdetails']/span[@class='p-bi-name']/a/text()").extract()
            # item['publisher'] = book.xpath("//div[@class='p-bookdetails']/span[@class='p-bi-store']/a/text()").extract()
            # print(book.xpath("//div[@class='p-name']//em/text()").get())
