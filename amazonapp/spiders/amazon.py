import scrapy
from ..items import AmazonappItem

class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    # allowed_domains = ['amazon.com']
    start_urls = [
        'https://www.amazon.com/gp/new-releases/books/?ie=UTF8&ref_=sv_b_2'
    ]

    def parse(self, response):
        items = AmazonappItem()

        product_name = response.css('.p13n-sc-truncated::text').extract()
        product_author = response.css('.a-link-child::text').extract()
        product_price = response.css('.p13n-sc-price::text').extract()
        product_imagelink = response.css('.a-spacing-small::attr(src)').extract()

        items['product_name'] = product_name
        items['product_author'] = product_author
        items['product_price'] = product_price
        items['product_imagelink'] = product_imagelink

        yield items
