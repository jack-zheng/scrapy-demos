import re
import scrapy


class Login1Spider(scrapy.Spider):
    name = 'login1'
    allowed_domains = ['github.com']
    start_urls = ['https://www.github.com/login']

    # def start_requests(self):  # 控制爬虫发出的第一个请求
    #     proxy = "xxxxxx"
    #     yield scrapy.Request(self.start_urls[0], meta={"proxy": proxy})

    def parse(self, response):
        authenticity_token = response.xpath("//input[@name='authenticity_token']/@value").get()
        print("*"*10 + " get token: " + authenticity_token)
        post_data = dict(
            authenticity_token = authenticity_token,
            login = "xxx",
            password = "xxx"
        )

        yield scrapy.FormRequest(
            "https://github.com/session",
            formdata=post_data,
            callback=self.after_login
        )

    def after_login(self, response):
        print(re.findall("jack-zheng", response.body.decode()))
