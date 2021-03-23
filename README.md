## Python based Web Crawler ([HouseofIndya](https://www.houseofindya.com/)) : 

### `Task Performed :` :pencil:
 From list of necklace sets under jewelry scraping the following data -->([Necklace Sets](https://www.houseofindya.com/zyra/necklace-sets/cat))
* Description
* Price 
* Url of Images

### `Prerequisties :` :page_with_curl:
* Python
* Scrapy 

### `Setting up the crawler :` :computer:

* Creating a new directory : 
```
open your command prompt (type cmd in 'search')
mkdir hoi_crawler
cd hoi_crawler
```
* Cloning the git repository in the directory : 
 ```
 git clone -b master https://github.com/SwarajShingote/Scraper_houseofindya.git
 ```
* Changing the current directory to 'Scraper_houseofindya' : 
```
cd Scraper_houseofindya
```
* Installing the required packages :
```
pip install -r requirements.txt
```
* Executing the spider 'HouseofIndya' :
```
scrapy crawl HouseofIndya
```
* Storing the output in json and csv form :
```
scrapy crawl HouseofIndya -t csv -o - >output.csv
scrapy crawl HouseofIndya -o output.csv

scrapy crawl HouseofIndya -t json -o - >output.json
scrapy crawl HouseofIndya -o output.json
```
* Check the output files :
```
output.csv
output.json 
```


