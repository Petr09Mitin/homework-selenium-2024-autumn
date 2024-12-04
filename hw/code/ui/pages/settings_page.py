from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ui.pages.base_page import BasePage, DEFAULT_TIMEOUT
from ui.locators.settings_general_locators import SettingsGeneralLocators
from ui.locators.settings_notifications_locators import SettingsNotificationsLocators
from ui.locators.settings_access_locators import SettingsAccessLocators
from ui.locators.settings_logs_locators import SettingsLogsLocators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from datetime import date
from os import path
import time
from selenium.common.exceptions import TimeoutException

class SettingsPage(BasePage):
    url = 'https://ads.vk.com/hq/settings'
    general_locators = SettingsGeneralLocators()
    notifications_locators = SettingsNotificationsLocators()
    access_locators = SettingsAccessLocators()
    logs_locators = SettingsLogsLocators()
    
    def fill_phone_number(self, phone, timeout=DEFAULT_TIMEOUT):
        self.send_keys_to_input(locator=self.general_locators.FILL_PHONE_INPUT, keys=phone, timeout=timeout)
        
    def click_add_email(self, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.general_locators.ADD_EMAIL_BUTTON, timeout=timeout)
        
    def click_delete_email(self, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.general_locators.DELETE_ADDED_EMAIL_BUTTON, timeout=timeout)
        
    def fill_FIO(self, FIO, timeout=DEFAULT_TIMEOUT):
        self.send_keys_to_input(locator=self.general_locators.FIO_INPUT, keys=FIO, timeout=timeout)
    
    def fill_INN(self, INN, timeout=DEFAULT_TIMEOUT):
        self.send_keys_to_input(locator=self.general_locators.INN_INPUT, keys=INN, timeout=timeout)
        
    def click_show_hot_keys(self, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.general_locators.SHOW_HOT_KEYS_BUTTON, timeout=timeout)
        
    def assert_hot_keys_modal_visible(self, timeout=DEFAULT_TIMEOUT):
        assert self.became_visible(locator=self.general_locators.MODAL_HOT_KEYS, timeout=timeout)
        
    def assert_hot_keys_modal_invisible(self, timeout=DEFAULT_TIMEOUT):
        assert self.became_invisible(locator=self.general_locators.MODAL_HOT_KEYS, timeout=timeout)
        
    def close_hot_keys_modal(self, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.general_locators.CLOSE_HOT_KEYS_BUTTON, timeout=timeout)
        
    def click_exit_from_accounts(self, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.general_locators.LOGOUT_DEVICES_BUTTON, timeout=timeout)
        
    def assert_successful_logout_modal(self, timeout=DEFAULT_TIMEOUT):
        assert self.became_visible(locator=self.general_locators.LOGOUT_SUCCESSFUL, timeout=timeout)
        
    def click_save_changes(self, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.general_locators.SAVE_BUTTON, timeout=timeout)
        
    def click_decline_changes(self, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.general_locators.REMOVE_CHANGES_BUTTON, timeout=timeout)
        
    def assert_added_email_input_visible(self, email_ID, timeout=DEFAULT_TIMEOUT):
        assert self.became_visible(locator=self.general_locators.ADDED_EMAIL_INPUT(email_ID), timeout=timeout)
        
    def assert_added_email_input_invisible(self, email_ID, timeout=DEFAULT_TIMEOUT):
        assert self.became_invisible(locator=self.general_locators.ADDED_EMAIL_INPUT(email_ID), timeout=timeout)
        
    def click_more_about_api(self, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.general_locators.MORE_ABOUT_API_BUTTON, timeout=timeout)
        
    def click_connect_agency(self, timeout=DEFAULT_TIMEOUT):
        self.click(self.general_locators.CONNECT_AGENCY, timeout=timeout)
        
    def assert_agency_modal_visible(self, timeout=DEFAULT_TIMEOUT):
        assert self.became_visible(self.general_locators.MODAL_AGENCY, timeout=timeout)
        
    def assert_agency_modal_invisible(self, timeout=DEFAULT_TIMEOUT):
        assert self.became_invisible(self.general_locators.MODAL_AGENCY, timeout=timeout)
        
    def click_close_agency_modal(self, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.general_locators.CANCEL_CONNECT_AGENCY, timeout=timeout)
        
    def click_connect_agency_in_modal(self, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.general_locators.ACCEPT_CONNECT_AGENCY, timeout=timeout)
        
    def assert_not_found_agency(self, timeout=DEFAULT_TIMEOUT):
        assert self.became_visible(locator=self.general_locators.NOT_FOUND_AGENCY, timeout=timeout)
        
    def assert_empty_agency(self, timeout=DEFAULT_TIMEOUT):
        assert self.became_visible(locator=self.general_locators.EMPTY_AGENT_FIELD, timeout=timeout)
        
    def assert_incorrect_agency(self, timeout=DEFAULT_TIMEOUT):
        assert self.became_visible(locator=self.general_locators.INCORRECT_AGENCY, timeout=timeout)
    
    def fill_agency_ID(self, agency_ID, timeout=DEFAULT_TIMEOUT):
        self.send_keys_to_input(locator=self.general_locators.AGENCY_ID_INPUT, keys=agency_ID, timeout=timeout)
    
    def fill_email(self, email, email_ID, timeout=DEFAULT_TIMEOUT):
        self.find(locator=self.general_locators.ADDED_EMAIL_INPUT(email_ID), timeout=timeout).send_keys(email)
        
    def assert_empty_FIO(self, timeout=DEFAULT_TIMEOUT):
        assert self.became_visible(locator=self.general_locators.EMPTY_FIELD, timeout=timeout)
        
    def assert_incorrect_email(self, timeout=DEFAULT_TIMEOUT):
        assert self.became_visible(locator=self.general_locators.INCORRECT_EMAIL, timeout=timeout)
        
    def assert_incorrect_phone(self, timeout=DEFAULT_TIMEOUT):
        assert self.became_visible(locator=self.general_locators.INCORRECT_PHONE, timeout=timeout)
        
    def assert_incorrect_INN(self, timeout=DEFAULT_TIMEOUT):
        assert self.became_visible(locator=self.general_locators.INCORRECT_INN, timeout=timeout)
        
    def assert_unavailable_INN(self, timeout=DEFAULT_TIMEOUT):
        assert self.became_visible(locator=self.general_locators.UNAVAILABLE_INN, timeout=timeout)
        
    def assert_valid_FIO(self, timeout=DEFAULT_TIMEOUT):
        assert self.became_invisible(locator=self.general_locators.EMPTY_FIELD, timeout=timeout)
    
    def assert_correct_email(self, timeout=DEFAULT_TIMEOUT):
        assert self.became_invisible(locator=self.general_locators.INCORRECT_EMAIL, timeout=timeout)
        
    def assert_correct_phone(self, timeout=DEFAULT_TIMEOUT):
        assert self.became_invisible(locator=self.general_locators.INCORRECT_PHONE, timeout=timeout)
        
    def assert_correct_INN(self, timeout=DEFAULT_TIMEOUT):
        assert self.became_invisible(locator=self.general_locators.INCORRECT_INN, timeout=timeout)
        
    def assert_incorrect_fields(self, timeout=DEFAULT_TIMEOUT):
        self.assert_incorrect_email()
        self.assert_incorrect_phone()
        self.assert_incorrect_INN()
        
    def assert_correct_fields(self, timeout=DEFAULT_TIMEOUT):
        self.assert_valid_FIO()
        self.assert_correct_email()
        self.assert_correct_phone()
        self.assert_correct_INN()
        
    def click_notifications_tab(self, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.notifications_locators.TAB_ITEM, timeout=timeout)
        
    def click_toggle_email_notifications(self, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.notifications_locators.EMAILS_NOTIFICATIONS, timeout=timeout)
        
    def assert_warning_notifications(self, timeout=DEFAULT_TIMEOUT):
        self.became_visible(locator=self.notifications_locators.WARNING_BLOCK, timeout=timeout)
        
    def assert_warning_notifications_invisible(self, timeout=DEFAULT_TIMEOUT):
        self.became_invisible(locator=self.notifications_locators.WARNING_BLOCK, timeout=timeout)
        
    def assert_reference_to_window(self, url, timeout=DEFAULT_TIMEOUT):
        assert self.driver.current_url == url
        
    def click_attach_tg(self, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.notifications_locators.TG_NOTIFICATIONS, timeout=timeout)
        
    def assert_reference_to_blanked_window(self, url, timeout=DEFAULT_TIMEOUT):
        start = time.time()
        while time.time() - start < timeout:
            if (len(self.driver.window_handles) > 1):
                self.go_to_new_tab()
                assert ((self.driver.current_url).index(url) == 0)
                return
        assert False
        
    def click_access_tab(self, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.access_locators.TAB_ITEM, timeout=timeout)
        
    def assert_no_cabinets(self, timeout=DEFAULT_TIMEOUT):
        assert self.became_visible(locator=self.access_locators.NO_CABINETS, timeout=timeout)
        
    def click_add_cabinet(self, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.access_locators.ADD_CABINET_BUTTON, timeout=timeout)
        
    def assert_add_cabinet_modal_visible(self, timeout=DEFAULT_TIMEOUT):
        assert self.became_visible(locator=self.access_locators.MODAL_ADD_CABINET, timeout=timeout)
        
    def click_close_add_cabinet_modal(self, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.access_locators.CANCEL_ADD_CABINET, timeout=timeout)
            
    def assert_add_cabinet_modal_invisible(self, timeout=DEFAULT_TIMEOUT):
        assert self.became_invisible(locator=self.access_locators.MODAL_ADD_CABINET, timeout=timeout)
        
    def click_submit_add_cabinet(self, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.access_locators.SUBMIT_ADD_CABINET, timeout=timeout)
        
    def assert_empty_account_ID(self, timeout=DEFAULT_TIMEOUT):
        assert self.became_visible(locator=self.access_locators.EMPTY_FIELD, timeout=timeout)
        
    def fill_account_ID(self, account_ID, timeout=DEFAULT_TIMEOUT):
        self.send_keys_to_input(locator=self.access_locators.INPUT_ADD_ACCOUNT, keys=account_ID, timeout=timeout)
        
    def assert_not_found_account(self, timeout=DEFAULT_TIMEOUT):
        assert self.became_visible(locator=self.access_locators.INCORRECT_ACCOUNT_ID, timeout=timeout)
        
    def click_more_about_multiaccounts(self, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.access_locators.MORE_INFO, timeout=timeout)
        
    def assert_added_cabinet(self, account_ID, timeout=DEFAULT_TIMEOUT):
        assert self.became_visible(locator=self.access_locators.find_cabinet_by_name(account_ID), timeout=timeout)
        
    def fill_search(self, query, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.access_locators.SEARCH, timeout=timeout)
        self.send_keys_to_input(locator=self.access_locators.SEARCH, keys=query, timeout=timeout)
        
    def assert_not_found_cabinets(self, timeout=DEFAULT_TIMEOUT):
        assert self.became_visible(locator=self.access_locators.NOTHING_FOUND, timeout=timeout)
        
    def click_clear_query(self, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.access_locators.CLEAR_QUERY, timeout=timeout)
        
    def assert_not_found_cabinets_invisible(self, timeout=DEFAULT_TIMEOUT):
        assert self.became_invisible(locator=self.access_locators.NOTHING_FOUND, timeout=timeout)
        
    def create_account(self, account_ID, timeout=DEFAULT_TIMEOUT):
        self.click_access_tab()
        self.click_add_cabinet()
        self.fill_account_ID(account_ID=account_ID)
        self.click_submit_add_cabinet()
        
    def click_remove_added_cabinet(self, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.access_locators.REMOVE_CABINET, timeout=timeout)
        
    def assert_remove_cabinet_modal(self, timeout=DEFAULT_TIMEOUT):
        assert self.became_visible(locator=self.access_locators.MODAL_REMOVE_CABINET, timeout=timeout)
        
    def click_cancel_remove_cabinet_modal(self, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.access_locators.CANCEL_REMOVE_CABINET_BUTTON, timeout=timeout)
        
    def assert_remove_cabinet_modal_invisible(self, timeout=DEFAULT_TIMEOUT):
        assert self.became_invisible(locator=self.access_locators.MODAL_REMOVE_CABINET, timeout=timeout)
        
    def hover_cabinet_item(self, account_ID, timeout=DEFAULT_TIMEOUT):
        self.hover(locator=self.access_locators.find_cabinet_by_name(name=account_ID), timeout=timeout)
        
    def click_accept_remove_cabinet(self, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.access_locators.ACCEPT_REMOVE_CABINET_BUTTON, timeout=timeout)
        
    def delete_added_cabinet(self, account_ID, timeout=DEFAULT_TIMEOUT):
        self.hover_cabinet_item(account_ID=account_ID)
        self.click_remove_added_cabinet()
        self.assert_remove_cabinet_modal()
        self.click_cancel_remove_cabinet_modal()
        self.assert_remove_cabinet_modal_invisible()
        self.hover_cabinet_item(account_ID=account_ID)
        self.click_remove_added_cabinet()
        self.click_accept_remove_cabinet()
        
    def click_logs_tab(self, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.logs_locators.TAB_ITEM, timeout=timeout)
        
    def click_filter_button(self, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.logs_locators.FILTER_BUTTON, timeout=timeout)
        
    def assert_opened_filter_block(self, timeout=DEFAULT_TIMEOUT):
        assert self.became_visible(locator=self.logs_locators.OBJECT_TYPE_BUTTON, timeout=timeout)
        
    def click_close_filter_block(self, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.logs_locators.CANCEL_BUTTON, timeout=timeout)
        
    def assert_closed_filter_block(self, timeout=DEFAULT_TIMEOUT):
        assert self.became_invisible(locator=self.logs_locators.OBJECT_TYPE_BUTTON, timeout=timeout)
        
    def click_choose_all_filters(self, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.logs_locators.SELECT_ALL_BUTTON, timeout=timeout)
        
    def assert_chosen_filters(self, timeout=DEFAULT_TIMEOUT):
        assert self.became_visible(locator=self.logs_locators.RESET_ALL_BUTTON, timeout=timeout)
        
    def click_reset_all_filters(self, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.logs_locators.RESET_ALL_BUTTON, timeout=timeout)
        
    def assert_reseted_filters(self, timeout=DEFAULT_TIMEOUT):
        assert self.became_visible(locator=self.logs_locators.SELECT_ALL_BUTTON, timeout=timeout)
        
    def click_accept_filters(self, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.logs_locators.SAVE_BUTTON, timeout=timeout)
        
    def assert_filters_accepted(self, timeout=DEFAULT_TIMEOUT):
        assert self.became_visible(locator=self.logs_locators.FILTERED_GROUPS, timeout=timeout)
        
    def click_reset_filtered_groups(self, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.logs_locators.RESET_FILTERED_GROUP, timeout=timeout)
        
    def assert_filters_not_accepted(self, timeout=DEFAULT_TIMEOUT):
        assert self.became_invisible(locator=self.logs_locators.FILTERED_GROUPS, timeout=timeout)
        
    def assert_empty_logs(self, timeout=DEFAULT_TIMEOUT):
        assert self.became_visible(locator=self.logs_locators.EMPTY_LOGS_HISTORY, timeout=timeout)
        
    def assert_not_found_logs(self, timeout=DEFAULT_TIMEOUT):
        assert self.became_visible(locator=self.logs_locators.NOT_FOUND, timeout=timeout)
        
    def click_open_calendar(self, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.logs_locators.CALENDAR_BUTTON, timeout=timeout)
        
    def assert_opened_calendar(self, timeout=DEFAULT_TIMEOUT):
        assert self.became_visible(locator=self.logs_locators.CALENDAR_MODAL, timeout=timeout)
        
    def click_close_calendar(self, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.logs_locators.CALENDAR_CANCEL_BUTTON, timeout=timeout)
        
    def assert_closed_calendar(self, timeout=DEFAULT_TIMEOUT):
        assert self.became_invisible(locator=self.logs_locators.CALENDAR_MODAL, timeout=timeout)