from spiders import woolworths

chrome_path = r"C:\Users\nadun\source\repos\ghn_scraper_service\chromedriver_win32\chromedriver.exe"
url = 'https://www.woolworths.com.au/shop/browse/dairy-eggs-fridge/cheese'

woolworths.crawl(chrome_path, url)
