from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class Browser:
    def __init__(self, browser_path):
        self.path = browser_path

    @property
    def driver(self):
        # options_headless = webdriver.ChromeOptions()
        # options_headless.add_argument("headless")
        driver = webdriver.Remote("http://127.0.0.1:4444/wd/hub", DesiredCapabilities.CHROME)
        # driver = webdriver.Chrome(self.path)
        print("Chrome driver initialised.")
        return driver
