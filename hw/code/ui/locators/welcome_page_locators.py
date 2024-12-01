from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import BasePageLocators

class WelcomePageLocators(BasePageLocators):
    WELCOME_HEADER = (By.XPATH, "//h1[contains(text(), 'Добро пожаловать')]")
    CREATE_CABINET_BUTTON = (By.XPATH, "//button[contains(text(), 'Создать новый кабинет')]")
    MYTARGET_BUTTON = (By.XPATH, "//button[contains(text(), 'Использовать рекламный кабинет myTarget')]")
    LANGUAGE_SWITCHER = (By.XPATH, "//div[contains(@class, 'LanguageSelector_languageSelector')]")
    LANGUAGE_EN = (By.XPATH, "//h4[text()='English']")
    LANGUAGE_RU = (By.XPATH, "//h4[text()='Русский']")
