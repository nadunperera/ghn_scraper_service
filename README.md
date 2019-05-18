ghn_scraper_service
=======

ghn_scraper_service is a collection of scrapers written using selenium and python.

### Usage

    For selenium/chrome:
    $ docker run -d -p 4444:4444 selenium/standalone-chrome
    
    For selenium/phantomjs:
    $ docker run -d -p 8910:8910 wernight/phantomjs phantomjs --webdriver=8910

    $ pip install -r requirements.txt
    $ python scrape.py

### Output
    Crawl results will be written in to crawl_results.csv. Pandas will be used to remove duplicates and 
    output will be written in to output.csv.

### Current Scrapers
* Woolworths
* JB Hi-Fi
