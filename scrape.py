from src.spiders import woolworths, jbhifi, coles
from src.helpers import pandas, browse
import json

# Do not use the url with the page number.
# Make sure it is clean as below. Spider will be adding the pageNumber potion while crawling.
# SAMPLE URLS
# https://www.woolworths.com.au/shop/browse/fruit-veg/fruit
# https://www.woolworths.com.au/shop/browse/drinks/soft-drinks

with open("src/data/woolworths/urls.json") as json_file:
    data = json.load(json_file)
    for url in data["urls"]:
        print("Woolworths start URL is " + url["startUrl"])
        start_url = url["startUrl"]

total_categories = 0
with open("src/data/woolworths/slugs.json") as json_file:
    data = json.load(json_file)
    for category in data["categories"]:
        print("Woolworths category URL is " + start_url + category["name"])
        total_categories += 1
print(f"Total number of Woolworths categories: {total_categories}")

# scrape_url = "https://www.woolworths.com.au/shop/browse/dairy-eggs-fridge/cheese"
# scrape_url = "https://www.jbhifi.com.au/computers-tablets/" #put one category url
# scrape_url = "https://shop.coles.com.au/a/a-national/everything/browse/entertaining-at-home/cheese-board-selections?pageNumber=1"

# select the browser driver to use
# chrome_driver for chrome
# phantomjs_driver for phantomjs
# browser = browse.Browser()

# do the crawl
# jbhifi.crawl(browser.chrome_driver, scrape_url)
# woolworths.crawl(browser.chrome_driver, scrape_url)
# coles.crawl(browser.chrome_driver, scrape_url)

# distinct results
# pandas.distinct()
