# third_assginment-of-web-scrapying
Use python spider web scrapping website automatically and get a clear json format

#Assignment Requirment

In this third assignment you will:

Scrape this website: http://quotes.toscrape.com

From each page you have to scrape: The quote;The author;The tags

##Project requirements - PART 1 -:

1. Initiate a new Scrapy project and call it: third_assignment

2. Create a new spider class called QuotesToScrapeSpider

3. Your spider should be named: quotes

4. Build the parse method, just a regular one and yield all the fields

5. Follow the links in pagination

6. Execute your spider and save the items in a JSON file

7. Notice that for each quote we have these unicode characters (\u201c, \u201d) which refers to the opening and closing quotation marks.
   Now by default for all other item exporters like CSV, Scrapy by default uses utf-8 encoding 
   and this is why in CSV files you don't see uninterpreted unicode characters like in JSON files (\u201c, \u201d) 
   so your job is to go through this link from Scrapy's documentation
   and figure out how you can force Scrapy to use UTF-8 encoding.

##Project Requirements - PART 2 - :

Now this your job is to build:

1. An item class called: QuotesItem
2. Create 3 fields(quote, author, tags) and use input and output processors (Make sure to join the tags by ";")
3. Now in your spider class load your item class (QuotesItem) and assign values to all the fields.
