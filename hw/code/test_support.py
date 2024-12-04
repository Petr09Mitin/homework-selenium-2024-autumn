import pytest
from base_case import BaseCase

class TestSupport(BaseCase):
    _help_url = 'https://ads.vk.com/help'
    _suggest_idea_url = 'https://ads.vk.com/upvote'
    _message = "All is awesome!"
    _email = "lexagorbunov14@gmail.com"
    _name = 'Эрих Мария Ремарк'
    
    def test_reference_to_help(self, support_page):
        support_page.hover_menu_item()
        support_page.assert_references_list_visible()
        support_page.click_help_reference()
        support_page.assert_reference_to_window(self._help_url)
        
    def test_reference_to_suggest_idea(self, support_page):
        support_page.hover_menu_item()
        support_page.assert_references_list_visible()
        support_page.click_suggest_idea_reference()
        support_page.assert_reference_to_window(self._suggest_idea_url)
        
    # These tests are commented because there is unpredictable site behavior after clicking "Ask a question" button
    # def test_ask_a_question_modal(self, support_page):
    #     support_page.click_open_ask_a_question()
    #     support_page.assert_ask_a_question_window_visible()
    #     support_page.click_close_ask_a_question()
    #     support_page.assert_ask_a_question_window_invisible()
        
    # def test_reference_to_help_from_modal(self, support_page):
    #     support_page.click_open_ask_a_question()
    #     support_page.click_reference_to_help_modal()
    #     support_page.assert_reference_to_window(self._help_url)
        
    # def test_success_question(self, support_page):
    #     support_page.click_open_ask_a_question()
    #     support_page.click_choose_other_theme()
    #     support_page.fill_message()
    #     support_page.fill_name()
    #     support_page.fill_email()
    #     support_page.add_image()
    #     support_page.click_submit_question()
    #     support_page.assert_successful_question()
    #     support_page.click_close_successful_modal()
    #     support_page.assert_closed_modal()