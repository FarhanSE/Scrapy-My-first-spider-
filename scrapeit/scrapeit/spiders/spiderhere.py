import scrapy
from ..items import ScrapeitItem

class secondSpider(scrapy.Spider):
    name = 'scrapeit'
    start_urls = [
        'http://quotes.toscrape.com/'
    ]
    def parse(self, response):
        item = ScrapeitItem()
        quotes = response.css('.quote')
        for q in quotes:
            quotess = q.css('span.text::text').extract()
            author = q.css('.author::text').extract()
            tags = q.css('.tag::text').extract()

            item['quote'] = quotess
            item['author'] = author
            item['tags'] = tags
            yield item
            next_page = response.css('li.next a::attr(href)').get()
            if next_page is not None:
                yield response.follow(next_page, callback = self.parse)