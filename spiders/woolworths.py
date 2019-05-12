from selenium import webdriver
import time
import csv

from selenium.common.exceptions import NoSuchElementException


def crawl(chrome_path, url):
    options_headless = webdriver.ChromeOptions()
    options_headless.add_argument('headless')
    driver = webdriver.Chrome(chrome_path, options=options_headless)

    page_number = 1
    products = get_product_details(url, 1, driver)
    total_products = products
    print(f'Total number of products crawled: {len(total_products)}')

    # output to a file
    with open('crawl_results.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Product Name', 'Price'])

        while products:
            page_number = page_number + 1
            products = get_product_details(url, page_number, driver)

            # write to the file whatever you get from crawling
            for product in products:
                try:
                    writer.writerow([product.find_element_by_class_name('shelfProductTile-descriptionLink').text, f"{product.find_element_by_class_name('price-dollars').text}.{product.find_element_by_class_name('price-centsPer').text}"])
                except NoSuchElementException:
                    pass  # passing if unable to locate above elements

            total_products = total_products + products
            print(f'Total number of products crawled: {len(total_products)}')
            if not products:
                break


def get_next_page(url=None, page_number=None):
    url = url + f'?pageNumber={page_number}'
    return url


def get_product_details(url=None, page_number=None, driver=None):
    url_with_page = get_next_page(url, page_number)
    driver.get(url_with_page)
    print(f'Crawling: {url_with_page}')
    time.sleep(2)
    products = driver.find_elements_by_class_name('shelfProductTile')
    print(f'Found {len(products)} products.')
    return products
