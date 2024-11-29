import pytest
from base_case import BaseCase
from datetime import date
import time

class TestCampaigns(BaseCase):
    _valid_name = 'test'
    _valid_name2 = 'name2'
    _valid_url = 'https://vk.com'
    _valid_budget = '1000'
    _valid_header = 'header'
    _valid_description = 'description'
    _valid_group_tag = 'svoya__kultura'
    _valid_folder_name = 'folder1'
    
    # def test_create_campaign_site(self, campaigns_page):
    #     campaigns_page.create_campaign_site(
    #         name=self._valid_name, 
    #         url=self._valid_url, 
    #         budget=self._valid_budget, 
    #         header=self._valid_header, 
    #         description=self._valid_description,
    #     )
    #     campaigns_page.assert_campaign_visible(self._valid_name)
    #     campaigns_page.delete_campaign(name=self._valid_name)
        
    # def test_create_campaign_group(self, campaigns_page):
    #     campaigns_page.create_campaign_group(
    #         name=self._valid_name, 
    #         group_tag=self._valid_group_tag, 
    #         description=self._valid_description,
    #     )
    #     campaigns_page.assert_campaign_visible(self._valid_name)
    #     campaigns_page.delete_campaign(name=self._valid_name)
    
    # def test_search(self, campaigns_page):
    #     time.sleep(30)
    #     campaigns_page.create_campaign_site(
    #         name=self._valid_name, 
    #         url=self._valid_url, 
    #         budget=self._valid_budget, 
    #         header=self._valid_header, 
    #         description=self._valid_description,
    #     )
    #     campaigns_page.create_campaign_site(
    #         name=self._valid_name2, 
    #         url=self._valid_url, 
    #         budget=self._valid_budget, 
    #         header=self._valid_header, 
    #         description=self._valid_description,
    #     )
        
    #     campaigns_page.assert_campaign_visible(self._valid_name)
    #     campaigns_page.assert_campaign_visible(self._valid_name2)
        
    #     campaigns_page.search_for_campaign(name=self._valid_name)
        
    #     campaigns_page.assert_campaign_visible(name=self._valid_name)
    #     campaigns_page.assert_campaign_not_visible(name=self._valid_name2)
        
    #     campaigns_page.clear_search()
    #     campaigns_page.delete_campaign(name=self._valid_name)
    #     campaigns_page.delete_campaign(name=self._valid_name2)
    
    def test_create_folder(self):
        campaigns_page.create_folder(name=self._valid_folder_name)
        campaigns_page.assert_folder_visible(name=self._valid_folder_name)
        campaigns_page.delete_folder(name=self._valid_folder_name)
