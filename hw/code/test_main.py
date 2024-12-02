import pytest, re
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from base_case import BaseCase
from ui.pages.main_page import MainPage
from ui.locators.main_page_locators import MainPageLocators

class TestMain(BaseCase):
    locators = MainPageLocators()

    # def test_main_page_for_unauth_user(self, driver):
    #     main_page = MainPage(driver)
    #     driver.get(main_page.url)
    #     assert "VK Реклама" in driver.title

    # def test_header_elements(self, driver):
    #     main_page = MainPage(driver)
    #     driver.get(main_page.url)
    #     assert main_page.is_vk_ads_logo_visible()
    #     assert main_page.is_nav_item_visible("Новости")
    #     assert main_page.is_nav_item_visible("Обучение")
    #     assert main_page.is_nav_item_visible("Кейсы")
    #     assert main_page.is_nav_item_visible("Форум идей")
    #     assert main_page.is_nav_item_visible("Монетизация")
    #     assert main_page.is_help_button_visible()
    #     assert main_page.is_nav_create_button_visible()

    # def test_help_button_redirect(self, driver):
    #     main_page = MainPage(driver)
    #     driver.get(main_page.url)
    #     main_page.click(self.locators.NAV_HELP_BUTTON)
    #     WebDriverWait(driver, 10).until(lambda d: "ads.vk.com/help" in d.current_url)
    #     assert "ads.vk.com/help" in driver.current_url

    # def test_slider_first_button(self, driver):
    #     main_page = MainPage(driver)
    #     driver.get(main_page.url)
    #     first_slide_button = WebDriverWait(driver, 40).until(ec.element_to_be_clickable(MainPageLocators.FIRST_SLIDE_BONUS_BUTTON))
    #     driver.execute_script("arguments[0].scrollIntoView();", first_slide_button)
    #     driver.execute_script("arguments[0].click();", first_slide_button)
    #     WebDriverWait(driver, 10).until(lambda d: "ads.vk.com/promo/firstbonus" in d.current_url)
    #     assert "ads.vk.com/promo/firstbonus" in driver.current_url

    # def test_slider_second_button(self, driver):
    #     main_page = MainPage(driver)
    #     driver.get(main_page.url)
        # second_slide_button = WebDriverWait(driver, 40).until(ec.element_to_be_clickable(MainPageLocators.SECOND_SLIDE_AD_BUTTON))
        # driver.execute_script("arguments[0].scrollIntoView();", second_slide_button)
        # driver.execute_script("arguments[0].click();", second_slide_button)
        # WebDriverWait(driver, 10).until(lambda d: "id.vk.com" in d.current_url # or "ads.vk.com/hq/overview" in d.current_url)
        # assert "id.vk.com" in driver.current_url # or "ads.vk.com/hq/overview" in driver.current_url

    # def test_slider_third_button(self, driver):
    #     main_page = MainPage(driver)
    #     driver.get(main_page.url)
    #     third_slide_button = WebDriverWait(driver, 40).until(ec.element_to_be_clickable(MainPageLocators.THIRD_SLIDE_MORE_BUTTON))
    #     driver.execute_script("arguments[0].scrollIntoView();", third_slide_button)
    #     driver.execute_script("arguments[0].click();", third_slide_button)
    #     WebDriverWait(driver, 10).until(lambda d: "adblogger.vk.com/for-advertisers" in d.current_url)
    #     assert "adblogger.vk.com/for-advertisers" in driver.current_url

    # def test_cases_button(self, driver):
    #     main_page = MainPage(driver)
    #     driver.get(main_page.url)
    #     main_page.click(MainPageLocators.CASES_VIEW_ALL_BUTTON, 10)
    #     WebDriverWait(driver, 10).until(lambda d: "ads.vk.com/cases" in d.current_url)
    #     assert "ads.vk.com/cases" in driver.current_url

    # def test_webinars_button(self, driver):
    #     main_page = MainPage(driver)
    #     driver.get(main_page.url)
    #     main_page.click(MainPageLocators.WEBINARS_MORE_BUTTON, 10) # это не кнопка, а большая область
    #     WebDriverWait(driver, 10).until(lambda d: "ads.vk.com/events" in d.current_url)
    #     assert "ads.vk.com/events" in driver.current_url

    # def test_cases_button(self, driver):
    #     main_page = MainPage(driver)
    #     driver.get(main_page.url)
    #     cases_button = driver.find_element(*MainPageLocators.CASES_VIEW_ALL_BUTTON)
    #     driver.execute_script("arguments[0].scrollIntoView();", cases_button)
    #     driver.execute_script("arguments[0].click();", cases_button)
    #     WebDriverWait(driver, 10).until(lambda d: "ads.vk.com/cases" in d.current_url)
    #     assert "ads.vk.com/cases" in driver.current_url

    # def test_case_navigation(self, driver):
    #     main_page = MainPage(driver)
    #     driver.get(main_page.url)
    #     case_title = driver.find_element(*MainPageLocators.ONE_CASE)
    #     driver.execute_script("arguments[0].scrollIntoView();", case_title)
    #     driver.execute_script("arguments[0].click();", case_title)
    #     WebDriverWait(driver, 10).until(lambda d: re.search(r"ads\.vk\.com/cases/.+", d.current_url))
    #     assert re.search(r"ads\.vk\.com/cases/.+", driver.current_url)

    # def test_webinars_button(self, driver):
    #     main_page = MainPage(driver)
    #     driver.get(main_page.url)
    #     webinars_button = driver.find_element(*MainPageLocators.WEBINARS_MORE_BUTTON)
    #     driver.execute_script("arguments[0].scrollIntoView();", webinars_button)
    #     driver.execute_script("arguments[0].click();", webinars_button)
    #     WebDriverWait(driver, 10).until(lambda d: "ads.vk.com/events" in d.current_url)
    #     assert "ads.vk.com/events" in driver.current_url

    # def test_news_button(self, driver):
    #     main_page = MainPage(driver)
    #     driver.get(main_page.url)
    #     news_button = driver.find_element(*MainPageLocators.NEWS_MORE_BUTTON)
    #     driver.execute_script("arguments[0].scrollIntoView();", news_button)
    #     driver.execute_script("arguments[0].click();", news_button)
    #     WebDriverWait(driver, 10).until(lambda d: "ads.vk.com/news" in d.current_url)
    #     assert "ads.vk.com/news" in driver.current_url

    # def test_footer_cabinet_button(self, driver):
    #     main_page = MainPage(driver)
    #     driver.get(main_page.url)
    #     footer_cabinet_button = driver.find_element(*MainPageLocators.FOOTER_CABINET_BUTTON)
    #     driver.execute_script("arguments[0].scrollIntoView();", footer_cabinet_button)
    #     driver.execute_script("arguments[0].click();", footer_cabinet_button)
    #     WebDriverWait(driver, 10).until(lambda d: "id.vk.com" in d.current_url)
    #     assert "id.vk.com" in driver.current_url

    # def test_footer_elements(self, driver):
    #     main_page = MainPage(driver)
    #     driver.get(main_page.url)
        
    #     assert main_page.is_footer_logo_visible()
    #     assert main_page.is_footer_cabinet_button_visible()
        
    #     assert main_page.is_footer_nav_item_visible("Новости")
    #     assert main_page.is_footer_nav_item_visible("Обучение для бизнеса")
    #     assert main_page.is_footer_nav_item_visible("Полезные материалы")
    #     assert main_page.is_footer_nav_item_visible("Кейсы")
    #     assert main_page.is_footer_nav_item_visible("Мероприятия")
    #     assert main_page.is_footer_nav_item_visible("Помощь")
    #     assert main_page.is_footer_nav_item_visible("Документы")
    #     assert main_page.is_footer_nav_item_visible("Монетизация")
        
    #     assert main_page.is_footer_social_visible("https://vk.com/vk_ads")
    #     assert main_page.is_footer_social_visible("https://ok.ru/group/64279825940712")
    #     assert main_page.is_footer_social_visible("https://dzen.ru/vk_ads")
    #     assert main_page.is_footer_social_visible("https://t.me/vk_ads")

    #     assert main_page.is_footer_language_selector_visible()
    #     assert main_page.is_footer_about_company_visible()
    #     assert main_page.is_footer_copyright_visible()
