from selenium.webdriver.common.by import By


class SettingsAccessLocators:
    TAB_ITEM = (By.XPATH, '//*[@data-testid="tabs-item-settings.access"]')
    
    NO_CABINETS = (By.XPATH, '//h2[contains(text(), "Доступа к другим кабинетам пока нет")]')
    
    MORE_INFO = (By.XPATH, '//a[@href="/help/articles/additionalaccounts"]')
    ADD_CABINET_BUTTON = (By.XPATH, '//button[@data-testid="add-user"]')
    
    MODAL_ADD_CABINET = (By.XPATH, '//div[@class="ModalRoot_componentWrapper__uzHTL"]')
    
    INPUT_ADD_ACCOUNT = (By.XPATH, '//*[@data-testid="userid-input"]')
    
    CANCEL_ADD_CABINET = (By.XPATH, '//*[@data-testid="cancel"]')
    SUBMIT_ADD_CABINET = (By.XPATH, '//*[@data-testid="submit"]')
    EMPTY_FIELD = (By.XPATH, '//span[contains(text(), "Обязательное поле")]')
    INCORRECT_ACCOUNT_ID = (By.XPATH, '//span[contains(text(), "Не нашли такой аккаунт. Проверьте, правильно ли введён ID")]')
    
    SEARCH = (By.XPATH, '//input[@data-testid="search"]')
    NOTHING_FOUND = (By.XPATH, '//h2[contains(text(), "Ничего не нашлось")]')
    CLEAR_QUERY = (By.XPATH, '//button[@aria-label="Очистить"]')
    REMOVE_CABINET = (By.XPATH, '//button[@data-test="remove-button"]')
    
    MODAL_REMOVE_CABINET = (By.XPATH, '//div[@class="vkuiModalPage__content-wrap"]')
    CANCEL_REMOVE_CABINET_BUTTON = (By.XPATH, '//div[@class="Remove_buttons__hSad4"]//button[contains(@class, "vkuiButton--mode-secondary")]')
    ACCEPT_REMOVE_CABINET_BUTTON = (By.XPATH, '//div[@class="Remove_buttons__hSad4"]//button[contains(@class, "vkuiButton--mode-primary")]')
    
    @staticmethod
    def find_cabinet_by_name(name):
        return (By.XPATH, f'//span[@class="ListAccess_name__QUCY9" and contains(text(), "{name}")]')