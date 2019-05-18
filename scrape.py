from src.spiders import woolworths, jbhifi, coles
from src.helpers import pandas, browse

# Do not use the url with the page number.
# Make sure it is clean as below. Spider will be adding the pageNumber potion while crawling.
# SAMPLE URLS
# https://www.woolworths.com.au/shop/browse/fruit-veg/fruit
# https://www.woolworths.com.au/shop/browse/drinks/soft-drinks

scrape_url = "https://www.woolworths.com.au/shop/browse/dairy-eggs-fridge/cheese"
# scrape_url = "https://www.jbhifi.com.au/computers-tablets/" #put one category url
# scrape_url = "https://shop.coles.com.au/a/a-national/everything/browse/entertaining-at-home/cheese-board-selections?pageNumber=1"

# select the browser driver to use
# chrome_driver for chrome
# phantomjs_driver for phantomjs
browser = browse.Browser()

# do the crawl
# jbhifi.crawl(browser.chrome_driver, scrape_url)
woolworths.crawl(browser.chrome_driver, scrape_url)
# coles.crawl(browser.chrome_driver, scrape_url)

# distinct results
pandas.distinct()
