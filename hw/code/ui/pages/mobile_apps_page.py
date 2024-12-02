from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC
from ui.pages.base_page import BasePage, DEFAULT_TIMEOUT
from ui.locators.mobile_apps import MobileAppsLocators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from datetime import date
from os import path
from selenium.common.exceptions import TimeoutException

class MobileAppsPage(BasePage):
    url = 'https://ads.vk.com/hq/apps'
    locators = MobileAppsLocators()
    
    def click_add_app(self, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.locators.ADD_APP_BUTTON, timeout=timeout)
        
    def click_close_adding_app(self, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.locators.MODAL_CLOSE_BUTTON, timeout=timeout)
        
    def assert_adding_window_visible(self, timeout=DEFAULT_TIMEOUT):
        assert self.became_visible(locator=self.locators.MODAL_ADD_APP, timeout=timeout) 
        
    def assert_adding_window_invisible(self, timeout=DEFAULT_TIMEOUT):
        assert self.became_invisible(locator=self.locators.MODAL_ADD_APP, timeout=timeout) 

    def assert_no_apps(self, timeout=DEFAULT_TIMEOUT):
        assert self.became_visible(locator=self.locators.NO_APPS_HEADER, timeout=timeout)
    
    def click_more_info(self, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.locators.MORE_ABOUT_APP, timeout=timeout)
        
    def assert_redirect_to_reference(self, reference_url, timeout=DEFAULT_TIMEOUT):
        self.go_to_new_tab()
        assert self.driver.current_url == reference_url
        
    def enter_app_url(self, app_url, timeout=DEFAULT_TIMEOUT):
        self.send_keys_to_input(locator=self.locators.INPUT_ADD_APP, keys=app_url, timeout=timeout)
        
    def click_add_app_url(self, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.locators.MODAL_ADD_APP_BUTTON, timeout=timeout)
        
    def send_app_url(self, app_url, timeout=DEFAULT_TIMEOUT):
        self.enter_app_url(app_url=app_url)
        self.click_add_app_url()

    def assert_wrong_app_url(self, timeout=DEFAULT_TIMEOUT):
        assert self.became_visible(locator=self.locators.WRONG_LINK, timeout=timeout)