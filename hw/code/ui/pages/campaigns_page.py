from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ui.pages.base_page import BasePage
from ui.locators.campaigns_page_locators import CampaignPageLocators
import time

class TargetActions():
    SITE = 'site'
    CATALOGUE = 'catalogue'

class CampaignsPage(BasePage):
    url = 'https://ads.vk.com/hq/dashboard'
    locators = CampaignPageLocators()
    target_actions = TargetActions()
    
    def click_create_campaign_button(self, timeout=15):
        pass
    
    def enter_campaign_name(self, name):
        pass
    
    def click_target_action(self, action):
        if action == self.target_actions.SITE:
            pass
        elif action == self.target_actions.CATALOGUE:
            pass
        else:
            raise ValueError("incorrect target action")
    
    def enter_site_url(self, url):
        pass
    
    def enter_budget(self, budget):
        pass
    
    def enter_dates(self, start_date, end_date):
        pass

    def click_continue(self):
        pass
    
    def enter_ad_group_name(self, name):
        pass
    
    def enter_region(self, region):
        pass
    
    def enter_ad_name(self, name):
        pass
    
    def load_ad_logo(self, filename):
        pass
    
    def enter_ad_header(self, header):
        pass
    
    def enter_short_description(self, description):
        pass
    
    def click_publish(self):
        pass
    
    def create_campaign(self):
        pass
    