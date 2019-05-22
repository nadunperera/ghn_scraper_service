from src.helpers import browser
from src.spiders import start

# chrome driver
# browse.Browser("http://127.0.0.1:4444/wd/hub")
# browser.chrome_driver

# phantomjs driver
# browse.Browser("http://127.0.0.1", "8910")
# browser.phantomjs_driver

driver = browser.Driver("http://127.0.0.1:4444/wd/hub")

start.crawl(driver.chrome, "woolworths")
