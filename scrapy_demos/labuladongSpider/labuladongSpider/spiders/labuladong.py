import scrapy
from copy import deepcopy


class LabuladongSpider(scrapy.Spider):
    name = 'labuladong'
    allowed_domains = ['gitee.io']
    start_urls = ['https://labuladong.gitee.io/algo/']
    # start_urls = ['https://labuladong.gitee.io/algo/1/2/']
    book_root = './book/'

    # def parse(self, response):
    #     item = {}
    #     id_title_maps = {}
    #     item["ids"] = id_title_maps

    #     id_title_maps['/1/'] = '第零章、必读文章'

    #     item['body'] = response.xpath('//div[@id="body-inner"]').get()
    #     item['title'] = '学习算法和刷题的框架思维'
    #     item['id'] = '/1/2/'
    #     yield item

    def parse(self, response):
        item = {}
        id_title_maps = {}
        item["ids"] = id_title_maps
        links = response.css('.dd-item')
        for link in links:
            # put title-id in to map
            title = link.xpath('./@title').get()
            if '/' in title:
                title = title.replace('/', '-')
            id = link.xpath('./@data-nav-id').get()
            id_title_maps[id] = title
            item['id'] = id
            item['title'] = title
            
            # check if li is a parent or not
            posts = link.xpath('.//ul').getall()
            if not posts:
                print('crawl url: ' + title)
                # 解析新页面 url
                item['href'] = self.start_urls[0] + id
                # 请求页面，抓取主体，传递到 pipeline
                yield scrapy.Request(
                    item['href'], 
                    callback=self.parse_detail, 
                    meta= { "item": deepcopy(item) })
            else:
                # create folder
                pass

    def parse_detail(self, response):
        item = response.meta["item"]
        item['body'] = response.xpath('//div[@id="body-inner"]').get()
        yield item