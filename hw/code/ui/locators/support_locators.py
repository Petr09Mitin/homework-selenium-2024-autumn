from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import BasePageLocators

class SupportPageLocators(BasePageLocators):
    MENU_ITEM = (By.XPATH, '//div[@data-route="help"]')
    
    LIST_WINDOW = (By.XPATH, '//div[contains(@class, "PopoverContent_root__C8WZq")]')
    
    REFERENCE_BUTTON = (By.XPATH, '//a[@data-testid="portal-link-menu-item"]')
    SUGGEST_IDEA_BUTTON = (By.XPATH, '//a[@data-testid="upvote-menu-item"]')
    ASK_QUESTION_BUTTON = (By.XPATH, '//div[@data-testid="feedback-menu-item"]')
    
    MODAL_ASK_QUESTION = (By.XPATH, '//div[@class="ModalRoot_componentWrapper__uzHTL"]')
    MODAL_CLOSE_BUTTON = (By.XPATH, '//div[contains(@class, "vkuiModalDismissButton")]')
    MODAL_REFERENCE_TO_HELP = (By.XPATH, '//a[@href="/help"]')
    
    MODAL_CHOOSE_THEME = (By.XPATH, '//div[contains(@class, "vkuiCustomSelect")]')
    LIST_THEMES = (By.XPATH, '//select[@name="theme"]')
    OTHER_THEME = (By.XPATH, '//option[@value="other"]')
    MESSAGE_FIELD = (By.XPATH, '//textarea[@name="message"]')
    NAME_FIELD = (By.XPATH, '//input[@name="name"]')
    EMAIL_FIELD = (By.XPATH, '//input[@name="email"]')
    SUBMIT_QUESTION_BUTTON = (By.XPATH, '//button[@data-testid="submit"]')
    ADD_IMAGE_INPUT = (By.XPATH, '//input[@class="vkuiVisuallyHidden"]')
    
    SUCCESS_MODAL = (By.XPATH, '//div[@class="ModalManagerPage_modalContent__ybbav"]')
    CLOSE_SUCCESS_MODAL = (By.XPATH, '//div[@class="vkuiPlaceholder__action"]/button')