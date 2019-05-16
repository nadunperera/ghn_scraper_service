from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class Browser:
    @property
    def driver(self):
        driver = webdriver.Remote(
            "http://127.0.0.1:4444/wd/hub", DesiredCapabilities.CHROME
        )
        print("Chrome driver initialised.")
        return driver
