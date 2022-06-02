import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://www.worldnovel.online/god-rank-upgrade-system/chapter-1/',
            'https://www.worldnovel.online/god-rank-upgrade-system/chapter-2/',
            'https://www.worldnovel.online/god-rank-upgrade-system/chapter-3/',
            'https://www.worldnovel.online/god-rank-upgrade-system/chapter-4/',
            'https://www.worldnovel.online/god-rank-upgrade-system/chapter-5/',
            'https://www.worldnovel.online/god-rank-upgrade-system/chapter-6/',
            'https://www.worldnovel.online/god-rank-upgrade-system/chapter-7/',
            'https://www.worldnovel.online/god-rank-upgrade-system/chapter-8/',
            'https://www.worldnovel.online/god-rank-upgrade-system/chapter-9/',
            'https://www.worldnovel.online/god-rank-upgrade-system/chapter-10/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    

    def parse(self, response):
        yield{
            'testing':response.css('#soop > p ::text').extract()
        }