from selenium.common.exceptions import StaleElementReferenceException, ElementClickInterceptedException, \
    TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from ui.locators.locators import BasePageLocators
CLICK_RETRY = 5


class BasePage(object):
    locators = BasePageLocators()

    def __init__(self, driver):
        self.driver = driver

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def click(self, locator, timeout=None):
        for i in range(CLICK_RETRY):
            try:
                self.find(locator, timeout=timeout)
                self.wait(timeout).until(EC.element_to_be_clickable(locator)).click()
                return
            except (StaleElementReferenceException, ElementClickInterceptedException, TimeoutException):
                if i == CLICK_RETRY - 1:
                    raise

    def send_keys(self, locator, text, timeout=None):
        elem = self.find(locator, timeout=timeout)
        self.click(locator)
        elem.clear()
        elem.send_keys(text)

    def choose_location(self):
        self.click(self.locators.LOCATION_PICKER_LOCATOR)
        self.click(self.locators.CITY_LOCATOR)
        self.click(self.locators.SAVE_LOCATION_LOCATOR)
