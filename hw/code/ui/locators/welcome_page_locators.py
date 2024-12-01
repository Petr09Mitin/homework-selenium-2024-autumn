from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import BasePageLocators

class WelcomePageLocators(BasePageLocators):
    WELCOME_HEADER = (By.XPATH, "//h1[contains(@class, 'registration_panelTitle')]")
    CREATE_CABINET_BUTTON = (By.CSS_SELECTOR, "div[data-testid='create-new']")
    MYTARGET_BUTTON = (By.CSS_SELECTOR, "div[data-testid='export-target']")
    LANGUAGE_SWITCHER = (By.XPATH, "//div[contains(@class, 'LanguageSelector_languageSelector')]")
    LANGUAGE_EN = (By.XPATH, "//h4[text()='English']")
    LANGUAGE_RU = (By.XPATH, "//h4[text()='Русский']")
