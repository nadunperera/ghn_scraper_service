from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class Browser:
    @property
    def chrome_driver(self):
        driver = webdriver.Remote(
            "http://127.0.0.1:4444/wd/hub", DesiredCapabilities.CHROME,
        )
        print("Chrome driver initialised.")
        return driver

    @property
    def phantomjs_driver(self):
        driver = webdriver.Remote(
            command_executor="http://127.0.0.1:8910",
            desired_capabilities=DesiredCapabilities.PHANTOMJS,
        )
        print("PhantomJS driver initialised.")
        return driver
