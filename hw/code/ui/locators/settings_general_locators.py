from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import BasePageLocators

class SettingsGeneralLocators(BasePageLocators):
    MENU_ITEM = (By.XPATH, '//*[@data-entityid="settings"]')
    TAB_ITEM = (By.XPATH, '//*[@data-testid="tabs-item-settings"]')
    
    GENERAL = (By.XPATH, '//*[@data-testid="tabs-item-settings"]')
    
    FILL_PHONE_INPUT = (By.XPATH, '//*[@data-testid="general-phone"]')
    ADD_EMAIL_BUTTON = (By.XPATH, '//*[@data-testid="add-email"]')
    
    @staticmethod
    def ADDED_EMAIL_INPUT(id):
        return (By.XPATH, f'//*[@data-testid="email-{id}"]')
    
    DELETE_ADDED_EMAIL_BUTTON = (By.XPATH, '//*[contains(@class, "vkuiRemovable__action")]')
    
    FIO_INPUT = (By.XPATH, '//*[@data-testid="general-ord-name"]')
    INN_INPUT = (By.XPATH, '//*[@data-testid="general-ord-inn"]')
    
    CABINET_NAME_INPUT = (By.XPATH, '//*[@data-testid="account-item"]')

    SHOW_HOT_KEYS_BUTTON = (By.XPATH, '//div[@class="HotKeysToggler_desc__15xpt"]//button')
    
    MODAL_HOT_KEYS = (By.XPATH, '//div[@id="_modal_2-label"]')
    
    CLOSE_HOT_KEYS_BUTTON = (By.XPATH, '//div[contains(@class, "ModalManagerPage_footerSeparator__OY6lz")]/button')
    MORE_ABOUT_API_BUTTON = (By.XPATH, '//*[@href="https://ads.vk.com/help/articles/help_api"]') 
    LOGOUT_DEVICES_BUTTON = (By.XPATH, '//*[contains(@class, "LogoutFromOtherDevices_button__cFDmE")]')
    SAVE_BUTTON = (By.XPATH, '//*[@data-testid="settings-save"]')
    REMOVE_CHANGES_BUTTON = (By.XPATH, '//*[@data-testid="settings-cancel"]')
    
    INCORRECT_PHONE = (By.XPATH, '//div[contains(text(), "Некорректный номер телефона")]')
    INCORRECT_EMAIL = (By.XPATH, '//div[contains(text(), "Некорректный email адрес")]')
    UNAVAILABLE_INN = (By.XPATH, '//div[contains(text(), "Некорректный ИНН")]')
    INCORRECT_INN = (By.XPATH, '//div[contains(text(), "Длина ИНН должна быть 12 символов")]')
    LOGOUT_SUCCESSFUL = (By.XPATH, '//div[contains(text(), "Активные сеансы на других устройствах завершены")]')
    EMPTY_FIELD = (By.XPATH, '//div[contains(text(), "Обязательное поле")]')
    
    CONNECT_AGENCY = (By.XPATH, '//button[contains(@class, "JoinAgency_action__m8gzk")]')
    MODAL_AGENCY = (By.XPATH, '//div[@class="ModalRoot_componentWrapper__uzHTL"]')
    CANCEL_CONNECT_AGENCY = (By.XPATH, '//div[@class="ModalRoot_componentWrapper__uzHTL"]//button[@data-testid="cancel"]')
    ACCEPT_CONNECT_AGENCY = (By.XPATH, '//div[@class="ModalRoot_componentWrapper__uzHTL"]//button[@data-testid="submit"]')
    
    AGENCY_ID_INPUT = (By.XPATH, '//div[@class="ModalRoot_componentWrapper__uzHTL"]//input[@placeholder="Введите ID агентства"]')
    
    EMPTY_AGENT_FIELD = (By.XPATH, '//div[contains(text(), "Введите ID")]')
    NOT_FOUND_AGENCY = (By.XPATH, '//div[contains(text(), "Агентства с таким ID не найдено")]')
    INCORRECT_AGENCY = (By.XPATH, '//div[contains(text(), "Некорректный ID")]')