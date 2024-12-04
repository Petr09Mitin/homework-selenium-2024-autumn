import pytest
from base_case import BaseCase

class TestSettings(BaseCase):
    _api_url = 'https://ads.vk.com/help/articles/help_api'
    _invalid_agency_id = '2222222222222222'
    _not_existed_agency_id = '32'
    _invalid_email = 'lolkek'
    _valid_email = 'lolkek@gmail.com'
    _incorrect_INN = '111'
    _unavailable_INN = 'asd'
    _correct_INN = '1' * 12
    _invalid_phone = '885'
    _valid_phone = '+79031111111'
    _valid_FIO = 'Эрих Мария Ремарк'
    
    _notifications_url = 'https://ads.vk.com/hq/settings/notifications'
    _notifications_tg_url= 'https://t.me/vkadssenderbot?start='
    
    _access_url = 'https://ads.vk.com/hq/settings/access'
    _access_incorrect_account_ID = '32'
    _access_correct_account_ID = '22766168'
    _access_more_info_url = 'https://ads.vk.com/help/articles/additionalaccounts'
    _access_not_existed_cabinet = 'lolkek'
    
    _logs_url = 'https://ads.vk.com/hq/settings/logs'
    
    def test_reference_to_api(self, settings_page):
        settings_page.click_more_about_api()
        settings_page.assert_reference_to_blanked_window(self._api_url)
        
    def test_agency(self, settings_page):
        settings_page.click_connect_agency()
        settings_page.assert_agency_modal_visible()
        settings_page.click_close_agency_modal()
        settings_page.assert_agency_modal_invisible()
        settings_page.click_connect_agency()
        settings_page.click_connect_agency_in_modal()
        settings_page.assert_empty_agency()
        settings_page.fill_agency_ID(self._invalid_agency_id)
        settings_page.click_connect_agency_in_modal()
        settings_page.assert_incorrect_agency()
        settings_page.fill_agency_ID(self._not_existed_agency_id)
        settings_page.click_connect_agency_in_modal()
        settings_page.assert_not_found_agency()
        
    def test_general_fields(self, settings_page):
        settings_page.click_show_hot_keys()
        settings_page.assert_hot_keys_modal_visible()
        settings_page.close_hot_keys_modal()
        settings_page.assert_hot_keys_modal_invisible()
        
        settings_page.click_add_email()
        settings_page.assert_added_email_input_visible(0)
        settings_page.click_delete_email()
        settings_page.assert_added_email_input_invisible(0)
        settings_page.click_add_email()
        
        settings_page.fill_phone_number(self._invalid_phone)
        settings_page.fill_INN(self._incorrect_INN)
        settings_page.fill_email(self._invalid_email, 0)
        settings_page.click_save_changes()
        settings_page.assert_incorrect_fields()
        
        settings_page.fill_phone_number(self._valid_phone)
        settings_page.fill_email(self._valid_email, 0)
        settings_page.fill_FIO(self._valid_FIO)
        settings_page.fill_INN(self._correct_INN)
        settings_page.assert_correct_fields()
        
        settings_page.fill_INN(self._unavailable_INN)
        settings_page.assert_unavailable_INN()
        settings_page.click_decline_changes()
        settings_page.assert_correct_INN()
        
    def test_notifications_warning(self, settings_page):
        settings_page.click_notifications_tab()
        settings_page.assert_reference_to_window(self._notifications_url)
        settings_page.click_toggle_email_notifications()
        settings_page.assert_warning_notifications()
        settings_page.click_toggle_email_notifications()
        settings_page.assert_warning_notifications_invisible()
        settings_page.click_attach_tg()
        settings_page.assert_reference_to_blanked_window(self._notifications_tg_url)
    
    def test_negative_access(self, settings_page):
        settings_page.click_access_tab()
        settings_page.assert_no_cabinets()
        settings_page.click_add_cabinet()
        settings_page.assert_add_cabinet_modal_visible()
        settings_page.click_close_add_cabinet_modal()
        settings_page.assert_add_cabinet_modal_invisible()
        settings_page.click_add_cabinet()
        settings_page.click_submit_add_cabinet()
        settings_page.assert_empty_account_ID()
        settings_page.fill_account_ID(self._access_incorrect_account_ID)
        settings_page.click_submit_add_cabinet()
        settings_page.assert_not_found_account()
        
    def test_more_about_multiaccounts(self, settings_page):
        settings_page.click_access_tab()
        settings_page.assert_reference_to_window(self._access_url)
        settings_page.click_more_about_multiaccounts()
        settings_page.assert_reference_to_blanked_window(self._access_more_info_url)
    
    def test_add_and_delete_cabinet(self, settings_page):
        settings_page.create_account(self._access_correct_account_ID)
        settings_page.assert_added_cabinet(self._access_correct_account_ID)
        settings_page.fill_search(self._access_not_existed_cabinet)
        settings_page.assert_not_found_cabinets()
        settings_page.click_clear_query()
        settings_page.assert_not_found_cabinets_invisible()
        settings_page.delete_added_cabinet(self._access_correct_account_ID)
        settings_page.assert_no_cabinets()
        
    def test_logs(self, settings_page):
        settings_page.click_logs_tab()
        settings_page.assert_reference_to_window(self._logs_url)
        settings_page.click_filter_button()
        settings_page.assert_opened_filter_block()
        settings_page.click_close_filter_block()
        settings_page.assert_closed_filter_block()
        settings_page.click_filter_button()
        settings_page.click_choose_all_filters()
        settings_page.assert_chosen_filters()
        settings_page.click_reset_all_filters()
        settings_page.assert_reseted_filters()
        settings_page.click_choose_all_filters()
        settings_page.click_accept_filters()
        settings_page.assert_closed_filter_block()
        settings_page.assert_filters_accepted()
        settings_page.click_reset_filtered_groups()
        settings_page.assert_filters_not_accepted()