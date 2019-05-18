from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class Driver:
    def __init__(self, address, port=None):
        self.browser_address = address
        self.browser_port = port

    @property
    def chrome(self):
        # "http://127.0.0.1:4444/wd/hub", DesiredCapabilities.CHROME,
        if self.browser_port:
            driver = webdriver.Remote(
                f"{self.browser_address}:{self.browser_port}",
                DesiredCapabilities.CHROME,
            )
        else:
            driver = webdriver.Remote(
                f"{self.browser_address}", DesiredCapabilities.CHROME
            )
        print("Chrome driver initialised.")
        return driver

    @property
    def phantomjs(self):
        # command_executor="http://127.0.0.1:8910",
        if self.browser_port:
            driver = webdriver.Remote(
                command_executor=f"{self.browser_address}:{self.browser_port}",
                desired_capabilities=DesiredCapabilities.PHANTOMJS,
            )
        else:
            driver = webdriver.Remote(
                command_executor=f"{self.browser_address}",
                desired_capabilities=DesiredCapabilities.PHANTOMJS,
            )
        print("PhantomJS driver initialised.")
        return driver
