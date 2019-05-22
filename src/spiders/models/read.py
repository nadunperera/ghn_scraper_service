import json


class JsonFile:
    def __init__(self, model):
        self.model = model

    def get_categories(self):
        category_dict = {}
        with open(f"src/spiders/models/{self.model}/categories.json") as json_file:
            category_dict = json.loads(json_file.read())["categories"]
        return category_dict

    def get_paths(self):
        paths_dict = {}
        with open(f"src/spiders/models/{self.model}/paths.json") as json_file:
            paths_dict = json.loads(json_file.read())["paths"]
        return paths_dict
