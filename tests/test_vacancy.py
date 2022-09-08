import pytest
from base import BaseCase
from utils.constants import CandidateInfo


class TestVacancy(BaseCase):
    def test_sent_correct_resume(self, vacancy_page):
        vacancy_page.filling_candidate_form(CandidateInfo)
        assert vacancy_page.find(vacancy_page.locators.SUCCESS_MESSAGE_LOCATOR)
