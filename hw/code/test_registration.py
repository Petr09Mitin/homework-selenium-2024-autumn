import pytest, time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from ui.locators.auth_page_locators import AuthPageLocators
from ui.locators.welcome_page_locators import WelcomePageLocators
from ui.pages.registration_page import RegistrationPage
from ui.pages.welcome_page import WelcomePage
from ui.pages.base_page import BasePage
from base_case import BaseCase

class TestRegistration(BaseCase):
    ### Тесты пройдут только в том случае, если у пользователя 
    ### с текущим логином и паролем еще нет кабинета

    error_required_field = "Обязательное поле"
    error_invalid_email = "Некорректный email адрес"   
    error_max_length = "Напишите текст не больше 60 символов"
    error_invalid_chars = "Некорректные символы. Разрешена только кириллица дефис и пробел"

    def test_redirect_to_vkid(self, driver):
        base_page = BasePage(driver)
        driver.get(base_page.url)
        cabinet_button = WebDriverWait(driver, 10).until(ec.element_to_be_clickable(AuthPageLocators.NAV_CABINET_BUTTON))
        cabinet_button.click()
        WebDriverWait(driver, 10).until(lambda d: 'id.vk.com' in d.current_url)
        assert 'id.vk.com' in driver.current_url

    def test_welcome_page_after_auth(self, welcome_page):
        assert welcome_page.is_welcome_header_visible()
        
    def test_language_switcher(self, welcome_page):
        welcome_page.assert_switch_language('en')
        welcome_page.assert_switch_language('ru')

    def test_registration_form_required_fields(self, welcome_page):
        welcome_page.click_create_cabinet()
        reg_page = RegistrationPage(welcome_page.driver)
        assert reg_page.is_registration_page()
        
        assert reg_page.is_advertiser_type_visible()
        assert reg_page.is_agency_type_visible()
        assert reg_page.is_country_selector_visible()
        assert reg_page.is_currency_selector_visible()
        assert reg_page.is_email_field_visible() 
        assert reg_page.is_individual_type_visible()
        assert reg_page.is_company_type_visible()
        assert reg_page.is_inn_field_visible()
        assert reg_page.is_full_name_field_visible()
        assert reg_page.is_terms_checkbox_visible()
        assert reg_page.is_mailing_checkbox_visible()

    def test_advertiser_account_type(self, welcome_page):
        welcome_page.click_create_cabinet()
        reg_page = RegistrationPage(welcome_page.driver)
        reg_page.select_advertiser_type()

        reg_page.select_company_type()
        assert reg_page.is_individual_type_visible()
        assert not reg_page.is_full_name_field_visible()
        assert not reg_page.is_inn_field_visible()

        reg_page.select_individual_type()
        assert reg_page.is_company_type_visible()
        assert reg_page.is_individual_type_visible()
        assert reg_page.is_full_name_field_visible()
        assert reg_page.is_inn_field_visible()

    def test_agency_account_type(self, welcome_page):
        welcome_page.click_create_cabinet()
        reg_page = RegistrationPage(welcome_page.driver)
        reg_page.select_agency_type()
        # Проверяем, что доступен только тип "Юридическое лицо"
        assert reg_page.is_company_type_visible()
        assert not reg_page.is_individual_type_visible()
        # Проверяем, что поля для физлиц не отображаются
        assert not reg_page.is_inn_field_visible()
        assert not reg_page.is_full_name_field_visible()

    def test_default_checkbox_states(self, welcome_page):
        welcome_page.click_create_cabinet()
        reg_page = RegistrationPage(welcome_page.driver)
        assert reg_page.get_terms_checkbox_state(), "Terms checkbox should be checked by default"
    #     assert reg_page.get_mailing_checkbox_state(), "Mailing checkbox should be checked by default"

    def test_email_placeholder(self, welcome_page):
        welcome_page.click_create_cabinet()
        reg_page = RegistrationPage(welcome_page.driver)
        assert reg_page.get_email_placeholder() == "example@mail.ru"

    def test_email_required_error(self, welcome_page):
        welcome_page.click_create_cabinet()
        reg_page = RegistrationPage(welcome_page.driver)
        reg_page.focus_and_blur_email()
        assert reg_page.is_requires_field_error_visible()

    def test_email_validation(self, welcome_page):
        welcome_page.click_create_cabinet()
        reg_page = RegistrationPage(welcome_page.driver)
        invalid_emails = [
            "test",
            "test@",
            "test@.",
            "test@.com",
            "test@domain.",
            "test@domain.c",
            "test@@domain.com",
            "!test@domain.com",
        ]
        for email in invalid_emails:
            reg_page.set_email(email)
            reg_page.focus_and_blur_email()
            error_message = reg_page.get_email_error()
            assert error_message == self.error_invalid_email, f"Expected error message: {self.error_invalid_email}, but got: {error_message}"

        valid_emails = [
            "test@domain.com",
            "test.user@domain.com",
            "test-user@domain.com",
            "test_user@domain.com",
            "test@домен.рф",
            "test@sub.domain.com"
        ]
        for email in valid_emails:
            reg_page.set_email(email)
            reg_page.focus_and_blur_email()
            error_message = reg_page.get_email_error()
            assert error_message == None, f"Expected error message: {self.error_invalid_email}, but got: {error_message}"

    def test_inn_validation(self, welcome_page):
        welcome_page.click_create_cabinet()
        reg_page = RegistrationPage(welcome_page.driver)
        reg_page.select_advertiser_type()
        reg_page.select_individual_type()
        _ = reg_page.is_set_inn("12345")
        reg_page.select_advertiser_type() # Чтобы появилась ошибка, нужно увести курсор
        assert reg_page.has_inn_min_length_error()
        _ = reg_page.is_set_inn("1234567890123")
        reg_page.select_advertiser_type()
        assert reg_page.has_inn_max_length_error()
        reg_page.select_advertiser_type()
        _ = reg_page.is_set_inn("123456789012")
        assert not (reg_page.has_inn_min_length_error() and reg_page.has_inn_max_length_error())

    def test_full_name_validation(self, welcome_page):
        welcome_page.click_create_cabinet()
        reg_page = RegistrationPage(welcome_page.driver)
        reg_page.select_advertiser_type()
        reg_page.select_individual_type()
        
        long_name = "А" * 61
        reg_page.set_full_name(long_name)
        reg_page.select_advertiser_type()
        assert reg_page.get_full_name_error() == self.error_max_length

        invalid_names = [
            "John Doe",
            "Иванов123",
            "Иванов!"
        ]
        for name in invalid_names:
            reg_page.set_full_name(name)
            reg_page.select_advertiser_type()
            assert reg_page.get_full_name_error() == self.error_invalid_chars

        valid_names = [
            "Иванов",
            "Иванов-Петров",
            "Иванов Иван",
            "Иванов-Петров Иван Иванович"
        ]
        for name in valid_names:
            reg_page.set_full_name(name)
            reg_page.select_advertiser_type()
            assert not reg_page.has_full_name_error()

    def test_successful_registration(self, welcome_page_for_registration    ):
        welcome_page_for_registration.click_create_cabinet()
        reg_page = RegistrationPage(welcome_page_for_registration.driver)
        reg_page.set_email("test@example.com")
        reg_page.click_create_cabinet()
        assert reg_page.wait_for_redirect_to_cabinet()

        reg_page.click_settings_menu_item()
        reg_page.click_delete_cabinet()
        reg_page.click_accept_delete_cabinet()
        assert reg_page.wait_for_redirect_to_main_page()

    
