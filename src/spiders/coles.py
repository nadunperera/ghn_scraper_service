def crawl(driver, scrape_url):
    print("PRINTING PAGE SOURCE")
    driver.get(scrape_url)
    print(driver.page_source)
    print("END PRINTING PAGE SOURCE")
