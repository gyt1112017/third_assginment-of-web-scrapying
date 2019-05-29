import scrapy
from urllib.parse import urljoin
from scrapy.loader import ItemLoader
from third_assignment.items import QuotesItem

class QuotesToScrapeSpider(scrapy.Spider):
    #identity
    name="quotes"
    
    #Request
    def start_requests(self):
        url= 'http://quotes.toscrape.com/'
        yield scrapy.Request(url=url, callback=self.parse)

    #Response
    def parse(self, response):
        quotes = response.xpath("//div[@class='quote']")
        for quote in quotes:
            loader = ItemLoader(item=QuotesItem(), selector=quote, response=response)
            loader.add_xpath("quote", ".//span[@class='text']/text()")
            loader.add_xpath("author", ".//span[2]/small/text()")
            loader.add_xpath("tags", ".//div[@class='tags']/a/text()")
        
            yield loader.load_item()


        next_page = response.xpath("//li[@class='next']/a/@href").extract_first()
        if next_page:
            next_page_page = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_page, callback=self.parse)
