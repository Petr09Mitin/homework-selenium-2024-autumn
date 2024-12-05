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
    url_vkid = "id.vk.com"

    def test_redirect_to_vkid(self, driver):
        base_page = BasePage(driver)
        base_page.click_cabinet_button()
        base_page.assert_redirect(self.url_vkid)

    ### Следующие тесты пройдут только в том случае, если у пользователя 
    ### с текущим логином и паролем еще нет кабинета

    error_required_field = "Обязательное поле"
    error_invalid_email = "Некорректный email адрес"   
    error_max_length = "Напишите текст не больше 60 символов"
    error_invalid_chars = "Некорректные символы. Разрешена только кириллица дефис и пробел"

    def test_welcome_page_for_registration_after_auth(self, welcome_page_for_registration):
        welcome_page_for_registration.assert_welcome_header_visible()
        
    def test_language_switcher(self, welcome_page_for_registration):
        welcome_page_for_registration.assert_switch_language('en')
        welcome_page_for_registration.assert_switch_language('ru')

    def test_registration_form_required_fields(self, welcome_page_for_registration):
        welcome_page_for_registration.click_create_cabinet()
        reg_page = RegistrationPage(welcome_page_for_registration.driver)
        reg_page.assert_registration_page_opened()

        reg_page.assert_advertiser_type_visible()
        reg_page.assert_agency_type_visible()
        reg_page.assert_country_selector_visible()
        reg_page.assert_currency_selector_visible()
        reg_page.assert_email_field_visible()
        reg_page.assert_individual_type_visible()
        reg_page.assert_company_type_visible()
        reg_page.assert_inn_field_visible()
        reg_page.assert_full_name_field_visible()
        reg_page.assert_terms_checkbox_visible()
        reg_page.assert_mailing_checkbox_visible()

    def test_advertiser_account_type(self, welcome_page_for_registration):
        welcome_page_for_registration.click_create_cabinet()
        reg_page = RegistrationPage(welcome_page_for_registration.driver)
        reg_page.select_advertiser_type()

        reg_page.select_company_type()
        reg_page.assert_individual_type_visible()
        reg_page.assert_full_name_field_visible(should_be_visible=False)
        reg_page.assert_inn_field_visible(should_be_visible=False)

        reg_page.select_individual_type()
        reg_page.assert_company_type_visible()
        reg_page.assert_individual_type_visible()
        reg_page.assert_full_name_field_visible()
        reg_page.assert_inn_field_visible()

    def test_agency_account_type(self, welcome_page_for_registration):
        welcome_page_for_registration.click_create_cabinet()
        reg_page = RegistrationPage(welcome_page_for_registration.driver)
        reg_page.select_agency_type()
        # Проверяем, что доступен только тип "Юридическое лицо"
        reg_page.assert_company_type_visible()
        reg_page.assert_individual_type_visible(should_be_visible=False)
        # Проверяем, что поля для физлиц не отображаются
        reg_page.assert_inn_field_visible(should_be_visible=False)
        reg_page.assert_full_name_field_visible(should_be_visible=False)

    def test_default_checkbox_states(self, welcome_page_for_registration):
        welcome_page_for_registration.click_create_cabinet()
        reg_page = RegistrationPage(welcome_page_for_registration.driver)
        reg_page.assert_terms_checkbox_visible()
        reg_page.assert_mailing_checkbox_visible()

    def test_email_placeholder(self, welcome_page_for_registration):
        welcome_page_for_registration.click_create_cabinet()
        reg_page = RegistrationPage(welcome_page_for_registration.driver)
        reg_page.assert_email_placeholder()

    def test_email_required_error(self, welcome_page_for_registration):
        welcome_page_for_registration.click_create_cabinet()
        reg_page = RegistrationPage(welcome_page_for_registration.driver)
        reg_page.focus_and_blur_email()
        reg_page.assert_required_field_error_visible()

    def test_email_validation(self, welcome_page_for_registration):
        welcome_page_for_registration.click_create_cabinet()
        reg_page = RegistrationPage(welcome_page_for_registration.driver)
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
            reg_page.assert_error_message(error_message, self.error_invalid_email)

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
            reg_page.assert_error_message(error_message, None)
            # assert error_message == None, f"Expected error message: {self.error_invalid_email}, but got: {error_message}"

    def test_inn_validation(self, welcome_page_for_registration):
        welcome_page_for_registration.click_create_cabinet()
        reg_page = RegistrationPage(welcome_page_for_registration.driver)
        reg_page.select_advertiser_type()
        reg_page.select_individual_type()
        _ = reg_page.is_set_inn("12345")
        reg_page.select_advertiser_type() # Чтобы появилась ошибка, нужно увести курсор
        reg_page.assert_inn_min_length_error()
        _ = reg_page.is_set_inn("1234567890123")
        reg_page.select_advertiser_type()
        reg_page.assert_inn_max_length_error()
        reg_page.select_advertiser_type()
        _ = reg_page.is_set_inn("123456789012")
        reg_page.assert_inn_min_length_error(should_be_visible=False)
        reg_page.assert_inn_max_length_error(should_be_visible=False)

    def test_full_name_validation(self, welcome_page_for_registration):
        welcome_page_for_registration.click_create_cabinet()
        reg_page = RegistrationPage(welcome_page_for_registration.driver)
        reg_page.select_advertiser_type()
        reg_page.select_individual_type()
        
        long_name = "А" * 61
        reg_page.set_full_name(long_name)
        reg_page.select_advertiser_type()
        error_message = reg_page.get_full_name_error()
        reg_page.assert_error_message(error_message, self.error_max_length)
        # assert reg_page.get_full_name_error() == self.error_max_length

        invalid_names = [
            "John Doe",
            "Иванов123",
            "Иванов!"
        ]
        for name in invalid_names:
            reg_page.set_full_name(name)
            reg_page.select_advertiser_type()
            error_message = reg_page.get_full_name_error()
            reg_page.assert_error_message(error_message, self.error_invalid_chars)
            # assert reg_page.get_full_name_error() == self.error_invalid_chars

        valid_names = [
            "Иванов",
            "Иванов-Петров",
            "Иванов Иван",
            "Иванов-Петров Иван Иванович"
        ]
        for name in valid_names:
            reg_page.set_full_name(name)
            reg_page.select_advertiser_type()
            error_message = reg_page.get_full_name_error()
            reg_page.assert_error_message(error_message, None)
            # assert not reg_page.has_full_name_error()

    def test_successful_registration(self, welcome_page_for_registration):
        welcome_page_for_registration.click_create_cabinet()
        reg_page = RegistrationPage(welcome_page_for_registration.driver)
        reg_page.set_email("test@example.com")
        reg_page.click_create_cabinet()
        reg_page.assert_redirect_to_cabinet()
        # assert reg_page.wait_for_redirect_to_cabinet()

        reg_page.click_settings_menu_item()
        reg_page.click_delete_cabinet()
        reg_page.click_accept_delete_cabinet()
        reg_page.assert_redirect_to_main_page()
        # assert reg_page.wait_for_redirect_to_main_page()
