from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC
from ui.pages.base_page import BasePage, DEFAULT_TIMEOUT
from ui.locators.support_locators import SupportPageLocators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from datetime import date
from os import path
from selenium.common.exceptions import TimeoutException

class SupportPage(BasePage):
    url = 'https://ads.vk.com/hq/overview'
    locators = SupportPageLocators()
    
    def hover_menu_item(self, timeout=DEFAULT_TIMEOUT):
        self.hover(locator=self.locators.MENU_ITEM, timeout=timeout)
        
    def click_help_reference(self, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.locators.REFERENCE_BUTTON, timeout=timeout)
        
    def click_suggest_idea_reference(self, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.locators.SUGGEST_IDEA_BUTTON, timeout=timeout)
        
    def assert_references_list_visible(self, timeout=DEFAULT_TIMEOUT):
        assert self.became_visible(locator=self.locators.LIST_WINDOW, timeout=timeout)
        
    def assert_reference_to_window(self, help_url, timeout=DEFAULT_TIMEOUT):
        self.go_to_new_tab()
        assert self.driver.current_url == help_url
        
    def click_open_ask_a_question(self, timeout=DEFAULT_TIMEOUT):
        self.hover_menu_item()
        self.click(locator=self.locators.ASK_QUESTION_BUTTON, timeout=timeout)
        
    def assert_ask_a_question_window_visible(self, timeout=DEFAULT_TIMEOUT):
        assert self.became_visible(locator=self.locators.MODAL_ASK_QUESTION, timeout=timeout)
        
    def click_close_ask_a_question(self, timeout=DEFAULT_TIMEOUT):
         self.click(locator=self.locators.MODAL_CLOSE_BUTTON, timeout=timeout)
         
    def assert_ask_a_question_window_invisible(self, timeout=DEFAULT_TIMEOUT):
        assert self.became_invisible(locator=self.locators.MODAL_ASK_QUESTION, timeout=timeout)
        
    def click_reference_to_help_modal(self, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.locators.MODAL_REFERENCE_TO_HELP, timeout=timeout)

    def click_choose_other_theme(self, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.locators.LIST_THEMES, timeout=timeout)
        self.click(locator=self.locators.OTHER_THEME, timeout=timeout)

    def fill_message(self, message, timeout=DEFAULT_TIMEOUT):
        self.send_keys_to_input(locator=self.locators.MESSAGE_FIELD, keys=message, timeout=timeout)
    
    def fill_name(self, name, timeout=DEFAULT_TIMEOUT):
        self.send_keys_to_input(locator=self.locators.NAME_FIELD, keys=name, timeout=timeout)
        
    def fill_email(self, email, timeout=DEFAULT_TIMEOUT):
        self.send_keys_to_input(locator=self.locators.EMAIL_FIELD, keys=email, timeout=timeout)
        
    def click_submit_question(self, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.locators.SUBMIT_QUESTION_BUTTON, timeout=timeout)
        
    def assert_successful_question(self, timeout=DEFAULT_TIMEOUT):
        assert self.became_visible(locator=self.locators.SUCCESS_MODAL, timeout=timeout)
        
    def assert_closed_modal(self, timeout=DEFAULT_TIMEOUT):
        assert self.became_invisible(locator=self.locators.SUCCESS_MODAL, timeout=timeout)
        
    def click_close_successful_modal(self, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.locators.CLOSE_SUCCESS_MODAL, timeout=timeout)
        
    def add_image(self, filename='image.png', timeout=DEFAULT_TIMEOUT):
        filepath = self._get_static_filepath(filename=filename)
        self.find(locator=self.locators.ADD_IMAGE_INPUT, timeout=timeout).send_keys(filepath)