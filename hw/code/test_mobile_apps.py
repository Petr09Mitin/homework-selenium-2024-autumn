import pytest
from base_case import BaseCase

class TestMobileApps(BaseCase):
    _reference_url = 'https://ads.vk.com/help/articles/add_app'
    _wrong_app_url = 'https://socio-project.ru'
    
    def test_add_app_modal(self, mobile_apps_page):
        mobile_apps_page.assert_no_apps()
        mobile_apps_page.click_add_app()
        mobile_apps_page.assert_adding_window_visible()
        mobile_apps_page.click_close_adding_app()
        mobile_apps_page.assert_adding_window_invisible()
    
    def test_redirecting_to_reference(self, mobile_apps_page):
        mobile_apps_page.click_add_app()
        mobile_apps_page.assert_adding_window_visible()
        mobile_apps_page.click_more_info()
        mobile_apps_page.assert_redirect_to_reference(self._reference_url)
    
    def test_wrong_name_of_app(self, mobile_apps_page):
        mobile_apps_page.click_add_app()
        mobile_apps_page.send_app_url(self._wrong_app_url)
        mobile_apps_page.assert_wrong_app_url()