from ui.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from ui.locators.welcome_page_locators import WelcomePageLocators

class WelcomePage(BasePage):
    locators = WelcomePageLocators()
    url = 'https://ads.vk.com/hq/registration/'

    def is_welcome_header_visible(self):
        return self.find(self.locators.WELCOME_HEADER).is_displayed()
    
    def switch_language(self, lang):
        self.click(self.locators.LANGUAGE_SWITCHER)
        if lang == 'en':
            self.click(self.locators.LANGUAGE_EN)
        else:
            self.click(self.locators.LANGUAGE_RU)
            
    def get_create_cabinet_button_text(self): # TODO: странный метод, не понятно зачем
        return self.find(self.locators.CREATE_CABINET_BUTTON).text
        
    def click_create_cabinet(self):
        self.find(self.locators.CREATE_CABINET_BUTTON).click() 