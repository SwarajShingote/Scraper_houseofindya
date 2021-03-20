import scrapy  

class firstSpider(scrapy.Spider): 
  name = "HouseofIndya"
  allowed_domains = ["https://www.houseofindya.com"]
  start_urls = [ 
     "https://www.houseofindya.com/zyra/necklace-sets/cat" 
  ]
   
  
  def parse(self, response):
     d1 = response.css('div.catgItem')
     for i in d1 :
         desc = i.css('img').attrib['alt']
         url = i.css('img').attrib['data-original']
         yield {
            'desc' : desc ,
            'url' : url,
         }
         # print('Desc: ', desc)
         # print('url: ', desc)

# import scrapy

# from houseofindya_scraper.items import DmozItem

# class MyprojectSpider(scrapy.Spider):
   
#    name = "first"
#    allowed_domains = ["dmoz.org"]
   
#    start_urls = [
#       "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
#       "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
#    ]
#    def parse(self, response):
#       for sel in response.xpath('//ul/li'):
#          item = DmozItem()
#          item['title'] = sel.xpath('a/text()').extract()
#          item['link'] = sel.xpath('a/@href').extract()
#          item['desc'] = sel.xpath('text()').extract()
#          yield item