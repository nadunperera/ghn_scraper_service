import time


# i do not know what to do with below. trying to make use of DRY
def get_page(scrape_url, page_number):
    scrape_url = scrape_url + f"?p={page_number}"
    return scrape_url


def get_products(scrape_url, page_number, selector, driver):
    scrape_url_with_page = get_page(scrape_url, page_number)
    driver.get(scrape_url_with_page)
    print(f"Crawling page {scrape_url_with_page}")
    time.sleep(2)
    products = driver.find_elements_by_xpath(selector)
    print(f"{len(products)} products on the page...")
    return products
