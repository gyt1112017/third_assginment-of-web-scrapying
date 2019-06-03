# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
import scrapy
from scrapy.loader.processors import TakeFirst, MapCompose, Join
from w3lib.html import remove_tags

"""
class QuotesItem(scrapy.Item):
    quote = scrapy.Field(
        output_processor = TakeFirst()
    )
    author = scrapy.Field(
        output_processor = TakeFirst()
    )
    tags = scrapy.Field(
        output_processor = Join(';')
    )
"""
def remove_quotations(value):
    return value.replace(u"\u201d", '').replace(u"\u201c", '')

def strip_value(value):
    return value.strip()

class QuotesItem(scrapy.Item):
    quote= scrapy.Field(
        input_processor= MapCompose(strip_value, remove_quotations),
        output_processor= TakeFirst()
    )
    author= scrapy.Field(
        input_processor= MapCompose(remove_tags, strip_value),
        output_processor= TakeFirst()
    )
    tags= scrapy.Field(
        input_processor= MapCompose(remove_tags),
        output_processor= Join(',')
    )