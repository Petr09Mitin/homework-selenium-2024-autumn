import pytest, re
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from base_case import BaseCase
from ui.pages.main_page import MainPage
from ui.locators.main_page_locators import MainPageLocators

class TestMain(BaseCase):
    locators = MainPageLocators()
    url_help = "ads.vk.com/help"
    url_first_bonus = "ads.vk.com/promo/firstbonus"
    url_vkid = "id.vk.com"
    url_adblogger = "adblogger.vk.com/for-advertisers"
    url_cases = "ads.vk.com/cases"
    url_webinars = "ads.vk.com/events"
    url_news = "ads.vk.com/news"

    def test_main_page_for_unauth_user(self, main_page):
        main_page.assert_title_contains()

    def test_header_elements(self, main_page):
        main_page.assert_header_elements_visible()

    def test_help_button_redirect(self, main_page):
        main_page.click(self.locators.NAV_HELP_BUTTON)
        main_page.assert_redirect(self.url_help)
    
    def test_slider_first_button(self, main_page):
        first_slide_button = WebDriverWait(main_page, 40).until(ec.element_to_be_clickable(MainPageLocators.FIRST_SLIDE_BONUS_BUTTON))
        main_page.execute_script("arguments[0].scrollIntoView();", first_slide_button)
        main_page.execute_script("arguments[0].click();", first_slide_button)
        main_page.assert_redirect(self.url_first_bonus)

    def test_slider_second_button(self, main_page):
        second_slide_button = WebDriverWait(main_page, 40).until(ec.element_to_be_clickable(MainPageLocators.SECOND_SLIDE_AD_BUTTON))
        main_page.execute_script("arguments[0].scrollIntoView();", second_slide_button)
        main_page.execute_script("arguments[0].click();", second_slide_button)
        main_page.assert_redirect(self.url_vkid)

    def test_slider_third_button(self, main_page):
        third_slide_button = WebDriverWait(main_page, 40).until(ec.element_to_be_clickable(MainPageLocators.THIRD_SLIDE_MORE_BUTTON))
        main_page.execute_script("arguments[0].scrollIntoView();", third_slide_button)
        main_page.execute_script("arguments[0].click();", third_slide_button)
        main_page.assert_redirect(self.url_adblogger)

    def test_cases_button(self, main_page):
        main_page.click(MainPageLocators.CASES_VIEW_ALL_BUTTON, 10)
        main_page.assert_redirect(self.url_cases)

    def test_webinars_button(self, main_page):
        main_page.click(MainPageLocators.WEBINARS_MORE_BUTTON, 10) # это не кнопка, а большая область
        main_page.assert_redirect(self.url_webinars)

    def test_case_navigation(self, main_page):
        case_title = main_page.find_element(*MainPageLocators.ONE_CASE)
        main_page.execute_script("arguments[0].scrollIntoView();", case_title)
        main_page.execute_script("arguments[0].click();", case_title)
        main_page.assert_redirect_to_cases()
        # WebDriverWait(driver, 10).until(lambda d: re.search(r"ads\.vk\.com/cases/.+", d.current_url))
        # assert re.search(r"ads\.vk\.com/cases/.+", driver.current_url)

    def test_news_button(self, main_page):
        news_button = main_page.find_element(*MainPageLocators.NEWS_MORE_BUTTON)
        main_page.execute_script("arguments[0].scrollIntoView();", news_button)
        main_page.execute_script("arguments[0].click();", news_button)
        main_page.assert_redirect(self.url_news)

    def test_footer_cabinet_button(self, main_page):
        footer_cabinet_button = main_page.find_element(*MainPageLocators.FOOTER_CABINET_BUTTON)
        main_page.execute_script("arguments[0].scrollIntoView();", footer_cabinet_button)
        main_page.execute_script("arguments[0].click();", footer_cabinet_button)
        main_page.assert_redirect(self.url_vkid)

    def test_footer_elements(self, main_page):
        main_page.assert_footer_elements_visible()
