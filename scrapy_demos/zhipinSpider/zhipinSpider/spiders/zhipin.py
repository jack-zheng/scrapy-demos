import scrapy


class ZhipinSpider(scrapy.Spider):
    '''
    boss 直聘前十页的招聘信息
    '''
    name = 'zhipin'
    allowed_domains = ['zhipin.com']
    start_urls = ['https://www.zhipin.com/c101210100-p100101/']

    def parse(self, response):
        job_list = response.xpath("//div[@class='job-list']/ul/li")
        for job in job_list:
            item = {}
            item["title"] = job.xpath(".//span[@class='job-name']/a/text()").get()
            item["pay"] = job.xpath(".//span[@class='red']/textt()").get()
            item["company"] = job.xpath(".//div[@class='info-company']//a/text()").get()
            print(item)
        pass
