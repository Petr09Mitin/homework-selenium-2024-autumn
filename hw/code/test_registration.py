import pytest
from ui.pages.registration_page import RegistrationPage
from ui.pages.welcome_page import WelcomePage
from ui.pages.base_page import BasePage
from base_case import BaseCase
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ui.locators.auth_page_locators import AuthPageLocators
from ui.locators.welcome_page_locators import WelcomePageLocators

class TestRegistration(BaseCase):
    # def test_redirect_to_vkid(self, driver): ## Под вопросом
    #     base_page = BasePage(driver)
    #     driver.get(base_page.url)
    #     assert 'id.vk.com' in driver.current_url

    # def test_welcome_page_after_auth(self, wp):
    #     welcome_page = WelcomePage(wp.driver)
    #     assert welcome_page.is_welcome_header_visible()
        
    # def test_language_switcher(self, wp):
    #     welcome_page = WelcomePage(wp.driver)
    #     welcome_page.switch_language('en')
    #     assert welcome_page.get_create_cabinet_button_text() == "Create a new account"
    #     welcome_page.switch_language('ru')
    #     assert welcome_page.get_create_cabinet_button_text() == "Создать новый кабинет"

    def test_redirect_to_vkid(self, driver):
        base_page = BasePage(driver)
        driver.get(base_page.url)
        cabinet_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(AuthPageLocators.NAV_CABINET_BUTTON)
        )
        cabinet_button.click()
        WebDriverWait(driver, 10).until(
            lambda d: 'id.vk.com' in d.current_url
        )
        assert 'id.vk.com' in driver.current_url

    def test_welcome_page_after_auth(self, wp):
        WebDriverWait(wp.driver, 10).until(
            EC.presence_of_element_located(WelcomePageLocators.WELCOME_HEADER)
        )
        assert wp.is_welcome_header_visible()
        
    def test_language_switcher(self, wp):
        WebDriverWait(wp.driver, 10).until(
            EC.presence_of_element_located(WelcomePageLocators.LANGUAGE_SWITCHER)
        )
        wp.switch_language('en')
        WebDriverWait(wp.driver, 10).until(
            lambda d: wp.get_create_cabinet_button_text() == "Create a new account"
        )
        assert wp.get_create_cabinet_button_text() == "Create a new account"
        wp.switch_language('ru')
        WebDriverWait(wp.driver, 10).until(
            lambda d: wp.get_create_cabinet_button_text() == "Создать новый кабинет"
        )
        assert wp.get_create_cabinet_button_text() == "Создать новый кабинет"

    # def test_registration_form_required_fields(self, wp):
    #     welcome_page = WelcomePage(wp.driver)
    #     welcome_page.click_create_cabinet()
    #     reg_page = RegistrationPage(wp.driver)
    #     assert reg_page.is_registration_page()
        
    #     assert reg_page.is_advertiser_type_visible()
    #     assert reg_page.is_agency_type_visible()
    #     assert reg_page.is_country_selector_visible()
    #     assert reg_page.is_currency_selector_visible()
    #     assert reg_page.is_email_field_visible() 
    #     assert reg_page.is_individual_type_visible()
    #     assert reg_page.is_company_type_visible()
    #     assert reg_page.is_inn_field_visible()
    #     assert reg_page.is_full_name_field_visible()
    #     assert reg_page.is_terms_checkbox_visible()
    #     assert reg_page.is_mailing_checkbox_visible()

        # Проверка 3х сценариев выбора типов аккаунта: 
        # Агенство; Рекламодатель + Юр. лицо; Рекламодатель + Физ. лицо
        # # reg_page.select_agency_type()
        # # assert not reg_page.is_individual_type_visible()
        # # assert not reg_page.is_full_name_field_visible()
        # # assert not reg_page.is_inn_field_visible()

        # # reg_page.select_advertiser_type()
        # # reg_page.select_company_type()
        # # assert reg_page.is_individual_type_visible()
        # # assert not reg_page.is_full_name_field_visible()
        # # assert not reg_page.is_inn_field_visible()

        # # reg_page.select_individual_type()
        # # assert reg_page.is_individual_type_visible()
        # # assert reg_page.is_full_name_field_visible()
        # # assert reg_page.is_inn_field_visible()

    # def test_advertiser_account_type(self, auth_page):
    #     welcome_page = WelcomePage(auth_page.driver)
    #     welcome_page.click_create_cabinet()
    #     reg_page = RegistrationPage(auth_page.driver)
    #     reg_page.select_agency_type()

    #     reg_page.select_advertiser_type()
    #     reg_page.select_company_type()
    #     assert reg_page.is_individual_type_visible()
    #     assert not reg_page.is_full_name_field_visible()
    #     assert not reg_page.is_inn_field_visible()

    #     reg_page.select_individual_type()
    #     assert reg_page.is_individual_type_visible()
    #     assert reg_page.is_full_name_field_visible()
    #     assert reg_page.is_inn_field_visible()

    # def test_agency_account_type(self, auth_page):
    #     welcome_page = WelcomePage(auth_page.driver)
    #     welcome_page.click_create_cabinet()
    #     reg_page = RegistrationPage(auth_page.driver)
    #     reg_page.select_agency_type()
    #     # Проверяем, что доступен только тип "Юридическое лицо"
    #     assert reg_page.is_company_type_selected()
    #     assert not reg_page.is_individual_type_visible()
    #     # Проверяем, что поля для физлиц не отображаются
    #     assert not reg_page.is_inn_field_visible()
    #     assert not reg_page.is_full_name_field_visible()

    # def test_checkboxes_default_state(self, auth_page):
    #     welcome_page = WelcomePage(auth_page.driver)
    #     welcome_page.click_create_cabinet()
    #     reg_page = RegistrationPage(auth_page.driver)
    #     # По умолчанию оба чекбокса должны быть отмечены
    #     assert reg_page.get_terms_checkbox_state() is True
    #     assert reg_page.get_mailing_checkbox_state() is True

    # def test_terms_checkbox_required(self, auth_page):
    #     welcome_page = WelcomePage(auth_page.driver)
    #     welcome_page.click_create_cabinet()
    #     reg_page = RegistrationPage(auth_page.driver)
    #     # Снимаем галочку с обязательного чекбокса
    #     reg_page.toggle_terms_checkbox()
    #     assert reg_page.get_terms_checkbox_state() is False
    #     # Пытаемся создать кабинет
    #     reg_page.fill_required_fields()
    #     reg_page.click_create_cabinet()
    #     # Должна появиться ошибка "Обязательное поле"
    #     assert reg_page.is_requires_field_error_visible()

    # def test_mailing_checkbox_optional(self, auth_page):
    #     welcome_page = WelcomePage(auth_page.driver)
    #     welcome_page.click_create_cabinet()
    #     reg_page = RegistrationPage(auth_page.driver)
    #     # Снимаем галочку с необязательного чекбокса
    #     reg_page.toggle_mailing_checkbox()
    #     assert reg_page.get_mailing_checkbox_state() is False
    #     # Заполняем все обязательные поля валидными данными и создаем кабинет
    #     reg_page.fill_required_fields()
    #     reg_page.click_create_cabinet()
    #     assert reg_page.wait_for_redirect_to_cabinet()

    # def test_successful_registration(self, auth_page):
    #     welcome_page = WelcomePage(auth_page.driver)
    #     welcome_page.click_create_cabinet()
    #     reg_page = RegistrationPage(auth_page.driver)
    #     reg_page.fill_required_fields()
    #     reg_page.click_create_cabinet()
    #     assert reg_page.wait_for_redirect_to_cabinet()
