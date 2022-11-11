import scrapy


class DeputadasSpider(scrapy.Spider):
    name = 'deputadas'
    allowed_domains = ['example.com']
    start_urls = ['http://example.com/']

    def parse(self, response):
        print("deputadas")
