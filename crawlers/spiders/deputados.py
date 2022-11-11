import scrapy


class DeputadosSpider(scrapy.Spider):
    name = 'deputados'
    allowed_domains = ['example.com']
    start_urls = ['http://example.com/']

    def parse(self, response):
        print("deputados")
