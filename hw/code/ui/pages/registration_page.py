import time

from ui.pages.base_page import BasePage, PageNotOpenedException
from selenium.webdriver.common.by import By
from ui.locators.registration_page_locators import RegistrationPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from ui.pages.base_page import WAIT_TIMEOUT, WAIT_TIMEOUT_10
from selenium.webdriver.support import expected_conditions as EC
from ui.locators.settings_access_locators import SettingsAccessLocators
from ui.locators.settings_general_locators import SettingsGeneralLocators

class RegistrationPage(BasePage):
    locators = RegistrationPageLocators()
    url = 'https://ads.vk.com/hq/registration/new/'
    
    def is_registration_page(self):
        current_url = self.driver.current_url.rstrip('/')
        expected_url = self.url.rstrip('/')
        return current_url == expected_url
    
    # Проверка видимости элементов
    def is_advertiser_type_visible(self):
        return self.find(self.locators.ADVERTISER_TYPE, WAIT_TIMEOUT_10)
    
    def is_agency_type_visible(self):
        return self.find(self.locators.AGENCY_TYPE, WAIT_TIMEOUT_10)
        
    def is_country_selector_visible(self):
        return self.find(self.locators.COUNTRY_SELECTOR, WAIT_TIMEOUT_10)
        
    def is_currency_selector_visible(self):
        return self.find(self.locators.CURRENCY_SELECTOR, WAIT_TIMEOUT_10)
        
    def is_email_field_visible(self):
        return self.find(self.locators.EMAIL_FIELD, WAIT_TIMEOUT_10)
    
    def is_individual_type_visible(self):
        try:
            self.find(self.locators.INDIVIDUAL_TYPE, 1) 
            return True
        except TimeoutException:
            return False
    
    def is_company_type_visible(self):
        try:
            self.find(self.locators.COMPANY_TYPE, 1) 
            return True
        except TimeoutException:
            return False
    
    def is_inn_field_visible(self):
        try:
            self.find(self.locators.INN_FIELD, 1) 
            return True
        except TimeoutException:
            return False

    def is_full_name_field_visible(self):
        try:
            self.find(self.locators.NAME_FIELD, 1) 
            return True
        except TimeoutException:
            return False
        
    def is_terms_checkbox_visible(self):
        return self.find(self.locators.TERMS_CHECKBOX, WAIT_TIMEOUT_10)

    def is_mailing_checkbox_visible(self):
        return self.find(self.locators.MAILING_CHECKBOX, WAIT_TIMEOUT_10)

    def is_requires_field_error_visible(self):
        try:
            self.find(self.locators.ERROR_REQUIRED_FIELD, WAIT_TIMEOUT_10)
            return True
        except TimeoutException:
            return False
    
    def wait_until_invisible(self, locator, timeout=WAIT_TIMEOUT_10):
        try:
            WebDriverWait(self.driver, timeout).until_not(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    # EMAIL
    def get_email_placeholder(self):
        return self.find(self.locators.EMAIL_FIELD).get_attribute('placeholder')

    def set_email(self, email):
        email_field = self.find(self.locators.EMAIL_FIELD)
        email_field.clear()
        email_field.send_keys(email)

    # def get_email_error(self):
    #     try:
    #         return self.find(self.locators.ERROR_INVALID_EMAIL).text
    #     except:
    #         try:
    #             return self.find(self.locators.ERROR_REQUIRED_FIELD).text
    #         except:
    #             return None

    def get_email_error(self):
        try:
            error_element = self.find(self.locators.ERROR_INVALID_EMAIL, WAIT_TIMEOUT_10)
            return error_element.text
        except TimeoutException:
            return None

    def has_email_error(self):
        return self.get_email_error() is not None
    
    # Имитация пользовательского взаимодействия с полем
    def focus_and_blur_email(self): 
        email_field = self.find(self.locators.EMAIL_FIELD)
        email_field.click()
        self.find(self.locators.ADVERTISER_TYPE).click()

    # INN
    def is_set_inn(self, inn):
        try:
            inn_field = self.find(self.locators.INN_FIELD, WAIT_TIMEOUT_10)
            inn_field.clear()
            inn_field.send_keys(inn)
            return True
        except TimeoutException:
            return False
        except Exception:
            return False
    
    def get_inn_value(self):
        try:
            inn_field = self.find(self.locators.INN_FIELD, WAIT_TIMEOUT_10)
            return inn_field.get_attribute('value')
        except TimeoutException:
            return None

    def has_inn_min_length_error(self):
        try:
            self.find(self.locators.ERROR_INN_MIN_LENGTH, WAIT_TIMEOUT_10)
            return True
        except TimeoutException:
            return False

    def has_inn_max_length_error(self):
        try:
            self.find(self.locators.ERROR_INN_MAX_LENGTH, WAIT_TIMEOUT_10)
            return True
        except TimeoutException:
            return False
    
    # FULL NAME
    def set_full_name(self, name):
        name_field = self.find(self.locators.NAME_FIELD)
        name_field.clear()
        name_field.send_keys(name)

    def get_full_name_error(self):
        try:
            return self.find(self.locators.ERROR_NAME_MAX_LENGTH).text
        except:
            try:
                return self.find(self.locators.ERROR_NAME_INVALID_CHARS).text
            except:
                return None

    def has_full_name_error(self):
        return self.get_full_name_error() is not None

    # Чекбоксы
    def get_terms_checkbox_state(self):
        return self.find(self.locators.TERMS_CHECKBOX).is_selected()

    def get_mailing_checkbox_state(self):
        return self.find(self.locators.MAILING_CHECKBOX).is_selected()

    def toggle_terms_checkbox(self):
        self.click(self.locators.TERMS_CHECKBOX, WAIT_TIMEOUT_10)

    def toggle_mailing_checkbox(self):
        self.click(self.locators.MAILING_CHECKBOX, WAIT_TIMEOUT_10)

    # Выбор типов аккаунта
    def select_advertiser_type(self):
        self.click(self.locators.ADVERTISER_TYPE, WAIT_TIMEOUT_10)

    def select_agency_type(self):
        self.click(self.locators.AGENCY_TYPE, WAIT_TIMEOUT_10)
        self.wait_until_invisible(self.locators.INDIVIDUAL_TYPE)

    def select_individual_type(self):
        self.click(self.locators.INDIVIDUAL_TYPE, WAIT_TIMEOUT_10)

    def select_company_type(self):
        self.click(self.locators.COMPANY_TYPE, WAIT_TIMEOUT_10)

    # Завершение регистрации
    def click_create_cabinet(self):
        self.click(self.locators.CREATE_BUTTON, WAIT_TIMEOUT_10)

    def wait_for_redirect_to_cabinet(self):
        try:
            return WebDriverWait(self.driver, WAIT_TIMEOUT).until(lambda d: "ads.vk.com/hq/overview" in d.current_url)
        except TimeoutException:
            return False
        
    # для удаления кабинета после регистрации
    def click_settings_menu_item(self, timeout=WAIT_TIMEOUT):
        self.click(locator=SettingsGeneralLocators.MENU_ITEM, timeout=timeout)
        
    def click_delete_cabinet(self, timeout=WAIT_TIMEOUT):
        self.click(locator=SettingsAccessLocators.DELETE_CABINET_BUTTON, timeout=timeout)
        
    def click_accept_delete_cabinet(self, timeout=WAIT_TIMEOUT):
        self.click(locator=SettingsAccessLocators.ACCEPT_DELETE_CABINET_BUTTON, timeout=timeout)

    def wait_for_redirect_to_main_page(self):
        try:
            return WebDriverWait(self.driver, WAIT_TIMEOUT).until(lambda d: "ads.vk.com" in d.current_url)
        except TimeoutException:
            return False
        
    # asserts
    def assert_registration_page_opened(self):
        assert self.is_registration_page(), "Должна открыться страница регистрации"
    
    def assert_advertiser_type_visible(self):
        assert self.is_advertiser_type_visible(), "Чекбокс Рекламодатель должен быть виден"
    
    def assert_agency_type_visible(self):
        assert self.is_agency_type_visible(), "Чекбокс Агентство должен быть виден"

    def assert_country_selector_visible(self):
        assert self.is_country_selector_visible(), "Селектор страны должен быть виден"
    
    def assert_currency_selector_visible(self):
        assert self.is_currency_selector_visible(), "Селектор валюты должен быть виден"

    def assert_email_field_visible(self):
        assert self.is_email_field_visible(), "Поле для ввода email должно быть видно"

    # def assert_inn_field_visible(self):
    #     assert self.is_inn_field_visible(), "Поле для ввода ИНН должно быть видно"

    def assert_inn_field_visible(self, should_be_visible=True):
        if should_be_visible:
            assert self.is_inn_field_visible(), "Поле для ввода ИНН должно быть видно"
        else:
            assert not self.is_inn_field_visible(), "Поле для ввода ИНН не должно быть видно"
    
    # def assert_full_name_field_visible(self):
    #     assert self.is_full_name_field_visible(), "Поле для ввода ФИО должно быть видно"

    def assert_full_name_field_visible(self, should_be_visible=True):
        if should_be_visible:
            assert self.is_full_name_field_visible(), "Поле для ввода ФИО должно быть видно"
        else:
            assert not self.is_full_name_field_visible(), "Поле для ввода ФИО не должно быть видно"
    
    # def assert_individual_type_visible(self):
    #     assert self.is_individual_type_visible(), "Чекбокс Физическое лицо должен быть виден"

    def assert_individual_type_visible(self, should_be_visible=True):
        if should_be_visible:
            assert self.is_individual_type_visible(), "Чекбокс Физическое лицо должен быть виден"
        else:
            assert not self.is_individual_type_visible(), "Чекбокс Физическое лицо не должен быть виден"
    
    def assert_company_type_visible(self):
        assert self.is_company_type_visible(), "Чекбокс Юридическое лицо должен быть виден"

    def assert_terms_checkbox_visible(self):
        assert self.is_terms_checkbox_visible(), "Чекбокс Условий должен быть виден"

    def assert_mailing_checkbox_visible(self):
        assert self.is_mailing_checkbox_visible(), "Чекбокс Рассылки должен быть виден"

    def assert_email_placeholder(self, expected_placeholder="example@mail.ru"):
        actual_placeholder = self.get_email_placeholder()
        assert actual_placeholder == expected_placeholder, f"Ожидался плейсхолдер email '{expected_placeholder}', но получен '{actual_placeholder}'"

    def assert_required_field_error_visible(self):
        assert self.is_requires_field_error_visible(), "Ошибка обязательного поля email должна быть видна"
    
    def assert_error_message(self, actual_message, expected_message):
        assert actual_message == expected_message, f"Ожидалось сообщение об ошибке: '{expected_message}', но получено: '{actual_message}'"

    # def assert_inn_min_length_error(self):
    #     assert self.has_inn_min_length_error(), "Ошибка о том, что не достигнута минимальная длина ИНН, должна быть видна"

    # def assert_inn_max_length_error(self):
    #     assert self.has_inn_max_length_error(), "Ошибка о том, что превышена максимальная длина ИНН, должна быть видна"

    def assert_inn_min_length_error(self, should_be_visible=True):
        if should_be_visible:
            assert self.has_inn_min_length_error(),  "Ошибка о том, что не достигнута минимальная длина ИНН, должна быть видна"
        else:
            assert not self.has_inn_min_length_error(),  "Ошибка о том, что не достигнута минимальная длина ИНН, не должна быть видна"

    def assert_inn_max_length_error(self, should_be_visible=True):
        if should_be_visible:
            assert self.has_inn_max_length_error(),  "Ошибка о том, что превышена максимальная длина ИНН, должна быть видна"
        else:
            assert not self.has_inn_max_length_error(),  "Ошибка о том, что превышена максимальная длина ИНН, не должна быть видна"

    def assert_redirect_to_cabinet(self):
        assert self.wait_for_redirect_to_cabinet(), "Ожидался редирект на ads.vk.com/hq/overview, но он не произошел"

    def assert_redirect_to_main_page(self):
        assert self.wait_for_redirect_to_main_page(), "Ожидался редирект на ads.vk.com, но он не произошел"
