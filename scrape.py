from src.spiders import woolworths, jbhifi
from src.helpers import pandas, chrome

chrome_path = r'src/chromedriver_win32/chromedriver.exe'

# Do not use the url with the page number.
# Make sure it is clean as below. Spider will be adding the pageNumber potion while crawling.
# SAMPLE URLS
# https://www.woolworths.com.au/shop/browse/fruit-veg/fruit
# https://www.woolworths.com.au/shop/browse/drinks/soft-drinks

scrape_url = 'https://www.woolworths.com.au/shop/browse/dairy-eggs-fridge/cheese'
# scrape_url = 'https://www.jbhifi.com.au/computers-tablets/' #put one category url

# setting up the browser
browser = chrome.Browser(chrome_path)

# do the crawl
jbhifi.crawl(browser.driver, scrape_url)
# woolworths.crawl(browser.driver, scrape_url)

# distinct results
pandas.distinct()
