import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from base_case import BaseCase
from ui.pages.auth_page import AuthPage
from ui.pages.base_page import BasePage
from ui.pages.cabinet_page import CabinetPage
from ui.pages.welcome_page import WelcomePage
from ui.locators.auth_page_locators import AuthPageLocators

class TestAuth(BaseCase):
    ### Тесты пройдут только в том случае, если у пользователя 
    ### с текущим логином и паролем уже есть кабинет     

    def test_redirect_to_vkid(self, driver):
        base_page = BasePage(driver)
        driver.get(base_page.url)
        cabinet_button = WebDriverWait(driver, 10).until(ec.element_to_be_clickable(AuthPageLocators.NAV_CABINET_BUTTON))
        cabinet_button.click()
        WebDriverWait(driver, 10).until(lambda d: 'id.vk.com' in d.current_url)
        assert 'id.vk.com' in driver.current_url

    def test_successful_auth(self, authorization_page):
        assert authorization_page.wait_for_redirect_to_cabinet()
        