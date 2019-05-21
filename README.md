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
    Output will be written into a CSV file on root.

### Current Scrapers
* Woolworths
* JB Hi-Fi

### Todo
* Need to arrange the files and folders properly.
* Need to decide on class and function requirements.