from src.spiders.models import read
from src.spiders.controllers import woolworths, jbhifi
from src.helpers import pandas


def crawl(driver, model):
    total_categories = 0
    crawler = read.JsonFile(model)

    paths_dict = crawler.get_paths()
    category_dict = crawler.get_categories()

    for category in category_dict:
        category_url = paths_dict[0].get("start_url") + category.get("url")
        if model is "woolworths":
            woolworths.scrape(category_url, paths_dict[0], driver)
            pandas.distinct(model, category.get("url"))
        elif model is "jbhifi":
            jbhifi.scrape(category_url, paths_dict[0], driver)
            pandas.distinct(model, category.get("name"))
        total_categories += 1

    print(f"Number of categories crawled in {model}: {total_categories}")
