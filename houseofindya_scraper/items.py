# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import scrapy

class DmozItem(scrapy.Item):
##    price = scrapy.Field()
    url = scrapy.Field()
    desc = scrapy.Field()
