import pytest
from selenium.webdriver.remote.webdriver import WebDriver


class BaseCase:
    driver = None

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver):
        self.driver: WebDriver = driver
