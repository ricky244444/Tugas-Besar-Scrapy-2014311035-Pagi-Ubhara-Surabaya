import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://www.worldnovel.online/novel-god-of-fishing/1/',
            'https://www.worldnovel.online/novel-god-of-fishing/chapter-2/',
            'https://www.worldnovel.online/novel-god-of-fishing/chapter-3/',
            'https://www.worldnovel.online/novel-god-of-fishing/chapter-4/',
            'https://www.worldnovel.online/novel-god-of-fishing/chapter-5/',
            'https://www.worldnovel.online/novel-god-of-fishing/chapter-6/',
            'https://www.worldnovel.online/novel-god-of-fishing/chapter-7/',
            'https://www.worldnovel.online/novel-god-of-fishing/chapter-8/',
            'https://www.worldnovel.online/novel-god-of-fishing/chapter-9/',
            'https://www.worldnovel.online/novel-god-of-fishing/chapter-10/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    

    def parse(self, response):
        yield{
            'testing':response.css('#soop > p ::text').extract()
        }