from selenium.webdriver.common.by import By


class BasePageLocators:
    LOCATION_PICKER_LOCATOR = (By.XPATH, "//input[@placeholder='Город']")
    CITY_LOCATOR = (By.XPATH, "//div[@class='select__list']//span[contains(text(), 'Санкт-Петербург')]")
    SAVE_LOCATION_LOCATOR = (By.XPATH, "//button[contains(text(), 'Сохранить')]")


class VacancyPageLocators(BasePageLocators):
    APPLY_LOCATOR = (By.XPATH, "//button[contains(@class, 'vacancy__actions__apply')]")
    FIRST_NAME_LOCATOR = (By.XPATH, "//input[@name='fname']")
    LAST_NAME_LOCATOR = (By.XPATH, "//input[@name='lname']")
    EMAIL_LOCATOR = (By.XPATH, "//input[@name='email']")
    TEL_LOCATOR = (By.XPATH, "//input[@type='tel']")
    RESUME_LINK_LOCATOR = (By.XPATH, "//input[@placeholder='Ссылка на резюме']")
    CHECK_BOX_LOCATOR = (By.XPATH, "//div[contains(@class, 'checkbox')]")
    SEND_RESUME_LOCATOR = (By.XPATH, "//button[contains(@class, 'confirm')]")
    SUCCESS_MESSAGE_LOCATOR = (By.XPATH, "//p[contains(text(), 'Ваш отклик отправлен')]")
