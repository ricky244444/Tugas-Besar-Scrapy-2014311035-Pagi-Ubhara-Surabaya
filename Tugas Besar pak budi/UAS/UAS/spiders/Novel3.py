import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://www.worldnovel.online/novel-forty-millenniums-of-cultivation-id/fmoc-chapter-1-indonesian/',
            'https://www.worldnovel.online/novel-forty-millenniums-of-cultivation-id/fmoc-chapter-2-indonesian/',
            'https://www.worldnovel.online/novel-forty-millenniums-of-cultivation-id/fmoc-chapter-3-indonesian/',
            'https://www.worldnovel.online/novel-forty-millenniums-of-cultivation-id/fmoc-chapter-4-indonesian/',
            'https://www.worldnovel.online/novel-forty-millenniums-of-cultivation-id/fmoc-chapter-5-indonesian/',
            'https://www.worldnovel.online/novel-forty-millenniums-of-cultivation-id/fmoc-chapter-6-indonesian/',
            'https://www.worldnovel.online/novel-forty-millenniums-of-cultivation-id/fmoc-chapter-7-indonesian-language/',
            'https://www.worldnovel.online/novel-forty-millenniums-of-cultivation-id/fmoc-chapter-8-indonesian/',
            'https://www.worldnovel.online/novel-forty-millenniums-of-cultivation-id/fmoc-chapter-9-indonesian/',
            'https://www.worldnovel.online/novel-forty-millenniums-of-cultivation-id/fmoc-chapter-10-indonesian/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    

    def parse(self, response):
        yield{
            'testing':response.css('#soop > p ::text').extract()
        }