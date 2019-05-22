import time


def get_page(model, scrape_url, page_number):
    if model is "woolworths":
        scrape_url = scrape_url + f"?pageNumber={page_number}"
    elif model is "jbhifi":
        scrape_url = scrape_url + f"?p={page_number}"
    return scrape_url


def get_products(scrape_url_with_page, selector, driver):
    driver.get(scrape_url_with_page)
    print(f"Crawling page {scrape_url_with_page}")
    time.sleep(2)
    products = driver.find_elements_by_xpath(selector)
    print(f"{len(products)} products on the page...")
    return products
