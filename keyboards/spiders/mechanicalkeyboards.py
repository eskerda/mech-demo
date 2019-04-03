# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from keyboards.items import KeyboardsItemLoader

class MechanicalkeyboardsSpider(Spider):
    name = 'mechanicalkeyboards'

    categories_url = 'https://mechanicalkeyboards.com/shop/'

    def start_requests(self):
        if hasattr(self, 'test_spider'):
            for url, callback in self.test_requests:
                yield Request(url, callback=callback)
            return
        yield Request(self.categories_url, callback=self.parse)

    @property
    def test_requests(self):
        return (
            ('https://mechanicalkeyboards.com/shop/index.php?l=product_list&c=53', self.parse_category),
            ('https://mechanicalkeyboards.com/shop/index.php?l=product_detail&p=4598', self.parse_product),
        )

    def parse(self, response):
        categories = response.css('div#mega-menu ul li a::attr(href)')
        for url in categories.extract():
            yield Request(response.urljoin(url), callback=self.parse_category)

    def parse_category(self, response):
        products = response.css('div.product-name a::attr(href)')
        for url in products.extract():
            yield Request(response.urljoin(url), callback=self.parse_product)

        next_page = next(iter(response.xpath("""
            //div[contains(@class, "blog-pagination")]//
                a[contains(@title, "Next Page")]/@href
        """).extract()), None)

        if next_page:
            yield Request(response.urljoin(next_page),
                          callback=self.parse_category)

    def parse_product(self, response):
        product = response.css('section.product-info')
        loader = KeyboardsItemLoader(selector=product)
        loader.add_css('name', 'h4.name ::text')
        loader.add_css('price', 'div#product_price ::text')
        loader.add_value('url', response.url)
        yield loader.load_item()

        # yield {
        #     "name": ''.join(product.css('h4.name ::text').extract()),
        #     "price": ''.join(product.css('div#product_price ::text').extract()),
        #     "url": response.url,
        # }
