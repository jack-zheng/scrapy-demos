import scrapy

import logging

logger = logging.getLogger(__name__)

class TiobeSpider(scrapy.Spider):
    name = 'tiobe'
    allowed_domains = ['tiobe.com']
    start_urls = ['http://tiobe.com/']

    def parse(self, response):
        logger.warning("Hello Scrapy...")
        pass
