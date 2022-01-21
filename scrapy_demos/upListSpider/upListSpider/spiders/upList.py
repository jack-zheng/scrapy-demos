import json
import scrapy


class UplistSpider(scrapy.Spider):
    name = 'upList'
    allowed_domains = ['bilibili.com']
    start_urls = ['https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/w_dyn_uplist?teenagers_mode=0']

    def start_requests(self):
        # 从浏览器扒的 cookies
        cookies = "l=v; _uuid=6EEBEA48...526"
        cookies = {sub.split("=")[0]:sub.split("=")[1] for sub in cookies.split("; ")}
        yield scrapy.Request(
            self.start_urls[0],
            callback=self.parse,
            cookies=cookies
        )

    def parse(self, response):
        resp = json.loads(response.body_as_unicode())
        # 打印 up 名字
        for item in resp['data']['items']:
            print(item['user_profile']['info']['uname'])
