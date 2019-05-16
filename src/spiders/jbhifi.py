import time
import csv

from selenium.common.exceptions import NoSuchElementException


def crawl(driver, scrape_url):
    category_urls = get_category_details(scrape_url, driver)

    # output to a file
    with open('crawl_results.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Product Name', 'Price'])

        for category_url in category_urls:
            total_products = 0
            page_number = 1
            products = get_product_details(category_url, page_number, driver)
            for product in products:
                try:
                    writer.writerow([product.find_element_by_tag_name('h4').text,
                                     product.find_element_by_class_name('price').text])
                except NoSuchElementException:
                    pass  # passing if unable to locate above elements

            total_products = total_products + len(products)
            page_number = page_number + 1
            products = get_product_details(category_url, page_number, driver)

            if not products:
                page_number = 0
                print(f'Total number of  category products crawled: {total_products}')
                break


def get_next_page(scrape_url, page_number):
    scrape_url = scrape_url + f'?p={page_number}'
    return scrape_url


def get_category_details(scrape_url, driver):
    driver.get(scrape_url)
    time.sleep(2)
    categories = driver.find_element_by_class_name('category-menu')
    category_urls = []
    for li in categories.find_elements_by_tag_name("li"):
        try:
            url = li.find_element_by_tag_name('a').get_attribute('href')
            if url[-1] != '#':
                category_urls.append( url)
        except NoSuchElementException:
            pass  # passing if unable to locate above elements
    return category_urls


def get_product_details(scrape_url, page_number, driver):
    scrape_url_with_page = get_next_page(scrape_url, page_number)
    driver.get(scrape_url_with_page)
    print(f'Crawling: {scrape_url_with_page}')
    time.sleep(2)
    products = driver.find_elements_by_class_name('product-tile')
    print(f'Found {len(products)} products.')
    return products
