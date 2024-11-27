from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ui.pages.base_page import BasePage
from ui.locators.campaigns_page_locators import CampaignPageLocators
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from datetime import date
from os import path
from selenium.common.exceptions import TimeoutException

class TargetActions():
    SITE = 'site'
    CATALOGUE = 'catalogue'

class CampaignsPage(BasePage):
    url = 'https://ads.vk.com/hq/dashboard'
    locators = CampaignPageLocators()
    target_actions = TargetActions()
    
    def click_learning_modal_dismiss(self, timeout=1):
        self.click(self.locators.LEARNING_MODAL_DISMISS_BUTTON, timeout=timeout)
    
    def click_create_campaign_button(self, timeout=15):
        self.click(self.locators.CREATE_CAMPAIGN_BUTTON, timeout=timeout)
    
    def enter_campaign_name(self, name, timeout=15):
        self.click(locator=self.locators.CAMPAIGN_NAME_INPUT, timeout=timeout)
        ActionChains(self.driver).send_keys(name+Keys.ENTER).perform()
    
    def click_target_action(self, action, timeout=15):
        locator = None
        if action == self.target_actions.SITE:
           locator = self.locators.SITE_OPTION 
        elif action == self.target_actions.CATALOGUE:
            locator = self.locators.CATALOGUE_OPTION
        else:
            raise ValueError("incorrect target action")
        self.click(locator=locator, timeout=timeout)
    
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
    
    def enter_start_date(self, date, timeout=15):
        self.click(self.locators.START_DATE, timeout=timeout)
        ActionChains(self.driver).send_keys(date+Keys.ENTER).perform()

    def enter_end_date(self, date, timeout=15):
        self.click(self.locators.END_DATE, timeout=timeout)
        ActionChains(self.driver).send_keys(date+Keys.ENTER).perform()

    def click_continue(self, timeout=15):
        self.click(self.locators.CONTINUE, timeout=timeout)
    
    def click_region(self, timeout=15):
        self.click(locator=self.locators.REGION, timeout=timeout)
    
    def enter_ad_header(self, name):
        inp = self.find(locator=self.locators.AD_HEADER)
        inp.clear()
        inp.send_keys(name+Keys.ENTER)
    
    def wait_until_ad_logo_loaded(self, timeout=50):
        WebDriverWait(self.driver, timeout=timeout).until(
            EC.visibility_of_element_located(self.locators.AD_LOGO_PREVIEW)
        )
    
    def click_close_button(self, timeout=15):
        self.click(locator=self.locators.CLOSE_BUTTON, timeout=timeout)
    
    def enter_ad_header(self, header, timeout=15):
        self.click(locator=self.locators.AD_HEADER, timeout=timeout)
        ActionChains(self.driver).send_keys(header+Keys.ENTER).perform()
    
    def enter_short_description(self, description, timeout=15):
        self.click(locator=self.locators.AD_SHORT_DESCRIPTION, timeout=timeout)
        ActionChains(self.driver).send_keys(description+Keys.ENTER).perform()
    
    def load_media(self, filename, timeout=15):
        filepath = self._get_static_filepath(filename=filename)
        self.find(locator=self.locators.ADD_MEDIA_FILE_INPUT, timeout=timeout).send_keys(filepath)
        WebDriverWait(self.driver, 50).until(
            EC.invisibility_of_element_located(self.locators.MEDIA_PLACEHOLDER)
        )
    
    def click_publish(self, timeout=15):
        self.click(locator=self.locators.PUBLISH_BUTTON, timeout=timeout)
        
    def get_campaign_name_element(self, name, timeout=15):
        campaign_name_locator = CampaignPageLocators.get_campaign_name_locator(name='test')
        WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located(campaign_name_locator)
        )
        return self.find(locator=campaign_name_locator, timeout=timeout)
    
    def hover_actions_icon(self, timeout=15):
        self.hover(self.locators.ACTIONS_ICON)
        
    def delete_campaign(self, timeout=15):
        self.hover_actions_icon(timeout=timeout)
        self.click(self.locators.DELETE_BUTTON)
    
    def delete_campaign(self, name, timeout=15):
        campaign_name_locator = CampaignPageLocators.get_campaign_name_locator(name=name)
        campaign_name = self.find(locator=campaign_name_locator, timeout=timeout)
        self.click(locator=campaign_name_locator, timeout=timeout)
        self.hover_actions_icon(timeout=timeout)
        self.click(self.locators.DELETE_BUTTON)
    
    def create_campaign(self):
        try:
            self.click_learning_modal_dismiss()
        except TimeoutException:
            pass
        self.click_create_campaign_button()
        self.enter_campaign_name('test')
        self.click_target_action(self.target_actions.SITE)
        self.enter_site_url('https://vk.com')
        self.enter_budget('1000')
        self.enter_start_date(date.today().strftime('%d.%m.%Y'))
        self.enter_end_date(date.today().strftime('%d.%m.%Y'))
        self.click_continue()
        self.click_region()
        self.click_continue()
        self.enter_ad_header(header='header')
        self.enter_short_description(description='description')
        self.wait_until_ad_logo_loaded()
        self.load_media(filename='var103.jpg')
        self.click_publish()
        campaign_name = self.get_campaign_name_element(name='test')
        assert campaign_name.is_displayed()
        assert campaign_name.text == 'test'
        self.delete_campaign(name='test')
        