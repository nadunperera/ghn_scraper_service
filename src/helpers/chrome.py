from selenium import webdriver


class Browser:

    def __init__(self, browser_path):
        self.path = browser_path

    @property
    def driver(self):
        options_headless = webdriver.ChromeOptions()
        options_headless.add_argument('headless')
        driver = webdriver.Chrome(self.path)
        print('Chrome driver initialised.')
        return driver
