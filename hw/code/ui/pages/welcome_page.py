from ui.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from ui.locators.welcome_page_locators import WelcomePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from ui.pages.base_page import WAIT_TIMEOUT

class WelcomePage(BasePage):
    locators = WelcomePageLocators()
    url = 'https://ads.vk.com/hq/registration/'

    def is_welcome_header_visible(self):
        try:
            WebDriverWait(self.driver, WAIT_TIMEOUT).until(
                EC.presence_of_element_located(WelcomePageLocators.WELCOME_HEADER)
            )
            return True
        except TimeoutException:
            return False
        
    # def wait_for_language_switcher(self):
    #     WebDriverWait(self.driver, WAIT_TIMEOUT).until(
    #         EC.presence_of_element_located(WelcomePageLocators.LANGUAGE_SWITCHER)
    #     )

    def switch_language(self, lang):
        self.click(self.locators.LANGUAGE_SWITCHER)
        if lang == 'en':
            self.click(self.locators.LANGUAGE_EN)
        else:
            self.click(self.locators.LANGUAGE_RU)

    # def wait_for_button_text(self, expected_text):
    #     WebDriverWait(self.driver, WAIT_TIMEOUT).until(
    #         lambda d: self.find(self.locators.WELCOME_HEADER).text == expected_text
    #     )

    def assert_switch_language(self, lang):
        expected_texts = {
            'en': "Welcome \nto VK Ads",
            'ru': "Добро пожаловать\nв VK Рекламу"
        }
        self.switch_language(lang)
        actual_text = self.find(self.locators.WELCOME_HEADER, WAIT_TIMEOUT).text
        assert actual_text == expected_texts[lang], f"Expected text '{expected_texts[lang]}', but got '{actual_text}'"
            
    # def get_create_cabinet_button_text(self):
    #     return self.find(self.locators.CREATE_CABINET_BUTTON).text
        
    def click_create_cabinet(self):
        self.click(self.locators.CREATE_CABINET_BUTTON, WAIT_TIMEOUT)

    def assert_welcome_header_visible(self):
        assert self.is_welcome_header_visible(), "Заголовок welcome-страницы не отображается корректно"
