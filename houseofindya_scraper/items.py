
import scrapy

class item_hoi(scrapy.Item):

    """ Defining field items for 
         description, price and url"""

    desc = scrapy.Field()
    price = scrapy.Field()
    url = scrapy.Field()