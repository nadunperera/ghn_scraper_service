ghn_scraper_service
=======

ghn_scraper_service is a collection of scrapers written using selenium. This was done using chromedriver_win32.

### Usage

    edit chrome_path in scrape.py
    edit url in scapy.py
    change spider time.sleep according your preference.
    $ pip install -r requirements.txt
    $ python scrape.py

### Output
    Crawl results will be written in to crawl_results.csv. Pandas will be used to remove duplicates and 
    output will be written in to output.csv.

### Current Scrapers
* Woolworths Online