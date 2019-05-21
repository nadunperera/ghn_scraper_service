import time, csv
from selenium.common.exceptions import NoSuchElementException


def scrape(category_url, selector, driver):
    page_number = 1
    total_products = 0

    with open("temp_jbhifi_dump.csv", "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["product_name", "price"])

        while True:
            print("Getting standard products on the page...")
            products = get_products(
                category_url, page_number, selector["single_products_selector"], driver
            )
            if products:
                for product in products:
                    try:
                        product_name = product.find_element_by_xpath(
                            selector["single_product_name"]
                        ).text
                        product_price = product.find_element_by_css_selector(
                            selector["single_product_dollar"]
                        ).text
                        writer.writerow([product_name, product_price])
                    except NoSuchElementException:
                        pass # skipped if no element found
                total_products = total_products + len(products)
                print(f"Total number of products added to the csv: {total_products}")
                page_number += 1
            else:
                break


def get_next_page(scrape_url, page_number):
    scrape_url = scrape_url + f"?p={page_number}"
    return scrape_url


def get_products(scrape_url, page_number, selector, driver):
    scrape_url_with_page = get_next_page(scrape_url, page_number)
    driver.get(scrape_url_with_page)
    print(f"Crawling page {scrape_url_with_page}")
    time.sleep(2)
    products = driver.find_elements_by_xpath(selector)
    print(f"{len(products)} products on the page...")
    return products
