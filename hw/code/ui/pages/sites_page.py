from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ui.pages.base_page import BasePage, DEFAULT_TIMEOUT
from ui.locators.sites_locators import SitePageLocators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from datetime import date
from os import path
import time
from selenium.common.exceptions import TimeoutException

class SitesPage(BasePage):
    url = 'https://ads.vk.com/hq/pixels'
    locators = SitePageLocators()
    
    def assert_noone_pixels(self, timeout=DEFAULT_TIMEOUT):
        assert self.became_visible(locator=self.locators.NOONE_PIXELS, timeout=timeout)
        
    def click_add_pixel(self, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.locators.ADD_PIXEL_BUTTON, timeout=timeout)
        
    def assert_add_pixel_modal(self, timeout=DEFAULT_TIMEOUT):
        assert self.became_visible(locator=self.locators.MODAL_ADD_PIXEL, timeout=timeout)
        
    def fill_site_domain(self, domain, timeout=DEFAULT_TIMEOUT):
        self.send_keys_to_input(locator=self.locators.INPUT_SITE_DOMAIN, keys=domain, timeout=timeout)
        
    def click_add_site_modal(self, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.locators.ADD_SITE_BUTTON, timeout=timeout)
        
    def assert_wrong_site_domain(self, timeout=DEFAULT_TIMEOUT):
        assert self.became_visible(locator=self.locators.INCORRECT_SITE_DOMAIN, timeout=timeout)
        
    def click_add_new_pixel(self, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.locators.ADD_NEW_PIXEL_BUTTON, timeout=timeout)
        
    def assert_created_pixel_modal(self, timeout=DEFAULT_TIMEOUT):
        assert self.became_visible(locator=self.locators.CREATED_PIXEL_MODAL, timeout=timeout)
        
    def click_close_created_pixel_modal(self, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.locators.CLOSE_CREATED_PIXEL_MODAL, timeout=timeout)
        
    def assert_created_pixel_item(self, timeout=DEFAULT_TIMEOUT):
        assert self.became_visible(locator=self.locators.PIXEL_ITEM_RAW, timeout=timeout)
        
    def hover_pixel_raw_item(self, timeout=DEFAULT_TIMEOUT):
        self.hover(locator=self.locators.PIXEL_ITEM_RAW, timeout=timeout)
        
    def hover_more_item(self, timeout=DEFAULT_TIMEOUT):
        self.hover(locator=self.locators.PIXEL_ITEM_MORE_SYMBOL, timeout=timeout)
        
    def click_more_item(self, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.locators.PIXEL_ITEM_MORE_SYMBOL, timeout=timeout)
        
    def click_remove_pixel(self, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.locators.REMOVE_PIXEL_BUTTON, timeout=timeout)
        
    def assert_remove_pixel_modal(self, timeout=DEFAULT_TIMEOUT):
        assert self.became_visible(locator=self.locators.REMOVE_PIXEL_MODAL, timeout=timeout)
        
    def click_accept_remove_pixel(self, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.locators.ACCEPT_REMOVE_PIXEL_BUTTON, timeout=timeout)
        
    def create_pixel(self, domain_site, timeout=DEFAULT_TIMEOUT):
        self.fill_site_domain(domain=domain_site)
        self.click_add_site_modal()
        self.click_add_new_pixel()
        self.assert_created_pixel_modal()
        self.click_close_created_pixel_modal()
        
    def delete_pixel(self, timeout=DEFAULT_TIMEOUT):
        self.hover_pixel_raw_item()
        self.hover_more_item()
        self.click_more_item()
        self.click_remove_pixel()
        self.assert_remove_pixel_modal()
        self.click_accept_remove_pixel()
        
    def click_go_to_pixel_settings(self, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.locators.PIXEL_SETTINGS_BUTTON, timeout=timeout)
        
    def click_go_to_diagnostic(self, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.locators.SITE_DIAGNOSTIC_TAB, timeout=timeout)
        
    def assert_diagnostic_window_opened(self, timeout=DEFAULT_TIMEOUT):
        assert self.became_visible(locator=self.locators.NO_DIAGNOSTIC_EARLIER, timeout=timeout)
        
    def click_check_site(self, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.locators.CHECK_SITE, timeout=timeout)
        
    def assert_diagnostic_is_working(self, timeout=DEFAULT_TIMEOUT):
        assert self.became_invisible(locator=self.locators.NO_DIAGNOSTIC_EARLIER, timeout=timeout)
        
    def click_audience_tab(self, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.locators.SITE_AUDIENCE_TAB, timeout=timeout)
        
    def assert_not_enough_audience(self, timeout=DEFAULT_TIMEOUT):
        assert self.became_visible(locator=self.locators.NOT_ENOUGH_AUDIENCE, timeout=timeout)
        
    def go_to_pixel_list(self, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.locators.MENU_ITEM, timeout=timeout)
        
    def click_pixel_code(self, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.locators.SITE_CODE_TAB, timeout=timeout)
        
    def assert_code_pixel_window_opened(self, timeout=DEFAULT_TIMEOUT):
        assert self.became_visible(locator=self.locators.GATHERING_DATA_LAYER_INPUT, timeout=timeout)
        
    def click_gather_data_layer(self, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.locators.GATHERING_DATA_LAYER_INPUT, timeout=timeout)
        
    def assert_gathering_data_description(self, timeout=DEFAULT_TIMEOUT):
        assert self.became_visible(locator=self.locators.GATHERING_DATA_DESCRIBING, timeout=timeout)
        
    def click_syncronize_customers(self, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.locators.SYNCRONIZATION_INPUT, timeout=timeout)
        
    def assert_syncronization_description(self, timeout=DEFAULT_TIMEOUT):
        assert self.became_visible(locator=self.locators.SYNCRONIZATION_DESCRIBING, timeout=timeout)
        
    def click_show_instruction(self, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.locators.INSTRUCTION_BUTTON, timeout=timeout)
        
    def assert_instruction_modal_opened(self, timeout=DEFAULT_TIMEOUT):
        assert self.became_visible(locator=self.locators.INSTRUCTION_MODAL, timeout=timeout)
        
    def click_close_instruction_modal(self, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.locators.CLOSE_INSTRUCTION_MODAL, timeout=timeout)
        
    def assert_instruction_modal_closed(self, timeout=DEFAULT_TIMEOUT):
        assert self.became_invisible(locator=self.locators.INSTRUCTION_MODAL, timeout=timeout)
        
    def click_pixel_events(self, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.locators.SITE_EVENTS_TAB, timeout=timeout)
        
    def assert_pixel_events_window_opened(self, timeout=DEFAULT_TIMEOUT):
        assert self.became_visible(locator=self.locators.NO_EVENTS, timeout=timeout)
        
    def click_add_pixel_event(self, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.locators.ADD_EVENT_BUTTON, timeout=timeout)
        
    def assert_add_pixel_event_window_opened(self, timeout=DEFAULT_TIMEOUT):
        assert self.became_visible(locator=self.locators.NAME_EVENT_INPUT, timeout=timeout)
        
    def fill_event_name(self, name, timeout=DEFAULT_TIMEOUT):
        self.send_keys_to_input(locator=self.locators.NAME_EVENT_INPUT, keys=name, timeout=timeout)
        
    def click_accept_add_event(self, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.locators.ACCEPT_ADD_EVENT_BUTTON, timeout=timeout)
        
    def fill_new_event_fields(self, name, timeout=DEFAULT_TIMEOUT):
        self.fill_event_name(name=name)
        self.click(locator=self.locators.PURCHASE_CATEGORY_OPTION, timeout=timeout)
        self.click(locator=self.locators.PAGE_VISITED_OPTION, timeout=timeout)
        self.send_keys_to_input(locator=self.locators.URL_EVENT_INPUT, keys=name, timeout=timeout)
        self.click_accept_add_event()