import time, csv
from selenium.common.exceptions import NoSuchElementException


def scrape(category_url, driver):
    page_number = 1
    products = get_products(category_url, page_number, driver)
    total_products = 0

    # output to a file
    with open("crawl_results.csv", "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["product_name", "price"])

        while products:
            for product in products:
                try:
                    writer.writerow(
                        [
                            product.find_element_by_class_name(
                                "shelfProductTile-descriptionLink"
                            ).text,
                            f"{product.find_element_by_class_name('price-dollars').text}.{product.find_element_by_class_name('price-centsPer').text}",
                        ]
                    )
                except NoSuchElementException:
                    pass  # skip if no element found
            total_products = total_products + len(products)
            print(f"Total number of products added to the csv: {total_products}")
            page_number = page_number + 1
            products = get_products(category_url, page_number, driver)


def get_next_page(scrape_url, page_number):
    scrape_url = scrape_url + f"?pageNumber={page_number}"
    return scrape_url


def get_products(scrape_url, page_number, driver):
    scrape_url_with_page = get_next_page(scrape_url, page_number)
    driver.get(scrape_url_with_page)
    print(f"Crawling page {scrape_url_with_page}")
    time.sleep(2)
    products = driver.find_elements_by_xpath(
        "//wow-tile/div/wow-shelf-product-tile"
    )
    bundle_tile_products = driver.find_elements_by_xpath(
        "//wow-tile/div/wow-shelf-bundle-tile"
    )
    print(f"{len(products)} products on the page.")
    return products
