from src.spiders.controllers import woolworths
import json


class Crawl:
    def __init__(self, driver, model):
        self.driver = driver
        self.model_name = model

    def get_categories(self):
        total_categories = 0
        start_url = self.get_start_url()
        with open(f"src/spiders/models/{self.model_name}/slugs.json") as json_file:
            data = json.load(json_file)
            for category in data["categories"]:
                category_url = start_url + category["name"]
                print(self.model_name + " category URL is " + category_url)
                woolworths.scrape(category_url, self.driver)
                total_categories += 1
        print(
            "Number of categories crawled in "
            + self.model_name
            + ": "
            + str(total_categories)
        )

    def get_start_url(self):
        with open(f"src/spiders/models/{self.model_name}/paths.json") as json_file:
            data = json.load(json_file)
            for url in data["path"]:
                print(self.model_name + " start URL is " + url["startUrl"])
                start_url = url["startUrl"]
                return start_url
