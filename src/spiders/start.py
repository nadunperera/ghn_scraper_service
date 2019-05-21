from src.spiders.controllers import woolworths, jbhifi
from src.helpers import pandas
import json


class Crawl:
    def __init__(self, driver, model):
        self.driver = driver
        self.model_name = model

    def get_categories(self):
        total_categories = 0
        path = self.get_paths()
        with open(f"src/spiders/models/{self.model_name}/slugs.json") as json_file:
            data = json.load(json_file)
            for category in data["categories"]:
                category_url = path["start_url"] + category["url"]
                print(self.model_name + " category URL is " + category_url)
                if self.model_name is "woolworths":
                    woolworths.scrape(category_url, path, self.driver)
                    # distinct results, create final output file
                    pandas.distinct(self.model_name, category["url"])
                elif self.model_name is "jbhifi":
                    jbhifi.scrape(category_url, path, self.driver)
                    # distinct results, create final output file
                    pandas.distinct(self.model_name, category["name"])
                total_categories += 1
        print(
            "Number of categories crawled in "
            + self.model_name
            + ": "
            + str(total_categories)
        )

    def get_paths(self):
        with open(f"src/spiders/models/{self.model_name}/paths.json") as json_file:
            data = json.load(json_file)
            for path in data["paths"]:
                print(self.model_name + " start URL is " + path["startUrl"])
                output = {}
                output["start_url"] = path["startUrl"]
                output["single_products_selector"] = path["singleProductsXpath"]
                output["single_product_name"] = path["singleProductName"]
                output["single_product_dollar"] = path["singleProductDollar"]
                if self.model_name is "woolworths":
                    output["single_product_cents"] = path["singleProductCents"]
                    output["bundle_product_selector"] = path["bundleProductsXpath"]
                    output["bundle_product_title"] = path["bundleProductTitle"]
                    output["bundle_product_names"] = path["bundleProductNames"]
                    output["bundle_product_prices"] = path["bundleProductPrices"]
                return output
