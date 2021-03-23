## Python based Web Crawler ([HouseofIndya](https://www.houseofindya.com/)) : 

### `Task Performed :` :pencil:
 From list of necklace sets under jewelry scraping the following data -->([Necklace Sets](https://www.houseofindya.com/zyra/necklace-sets/cat))
 
 ![indya](https://user-images.githubusercontent.com/62458537/112197097-b43b3f80-8c31-11eb-9482-d4ecb5384ffe.PNG)

* Description
* Price 
* Url of Images

### `Prerequisties :` :page_with_curl:
* Python(3.7)

### `Setting up the crawler :` :computer:

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
scrapy crawl HouseofIndya -t csv -o raw_data >output.csv
scrapy crawl HouseofIndya -o output.csv

scrapy crawl HouseofIndya -t json -o raw_data >output.json
scrapy crawl HouseofIndya -o output.json
```
* Check the output files :
```
output.csv
output.json 
```