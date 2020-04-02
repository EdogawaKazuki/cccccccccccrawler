import scrapy


class Spider(scrapy.Spider):
    name = "hpoi"

    def start_requests(self):
        urls = []
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        pass
