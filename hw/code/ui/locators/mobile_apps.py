from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import BasePageLocators


class MobileAppsLocators(BasePageLocators):
    MENU_ITEM = (By.XPATH, '//a[@href="/hq/apps"]')

    NO_APPS_HEADER = (By.XPATH, '//h2[contains(text(), "Нет привязанных приложений")]')    
    ADD_APP_BUTTON = (By.XPATH, '//button[@data-testid="button-Добавить приложение"]')
    MODAL_ADD_APP = (By.XPATH, '//div[@class="ModalRoot_componentWrapper__uzHTL"]')
    MORE_ABOUT_APP = (By.XPATH, '//a[@href="/help/articles/add_app"]')
    INPUT_ADD_APP = (By.XPATH, '//input[@data-testid="app-link"]')
    MODAL_CLOSE_BUTTON = (By.XPATH, '//div[@class="ModalRoot_componentWrapper__uzHTL"]//div[@aria-label="Закрыть"]')
    MODAL_ADD_APP_BUTTON = (By.XPATH, '//button[@data-testid="app-add"]')
    
    WRONG_LINK = (By.XPATH, '//span[contains(text(), "Введите корректную ссылку на приложение")]')