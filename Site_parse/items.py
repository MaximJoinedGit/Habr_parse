# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class InfoItem(scrapy.Item):
    # _id = scrapy.Field()
    page_header = scrapy.Field()
    page_url = scrapy.Field()
    page_text = scrapy.Field()
    page_tags = scrapy.Field()
