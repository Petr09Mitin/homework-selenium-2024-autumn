import time

from ui.pages.base_page import BasePage, PageNotOpenedException
from selenium.webdriver.common.by import By
from ui.locators.registration_page_locators import RegistrationPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException

class RegistrationPage(BasePage):
    locators = RegistrationPageLocators()
    url = 'https://ads.vk.com/hq/registration/new/'
    
    def is_registration_page(self):
        return self.driver.current_url == self.url
        
    def is_account_type_visible(self):
        return self.find(self.locators.ACCOUNT_TYPE).is_displayed()
    
    def is_advertiser_type_visible(self):
        return self.find(self.locators.ADVERTISER_TYPE).is_displayed()
    
    def is_agency_type_visible(self):
        return self.find(self.locators.AGENCY_TYPE).is_displayed()
        
    def is_country_selector_visible(self):
        return self.find(self.locators.COUNTRY_SELECTOR).is_displayed()
        
    def is_currency_selector_visible(self):
        return self.find(self.locators.CURRENCY_SELECTOR).is_displayed()
        
    def is_email_field_visible(self):
        return self.find(self.locators.EMAIL_FIELD).is_displayed()

    def get_email_placeholder(self):
        return self.find(self.locators.EMAIL_FIELD).get_attribute('placeholder')

    def focus_and_blur_email(self):
        email_field = self.find(self.locators.EMAIL_FIELD)
        email_field.click()
        self.find(self.locators.ACCOUNT_TYPE).click()  # клик в другое место

    def set_email(self, email):
        email_field = self.find(self.locators.EMAIL_FIELD)
        email_field.clear()
        email_field.send_keys(email)

    def get_email_error(self):
        try:
            return self.find(self.locators.ERROR_INVALID_EMAIL).text
        except:
            try:
                return self.find(self.locators.ERROR_REQUIRED_FIELD).text
            except:
                return None

    def has_email_error(self):
        return self.get_email_error() is not None

    def set_inn(self, inn):
        inn_field = self.find(self.locators.INN_FIELD)
        inn_field.clear()
        inn_field.send_keys(inn)

    def get_inn_value(self):
        return self.find(self.locators.INN_FIELD).get_attribute('value')

    def get_inn_error(self):
        try:
            return self.find(self.locators.ERROR_INN_MIN_LENGTH).text
        except:
            try:
                return self.find(self.locators.ERROR_INN_MAX_LENGTH).text
            except:
                return None

    def has_inn_error(self):
        return self.get_inn_error() is not None

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

    def get_terms_checkbox_state(self):
        return self.find(self.locators.TERMS_CHECKBOX).is_selected()

    def get_mailing_checkbox_state(self):
        return self.find(self.locators.MAILING_CHECKBOX).is_selected()

    def toggle_terms_checkbox(self):
        self.find(self.locators.TERMS_CHECKBOX).click()

    def toggle_mailing_checkbox(self):
        self.find(self.locators.MAILING_CHECKBOX).click()

    def click_create_cabinet(self):
        self.find(self.locators.CREATE_BUTTON).click()

    # Выбор типов аккаунта
    def select_advertiser_type(self):
        self.find(self.locators.ADVERTISER_TYPE).click()

    def select_agency_type(self):
        self.find(self.locators.AGENCY_TYPE).click()

    def select_individual_type(self):
        self.find(self.locators.INDIVIDUAL_TYPE).click()

    def select_company_type(self):
        self.find(self.locators.AGENCY_TYPE).click()

    # Проверяет, что выбран тип "Юридическое лицо"
    def is_company_type_selected(self):
        return self.find(self.locators.COMPANY_TYPE).is_selected()

    def is_individual_type_visible(self):
        try:
            return self.find(self.locators.INDIVIDUAL_TYPE).is_displayed()
        except:
            return False
        
    def is_company_type_visible(self):
        try:
            return self.find(self.locators.COMPANY_TYPE).is_displayed()
        except:
            return False

    def is_inn_field_visible(self):
        try:
            return self.find(self.locators.INN_FIELD).is_displayed()
        except:
            return False

    def is_full_name_field_visible(self):
        try:
            return self.find(self.locators.NAME_FIELD).is_displayed()
        except:
            return False
        
    def is_terms_checkbox_visible(self):
        try:
            return self.find(self.locators.TERMS_CHECKBOX).is_displayed()
        except:
            return False

    def is_mailing_checkbox_visible(self):
        try:
            return self.find(self.locators.MAILING_CHECKBOX).is_displayed()
        except:
            return False

    def is_requires_field_error_visible(self):
        try:
            return self.find(self.locators.ERROR_REQUIRED_FIELD).is_displayed()
        except:
            return False
    
    # Заполняет все обязательные поля валидными данными
    def fill_required_fields(self):
        self.select_advertiser_type()
        self.set_email("test@example.com")
        self.select_individual_type()
        # TODO: добавить заполнение других обязательных полей

    # def wait_for_redirect_to_cabinet(self):
    #     return self.wait().until(lambda d: "ads.vk.com/hq/overview" in d.current_url)
    def wait_for_redirect_to_cabinet(self, timeout=15):
        try:
            return WebDriverWait(self.driver, timeout).until(lambda d: "ads.vk.com/hq/overview" in d.current_url)
        except TimeoutException:
            return False
        