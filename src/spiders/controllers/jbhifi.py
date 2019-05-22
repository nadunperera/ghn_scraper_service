import time, csv
from selenium.common.exceptions import NoSuchElementException
from src.spiders.controllers import common


def scrape(category_url, paths_dict, driver):
    page_number = 1
    total_products = 0

    with open("temp_jbhifi_dump.csv", "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["product_name", "price"])

        while True:
            print("Getting standard products on the page...")
            scrape_url_with_page = common.get_page("jbhifi", category_url, page_number)
            products = common.get_products(
                scrape_url_with_page, paths_dict.get("single_product_tile"), driver
            )
            if products:
                for product in products:
                    try:
                        product_name = product.find_element_by_xpath(
                            paths_dict.get("single_product_name")
                        ).text
                        product_price = product.find_element_by_css_selector(
                            paths_dict.get("single_product_dollar")
                        ).text
                        writer.writerow([product_name, product_price])
                    except NoSuchElementException:
                        pass  # skipped if no element found
                total_products = total_products + len(products)
                print(f"Total number of products added to the csv: {total_products}")
                page_number += 1
            else:
                break
