import time, csv
from selenium.common.exceptions import NoSuchElementException
from src.spiders.controllers import common


def scrape(category_url, paths_dict, driver):
    page_number = 1
    total_products = 0

    # output to a file
    with open("temp_woolworths_dump.csv", "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["product_name", "price"])

        while True:
            # getting single products on the page
            print("Getting single products on the page...")
            scrape_url_with_page = common.get_page(
                "woolworths", category_url, page_number
            )
            single_products = common.get_products(
                scrape_url_with_page, paths_dict.get("single_product_tile"), driver
            )
            if single_products:
                for single_product in single_products:
                    product_name = single_product.find_element_by_class_name(
                        paths_dict.get("single_product_name")
                    ).text
                    try:
                        # getting dollars and cents and connecting together with a dot
                        price = (
                            single_product.find_element_by_class_name(
                                paths_dict.get("single_product_dollar")
                            ).text
                            + "."
                            + single_product.find_element_by_class_name(
                                paths_dict.get("single_product_cents")
                            ).text
                        )
                        writer.writerow([product_name, price])
                    except NoSuchElementException:
                        writer.writerow([product_name, "check_stock"])
                total_products = total_products + len(single_products)
                print(f"Total number of products added to the csv: {total_products}")

                # getting bundle products on the same page
                print("Getting bundle products on the page...")
                scrape_url_with_page = common.get_page(
                    "woolworths", category_url, page_number
                )
                bundle_products = common.get_products(
                    scrape_url_with_page, paths_dict.get("bundle_product_tile"), driver
                )
                if bundle_products:
                    for bundle_product in bundle_products:
                        try:
                            bundle_product_title = bundle_product.find_element_by_class_name(
                                paths_dict.get("bundle_product_title")
                            ).text
                            bundle_product_names = bundle_product.find_elements_by_class_name(
                                paths_dict.get("bundle_product_names")
                            )
                            bundle_product_prices = bundle_product.find_elements_by_class_name(
                                paths_dict.get("bundle_product_prices")
                            )
                            bundle_product_price_index = 0

                            for bundle_product_name in bundle_product_names:
                                bundle_product_full_name = (
                                    bundle_product_title
                                    + " "
                                    + bundle_product_name.text
                                )
                                bundle_product_price = bundle_product_prices[
                                    bundle_product_price_index
                                ].text
                                # checking whether 1 or more items are out of stock from the bundle
                                if len(bundle_product_names) is len(
                                    bundle_product_prices
                                ):
                                    writer.writerow(
                                        [bundle_product_full_name, bundle_product_price]
                                    )
                                    bundle_product_price_index += 1
                                else:
                                    # if out of stock, just write the product name, don't worry about the price
                                    writer.writerow(
                                        [bundle_product_full_name, "check_stock"]
                                    )
                                    continue

                            total_products = total_products + len(bundle_product_names)
                            print(
                                f"Total number of products added to the csv: {total_products}"
                            )
                        except NoSuchElementException:
                            print("Cannot file specifed bundle element, skipping...")
                page_number += 1
            else:
                break
