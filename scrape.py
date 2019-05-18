from src.helpers import pandas, browser
from src.spiders import start


# scrape_url = "https://www.jbhifi.com.au/computers-tablets/" #put one category url

# chrome driver
# browse.Browser("http://127.0.0.1:4444/wd/hub")
# browser.chrome_driver

# phantomjs driver
# browse.Browser("http://127.0.0.1", "8910")
# browser.phantomjs_driver

driver = browser.Driver("http://127.0.0.1:4444/wd/hub")

crawler = start.Crawl(driver.chrome, "woolworths")
crawler.get_categories()

# do the crawl
# jbhifi.crawl(browser.chrome_driver, scrape_url)
# woolworths.crawl(browser.chrome_driver, scrape_url)
# coles.crawl(browser.chrome_driver, scrape_url)

# distinct results
pandas.distinct()
