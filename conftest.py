import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from ui.pages.base_page import BasePage
from ui.pages.vacancy_page import VacancyPage


def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome')
    parser.addoption('--url', default='https://job.ozon.ru/')


@pytest.fixture(scope='session')
def config(request):
    browser = request.config.getoption('--browser')
    url = request.config.getoption('--url')
    return {
        'browser': browser,
        'url': url,
    }


@pytest.fixture()
def driver(config):
    browser = config['browser']
    url = config['url']
    options = Options()
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
    else:
        raise RuntimeError(f'Unsupported browser: "{browser}"')
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def base_page(driver):
    page = BasePage(driver=driver)
    page.choose_location()
    return page


@pytest.fixture
def vacancy_page(driver, base_page):
    page = VacancyPage(driver=driver)
    page.go_to_vacancy_page()
    return page
