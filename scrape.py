from src.spiders import woolworths
from src.helpers import pandas
from src.helpers import chrome

chrome_path = r'src/chromedriver_win32/chromedriver.exe'

# Do not use the url with the page number.
# Make sure it is clean as below. Spider will be adding the pageNumber potion while crawling.
# SAMPLE URLS
# https://www.woolworths.com.au/shop/browse/fruit-veg/fruit
# https://www.woolworths.com.au/shop/browse/drinks/soft-drinks

scrape_url = 'https://www.woolworths.com.au/shop/browse/dairy-eggs-fridge/cheese'

browser = chrome.Browser(chrome_path)

woolworths.crawl(browser.driver, scrape_url)
pandas.distinct()
