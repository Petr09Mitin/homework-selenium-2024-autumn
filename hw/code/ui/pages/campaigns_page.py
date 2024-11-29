from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ui.pages.base_page import BasePage, DEFAULT_TIMEOUT
from ui.locators.campaigns_page_locators import CampaignPageLocators
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from datetime import date
from os import path
from selenium.common.exceptions import TimeoutException

class TargetActions():
    SITE = 'site'
    GROUP = 'group'

class CampaignsPage(BasePage):
    url = 'https://ads.vk.com/hq/dashboard'
    locators = CampaignPageLocators()
    target_actions = TargetActions()
    
    def click_learning_modal_dismiss(self, timeout=1):
        try:
            self.click(self.locators.LEARNING_MODAL_DISMISS_BUTTON, timeout=timeout)
        except TimeoutException:
            pass
    
    def click_create_campaign_button(self, timeout=DEFAULT_TIMEOUT):
        self.click(self.locators.CREATE_CAMPAIGN_BUTTON, timeout=timeout)
    
    def enter_campaign_name(self, name, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.locators.CAMPAIGN_NAME_INPUT, timeout=timeout)
        ActionChains(self.driver).send_keys(name+Keys.ENTER).perform()
    
    def click_target_action(self, action, timeout=DEFAULT_TIMEOUT):
        locator = None
        if action == self.target_actions.SITE:
           locator = self.locators.SITE_OPTION 
        elif action == self.target_actions.GROUP:
            locator = self.locators.GROUP_OPTION
        else:
            raise ValueError("incorrect target action")
        self.click(locator=locator, timeout=timeout)
        
    def select_target_group(self, group_tag, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.locators.GROUP_SELECTOR, timeout=timeout)
        self.click(locator=self.locators.ENTER_OTHER_GROUP, timeout=timeout)
        ActionChains(self.driver).send_keys(group_tag).perform()
        self.click(locator=self.locators.ADD_GROUP_BUTTON, timeout=timeout)
    
    def enter_site_url(self, url):
        inp = self.find(locator=self.locators.ADVERTISED_SITE_FIELD)
        inp.clear()
        inp.send_keys(url+Keys.ENTER)
    
    def enter_budget(self, budget_value):
        budget_field = self.find(self.locators.BUDGET)
        budget_field.clear()
        budget_field.send_keys(budget_value)
        
        budget_value_without_currency = budget_field.get_attribute("value").replace('₽', '')
        
        WebDriverWait(self.driver, 20).until(
            lambda driver: budget_value_without_currency in budget_field.get_attribute("value")
        )
    
    def enter_start_date(self, date, timeout=DEFAULT_TIMEOUT):
        self.click(self.locators.START_DATE, timeout=timeout)
        ActionChains(self.driver).send_keys(date+Keys.ENTER).perform()

    def enter_end_date(self, date, timeout=DEFAULT_TIMEOUT):
        self.click(self.locators.END_DATE, timeout=timeout)
        ActionChains(self.driver).send_keys(date+Keys.ENTER).perform()

    def click_continue(self, timeout=DEFAULT_TIMEOUT):
        self.click(self.locators.CONTINUE, timeout=timeout)
    
    def click_region(self, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.locators.REGION, timeout=timeout)
    
    def enter_ad_header(self, name):
        inp = self.find(locator=self.locators.AD_HEADER)
        inp.clear()
        inp.send_keys(name+Keys.ENTER)
    
    def wait_until_ad_logo_loaded(self, timeout=50):
        WebDriverWait(self.driver, timeout=timeout).until(
            EC.visibility_of_element_located(self.locators.AD_LOGO_PREVIEW)
        )
    
    def click_close_button(self, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.locators.CLOSE_BUTTON, timeout=timeout)
    
    def enter_ad_header(self, header, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.locators.AD_HEADER, timeout=timeout)
        ActionChains(self.driver).send_keys(header+Keys.ENTER).perform()
    
    def enter_short_description(self, description, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.locators.AD_SHORT_DESCRIPTION, timeout=timeout)
        ActionChains(self.driver).send_keys(description+Keys.ENTER).perform()
    
    def load_media(self, filename='image.png', timeout=DEFAULT_TIMEOUT):
        filepath = self._get_static_filepath(filename=filename)
        self.find(locator=self.locators.ADD_MEDIA_FILE_INPUT, timeout=timeout).send_keys(filepath)
        WebDriverWait(self.driver, 50).until(
            EC.invisibility_of_element_located(self.locators.MEDIA_PLACEHOLDER)
        )
    
    def click_publish(self, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.locators.PUBLISH_BUTTON, timeout=timeout)
        
    def get_campaign_name_element(self, name, timeout=DEFAULT_TIMEOUT):
        campaign_name_locator = CampaignPageLocators.get_campaign_name_locator(name=name)
        WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located(campaign_name_locator)
        )
        return self.find(locator=campaign_name_locator, timeout=timeout)
    
    def hover_actions_icon(self, timeout=DEFAULT_TIMEOUT):
        self.hover(self.locators.ACTIONS_ICON)
    
    def enter_description(self, description, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.locators.DESCRIPTION, timeout=timeout)
        ActionChains(self.driver).send_keys(description+Keys.ENTER).perform()
    
    def click_confirm(self, timeout=5):
        try:
            self.click(locator=self.locators.CONFIRM_CAMPAIGN, timeout=timeout)
        except TimeoutException:
            pass
    
    def click_shot_in_video(self, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.locators.SHOT_IN_VIDEO, timeout=timeout)
    
    def delete_campaign(self, name, timeout=DEFAULT_TIMEOUT):
        campaign_name_locator = CampaignPageLocators.get_campaign_name_locator(name=name)
        campaign_name = self.find(locator=campaign_name_locator, timeout=timeout)
        self.click(locator=campaign_name_locator, timeout=timeout)
        self.hover_actions_icon(timeout=timeout)
        self.click(self.locators.DELETE_BUTTON)
        self.click(locator=self.locators.CAMPAIGNS_MENU_TAB, timeout=timeout)
    
    def go_to_create_campaign(self):
        self.click_learning_modal_dismiss()
        self.click_create_campaign_button()
        
    def assert_campaign_visible(self, name):
        campaign_name = self.get_campaign_name_element(name=name)
        assert campaign_name.is_displayed()
        assert campaign_name.text == name
    
    def assert_campaign_not_visible(self, name):
        campaign_name_locator = CampaignPageLocators.get_campaign_name_locator(name=name)
        assert self.became_invisible(locator=campaign_name_locator)
    
    def enter_dates(self, start_date=date.today().strftime('%d.%m.%Y'), end_date=date.today().strftime('%d.%m.%Y')):
        self.enter_start_date(start_date)
        self.enter_end_date(end_date)
    
    def create_campaign_site(self, name, url, budget, header, description):
        self.go_to_create_campaign()
        self.enter_campaign_name(name)
        self.click_target_action(self.target_actions.SITE)
        self.enter_site_url(url=url)
        self.enter_budget(budget)
        self.enter_dates()
        self.click_continue()
        self.click_region()
        self.click_continue()
        self.enter_ad_header(header=header)
        self.enter_short_description(description=description)
        self.wait_until_ad_logo_loaded()
        self.load_media()
        self.click_publish()
    
    def create_campaign_group(self, name, group_tag, description):
        self.go_to_create_campaign()
        self.enter_campaign_name(name)
        self.click_target_action(self.target_actions.GROUP)
        self.select_target_group(group_tag)
        self.enter_dates()
        self.click_continue()
        self.click_region()
        self.click_continue()
        self.enter_description(description=description)
        self.wait_until_ad_logo_loaded()
        self.click_shot_in_video()
        self.load_media()
        self.click_publish()
        self.click_confirm()
    
    def search_for_campaign(self, name, timeout=DEFAULT_TIMEOUT):
        inp = self.find(locator=self.locators.SEARCH_INPUT, timeout=timeout)
        inp.send_keys(name+Keys.ENTER)

    def clear_search(self, timeout=DEFAULT_TIMEOUT):
        self.click(self.locators.FILTER_BUTTON, timeout=timeout)
        self.click(self.locators.FILTERS_RESET_BUTTON, timeout=timeout)
        self.click(self.locators.FILTERS_APPLY_BUTTON, timeout=timeout)
    
    def create_folder(self, name, timeout=DEFAULT_TIMEOUT):
        pass
    
    def assert_folder_visible(self, name, timeout=DEFAULT_TIMEOUT):
        pass
    
    def delete_folder(self, name, timeout=DEFAULT_TIMEOUT):
        pass
        