# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Join, Compose


class KeyboardsItem(Item):
    name = Field()
    price = Field()
    url = Field()

class KeyboardsItemLoader(ItemLoader):
    default_output_processor = TakeFirst()
    default_item_class = KeyboardsItem
    name_out = Join()
    price_in = MapCompose(
        # lambda s: s.strip('$'),
        # lambda s: float(s),
        # lambda s: { 'price': s, 'currency': 'USD' }
    )
