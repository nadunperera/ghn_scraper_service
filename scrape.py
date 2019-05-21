from src.helpers import browser
from src.spiders import start


# scrape_url = "https://www.jbhifi.com.au/computers-tablets/" #put one category url
# for nadun = "https://www.jbhifi.com.au/computers-tablets/storage/?p=1"

# chrome driver
# browse.Browser("http://127.0.0.1:4444/wd/hub")
# browser.chrome_driver

# phantomjs driver
# browse.Browser("http://127.0.0.1", "8910")
# browser.phantomjs_driver

driver = browser.Driver("http://127.0.0.1:4444/wd/hub")

crawler = start.Crawl(driver.chrome, "jbhifi")
crawler.get_categories()
