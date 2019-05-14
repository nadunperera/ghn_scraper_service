import time
import csv

from selenium.common.exceptions import NoSuchElementException


def crawl(driver, scrape_url):

    page_number = 1
    total_products = 0
    products = get_product_details(scrape_url, 1, driver)

    # output to a file
    with open('crawl_results.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Product Name', 'Price'])

        while products:
            # write to the file whatever you get from crawling
            for product in products:
                try:
                    writer.writerow([product.find_element_by_tag_name('h4').text,
                                     product.find_element_by_class_name('price').text])
                except NoSuchElementException:
                    pass  # passing if unable to locate above elements

            total_products = total_products + len(products)
            page_number = page_number + 1
            products = get_product_details(scrape_url, page_number, driver)

            if not products:
                print(f'Total number of products crawled: {total_products}')
                break


def get_next_page(scrape_url, page_number):
    scrape_url = scrape_url + f'?p={page_number}'
    return scrape_url


def get_product_details(scrape_url, page_number, driver):
    scrape_url_with_page = get_next_page(scrape_url, page_number)
    driver.get(scrape_url_with_page)
    print(f'Crawling: {scrape_url_with_page}')
    time.sleep(2)
    products = driver.find_elements_by_class_name('product-tile')
    print(f'Found {len(products)} products.')
    return products
