import time

from ui.pages.base_page import BasePage, PageNotOpenedException
from selenium.webdriver.common.by import By
from ui.locators.registration_page_locators import RegistrationPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from ui.pages.base_page import WAIT_TIMEOUT, WAIT_TIMEOUT_10
from selenium.webdriver.support import expected_conditions as EC

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
        