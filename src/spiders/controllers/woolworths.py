import time, csv
from selenium.common.exceptions import NoSuchElementException


def scrape(category_url, xpath, driver):
    page_number = 1
    total_products = 0

    # output to a file
    with open("temp_dump.csv", "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["product_name", "price"])

        while True:
            # getting single products on the page
            print("Getting single products on the page...")
            single_products = get_products(
                category_url, page_number, xpath["single_product_xpath"], driver
            )
            if single_products:
                for single_product in single_products:
                    try:
                        product_name = single_product.find_element_by_class_name(
                            xpath["single_product_name"]
                        ).text
                        # getting dollars and cents and connecting together with a dot
                        price = (
                            single_product.find_element_by_class_name(
                                xpath["single_product_dollar"]
                            ).text
                            + "."
                            + single_product.find_element_by_class_name(
                                xpath["single_product_cents"]
                            ).text
                        )
                        writer.writerow([product_name, price])
                    except NoSuchElementException:
                        print("Cannot file specifed element, skipping...")
                total_products = total_products + len(single_products)
                print(f"Total number of products added to the csv: {total_products}")

                # getting bundle products on the same page
                print("Getting bundle products on the page...")
                bundle_products = get_products(
                    category_url, page_number, xpath["bundle_product_xpath"], driver
                )
                if bundle_products:
                    for bundle_product in bundle_products:
                        try:
                            bundle_product_title = bundle_product.find_element_by_class_name(
                                xpath["bundle_product_title"]
                            ).text
                            bundle_product_names = bundle_product.find_elements_by_class_name(
                                xpath["bundle_product_names"]
                            )
                            bundle_product_prices = bundle_product.find_elements_by_class_name(
                                xpath["bundle_product_prices"]
                            )
                            bundle_product_price_index = 0

                            for bundle_product_name in bundle_product_names:
                                try:
                                    bundle_product_full_name = (
                                        bundle_product_title + " " + bundle_product_name.text
                                    )
                                    bundle_product_price = bundle_product_prices[
                                        bundle_product_price_index
                                    ].text
                                    bundle_product_price_index += 1
                                    writer.writerow(
                                        [bundle_product_full_name, bundle_product_price]
                                    )
                                except IndexError:
                                    print("Out of stock product, skipping...")
                            total_products = total_products + len(bundle_product_names)
                            print(
                                f"Total number of products added to the csv: {total_products}"
                            )
                        except NoSuchElementException:
                            print("Cannot file specifed bundle element, skipping...")
                page_number += 1
            else:
                break

def get_next_page(scrape_url, page_number):
    scrape_url = scrape_url + f"?pageNumber={page_number}"
    return scrape_url


def get_products(scrape_url, page_number, xpath, driver):
    scrape_url_with_page = get_next_page(scrape_url, page_number)
    driver.get(scrape_url_with_page)
    print(f"Crawling page {scrape_url_with_page}")
    time.sleep(2)
    products = driver.find_elements_by_xpath(xpath)
    print(f"{len(products)} products on the page.")
    return products
