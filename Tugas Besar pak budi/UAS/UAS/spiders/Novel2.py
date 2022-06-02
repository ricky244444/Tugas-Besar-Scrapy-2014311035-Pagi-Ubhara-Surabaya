import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://www.worldnovel.online/the-earth-is-my-dantian/chapter-1-young-master-twelve-ye-sheng/',
            'https://www.worldnovel.online/the-earth-is-my-dantian/chapter-2-the-earth-is-my-dantian/',
            'https://www.worldnovel.online/the-earth-is-my-dantian/chapter-3-incredible-improvement/',
            'https://www.worldnovel.online/the-earth-is-my-dantian/chapter-4-the-old-ladys-reprimand/',
            'https://www.worldnovel.online/the-earth-is-my-dantian/chapter-5-butler-fu/',
            'https://www.worldnovel.online/the-earth-is-my-dantian/chapter-6-army-paddles/',
            'https://www.worldnovel.online/the-earth-is-my-dantian/chapter-7-up-to-no-good/',
            'https://www.worldnovel.online/the-earth-is-my-dantian/chapter-8-the-general-collections-library/',
            'https://www.worldnovel.online/the-earth-is-my-dantian/chapter-9-water-chestnut-flower/',
            'https://www.worldnovel.online/the-earth-is-my-dantian/chapter-10-reincarnation-seal/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    

    def parse(self, response):
        yield{
            'testing':response.css('#soop > p ::text').extract()
        }