import time

from ui.pages.base_page import BasePage
from ui.locators.locators import VacancyPageLocators
from utils.constants import VACANCY_URL


class VacancyPage(BasePage):
    locators = VacancyPageLocators()
    page_url = VACANCY_URL

    def go_to_vacancy_page(self):
        self.driver.get(self.page_url)

    def filling_candidate_form(self, candidate):
        self.click(self.locators.APPLY_LOCATOR)
        self.send_keys(self.locators.FIRST_NAME_LOCATOR, candidate.first_name)
        self.send_keys(self.locators.LAST_NAME_LOCATOR, candidate.last_name)
        self.send_keys(self.locators.EMAIL_LOCATOR, candidate.email)
        self.send_keys(self.locators.TEL_LOCATOR, candidate.tel)
        self.send_keys(self.locators.RESUME_LINK_LOCATOR, candidate.resume_link)
        self.click(self.locators.CHECK_BOX_LOCATOR)
        self.click(self.locators.SEND_RESUME_LOCATOR)
