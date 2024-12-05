import pytest
from base_case import BaseCase

class TestSites(BaseCase):
    _wrong_domain_site = "kas"
    _correct_domain_site = 'https://socio-project.ru'
    
    _valid_event_name = 'lolkekeshkere'
    
    _audience_name = "ahaha yeah"
    
    def test_create_and_delete_pixel(self, sites_page):
        sites_page.assert_noone_pixels()
        sites_page.click_add_pixel()
        sites_page.assert_add_pixel_modal()
        sites_page.fill_site_domain(self._wrong_domain_site)
        sites_page.click_add_site_modal()
        sites_page.assert_wrong_site_domain()
        sites_page.create_pixel(self._correct_domain_site)
        sites_page.assert_created_pixel_item()
        sites_page.delete_pixel()
        
    def test_diagnostic(self, sites_page):
        sites_page.click_add_pixel()
        sites_page.create_pixel(self._correct_domain_site)
        sites_page.click_go_to_pixel_settings()
        sites_page.click_go_to_diagnostic()
        sites_page.assert_diagnostic_window_opened()
        sites_page.click_check_site()
        sites_page.assert_diagnostic_is_working()
        sites_page.go_to_pixel_list()
        sites_page.delete_pixel()
    
    def test_audience(self, sites_page):
        sites_page.click_add_pixel()
        sites_page.create_pixel(self._correct_domain_site)
        sites_page.click_go_to_pixel_settings()
        sites_page.click_audience_tab()
        sites_page.assert_not_enough_audience()
        sites_page.go_to_pixel_list()
        sites_page.delete_pixel()
    
    def test_pixel_code(self, sites_page):
        sites_page.click_add_pixel()
        sites_page.create_pixel(self._correct_domain_site)
        sites_page.click_go_to_pixel_settings()
        sites_page.click_pixel_code()
        sites_page.assert_code_pixel_window_opened()
        sites_page.click_gather_data_layer()
        sites_page.assert_gathering_data_description()
        sites_page.click_syncronize_customers()
        sites_page.assert_syncronization_description()
        sites_page.click_show_instruction()
        sites_page.assert_instruction_modal_opened()
        sites_page.click_close_instruction_modal()
        sites_page.assert_instruction_modal_closed()
        sites_page.go_to_pixel_list()
        sites_page.delete_pixel()
        
    def test_audience_tags(self, sites_page):
        sites_page.click_add_pixel()
        sites_page.create_pixel(self._correct_domain_site)
        sites_page.click_go_to_pixel_settings()
        sites_page.click_audience_tags()
        sites_page.assert_no_audience_tags()
        sites_page.click_create_audience_tags()
        sites_page.assert_create_audience_tags_modal()
        sites_page.click_close_audience_tags_modal()
        sites_page.assert_closed_audience_tags_modal()
        sites_page.click_create_audience_tags()
        sites_page.fill_create_audience_tag(self._audience_name)
        sites_page.click_accept_create_audience_tags_modal()
        sites_page.assert_created_audience_tag()
        sites_page.go_to_pixel_list()
        sites_page.delete_pixel()