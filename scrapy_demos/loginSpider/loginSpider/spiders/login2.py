import scrapy


class Login2Spider(scrapy.Spider):
    name = 'login2'
    allowed_domains = ['github.com']
    start_urls = ['http://github.com/login']

    def parse(self, response):
        yield scrapy.FormRequest.from_response(
            response,
            formata={"login":"xxx", "password":"xxxx"},
            callback=self.after_login
        )

    def after_login(self, response):
        pass