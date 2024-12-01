from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import BasePageLocators

class RegistrationPageLocators(BasePageLocators):
    ADVERTISER_TYPE = (By.XPATH, "//span[contains(text(), 'Рекламодатель')]")
    AGENCY_TYPE = (By.XPATH, "//span[contains(text(), 'Агентство')]")
    COUNTRY_SELECTOR = (By.CSS_SELECTOR, "input[data-testid='country']")
    CURRENCY_SELECTOR = (By.CSS_SELECTOR, "input[data-testid='currency']")
    EMAIL_FIELD = (By.CSS_SELECTOR, "input[data-testid='email']")
    INDIVIDUAL_TYPE = (By.XPATH, "//span[contains(text(), 'Физическое лицо') or contains(text(), 'Individual')]")
    COMPANY_TYPE = (By.XPATH, "//span[contains(text(), 'Юридическое лицо') or contains(text(), 'Legal entity')]")
    INDIVIDUAL_TYPE = (By.XPATH, "//span[contains(text(), 'Физическое лицо')]")
    COMPANY_TYPE = (By.XPATH, "//span[contains(text(), 'Юридическое лицо')]")
    INN_FIELD = (By.NAME, "inn")
    NAME_FIELD = (By.NAME, "name")
    TERMS_CHECKBOX = (By.CSS_SELECTOR, "input[name='offer']")
    MAILING_CHECKBOX = (By.CSS_SELECTOR, "input.vkuiVisuallyHidden.vkuiCheckbox__input[type='checkbox'][checked]:not([name='offer'])")
    CREATE_BUTTON = (By.CSS_SELECTOR, "button[data-testid='create-button']")

    ERROR_REQUIRED_FIELD = (By.XPATH, "//span[@role='alert'][text()='Обязательное поле']")
    ERROR_INVALID_EMAIL = (By.XPATH, "//span[@role='alert'][text()='Некорректный email адрес']")
    ERROR_INN_MIN_LENGTH = (By.XPATH, "//span[@role='alert'][text()='Напишите не меньше 12 символов']")
    ERROR_INN_MAX_LENGTH = (By.XPATH, "//span[@role='alert'][text()='Напишите текст не больше 12 символов']")
    ERROR_NAME_MAX_LENGTH = (By.XPATH, "//span[@role='alert'][text()='Напишите текст не больше 60 символов']")
    ERROR_NAME_INVALID_CHARS = (By.XPATH, "//span[@role='alert'][text()='Некорректные символы. Разрешена только кириллица дефис и пробел']")

    # ADVERTISER_TYPE = (By.CSS_SELECTOR, "input[data-testid='cabinet-advert']") # рекламодатель
    # AGENCY_TYPE = (By.CSS_SELECTOR, "input[data-testid='cabinet-agency']") # агентство
