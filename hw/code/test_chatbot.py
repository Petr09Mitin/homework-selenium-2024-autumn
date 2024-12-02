import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from base_case import BaseCase
from ui.pages.main_page import MainPage
from ui.locators.main_page_locators import MainPageLocators
from ui.locators.cabinet_page_locators import CabinetPageLocators

class TestChatBot(BaseCase):

    def test_open_chatbot_from_help_menu(self, cabinet_page):
        cabinet_page.driver.get(cabinet_page.url)
        cabinet_page.open_chat_from_help_menu()
        # Ждем появления новой вкладки
        WebDriverWait(cabinet_page.driver, 10).until(lambda d: len(d.window_handles) > 1)
        # Переключаемся на новую вкладку
        new_window = cabinet_page.driver.window_handles[-1]
        cabinet_page.driver.switch_to.window(new_window)
        # Должна открыться страница авторизации на vk.com
        assert "vk.com" in cabinet_page.driver.current_url
        cabinet_page.driver.switch_to.window(cabinet_page.driver.window_handles[0])
