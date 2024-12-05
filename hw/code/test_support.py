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