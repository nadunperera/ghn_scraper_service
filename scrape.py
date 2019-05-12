from spiders import woolworths
from helper import pandas

chrome_path = r'C:\Users\nadun\source\repos\ghn_scraper_service\chromedriver_win32\chromedriver.exe'

# Do not use the url with the page number.
# Make sure it is clean as below. Spider will be adding the pageNumber potion while crawling.
# SAMPLE URLS
# https://www.woolworths.com.au/shop/browse/fruit-veg/fruit
# https://www.woolworths.com.au/shop/browse/drinks/soft-drinks

url = 'https://www.woolworths.com.au/shop/browse/dairy-eggs-fridge/cheese'

woolworths.crawl(chrome_path, url)
pandas.distinct()
