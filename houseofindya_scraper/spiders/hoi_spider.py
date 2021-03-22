import scrapy  

class spider_hoi(scrapy.Spider):  

  """ name : unique name for the spider 
      allowed_domains : base url for spider to crawl
      start_urls : list of urls where spider starts crawling """ 

  name = "HouseofIndya"
  allowed_domains = ["https://www.houseofindya.com"]
  start_urls = [ 
     "https://www.houseofindya.com/zyra/necklace-sets/cat" 
  ]
   
  # function extracts and parses the scraped data"""
  def parse(self, response):
     
     # selector_1 : for extracting the productlist 
     selector_1 = response.css('#JsonProductList')

     # selector_2 : for extracting the li tags
     selector_2 = selector_1.css('li')

     # base url for images  
     base_url_img = 'https://img.faballey.com/Images/Product/'
     
     # Iterating over all the li tags
     for sel in selector_2 :

         # desc : scraping the description using 'data-name' attribute
         desc = sel.attrib['data-name']

         # price : scraping the price(converting to float) using 'data-price' attribute
         price = float(sel.attrib['data-price'])
         
         # data-id : scraping the id for each image using 'data-id' attribute
         data_id = sel.attrib['data-id']

         # url : creating the url for images using base url and id of each image
         url = base_url_img + data_id + '/1.jpg'

         # returing the descriptions, prices and urls of necklace-sets  
         yield {
            'desc' : desc ,
            'price' : price,
            'url' : url,
         }  