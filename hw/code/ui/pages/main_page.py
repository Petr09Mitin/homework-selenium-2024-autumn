from ui.pages.base_page import BasePage
from ui.locators.main_page_locators import MainPageLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import re


class MainPage(BasePage):
    locators = MainPageLocators()
    url = 'https://ads.vk.com/'

    def click_vk_ads_logo(self):
        self.click(self.locators.VK_ADS_LOGO)

    def is_vk_ads_logo_visible(self):
        return self.is_element_visible(self.locators.NAV_VK_ADS_LOGO)

    def is_nav_item_visible(self, item_name):
        try:
            if item_name == "Обучение":
                return self.is_element_visible(self.locators.NAV_EDUCATION_DROPDOWN)
            self.find(self.locators.NAV_ITEM(item_name), 1)
            return True
        except TimeoutException:
            return False
        
    def is_help_button_visible(self):
        return self.is_element_visible(self.locators.NAV_HELP_BUTTON)
    
    # def is_nav_cabinet_button_visible(self)
    def is_nav_create_button_visible(self):
        return self.is_element_visible(self.locators.NAV_CREATE_BUTTON)
        
    def is_footer_logo_visible(self):
        return self.is_element_visible(self.locators.FOOTER_LOGO)
    
    def is_footer_cabinet_button_visible(self):
        return self.is_element_visible(self.locators.FOOTER_CABINET_BUTTON)
    
    def is_footer_nav_item_visible(self, text):
        try:
            items = self.find_multiple(self.locators.FOOTER_NAV_ITEMS, 1)
            return any(item.text == text for item in items)
        except TimeoutException:
            return False

    def is_footer_social_visible(self, network):
        try:
            socials = self.find_multiple(self.locators.FOOTER_SOCIAL_LINKS, 1)
            return any(network in social.get_attribute("href") for social in socials)
        except TimeoutException:
            return False

    def is_footer_language_selector_visible(self):
        return self.is_element_visible(self.locators.FOOTER_LANGUAGE_SELECTOR)
    
    def is_footer_about_company_visible(self):
        return self.is_element_visible(self.locators.FOOTER_ABOUT_COMPANY)
    
    def is_footer_copyright_visible(self):
        return self.is_element_visible(self.locators.FOOTER_COPYRIGHT)
    
    def assert_title_contains(self):
        expected_title = "VK Реклама"
        actual_title = self.driver.title
        assert expected_title in actual_title, f"Заголовок страницы должен содержать '{expected_title}', но он содержит: '{actual_title}'"

    def assert_header_elements_visible(self):
        assert self.is_vk_ads_logo_visible(), "Логотип VK Ads должен быть виден"
        assert self.is_nav_item_visible("Новости"), "Элемент навигации 'Новости' должен быть виден"
        assert self.is_nav_item_visible("Обучение"), "Элемент навигации 'Обучение' должен быть виден"
        assert self.is_nav_item_visible("Кейсы"), "Элемент навигации 'Кейсы' должен быть виден"
        assert self.is_nav_item_visible("Форум идей"), "Элемент навигации 'Форум идей' должен быть виден"
        assert self.is_nav_item_visible("Монетизация"), "Элемент навигации 'Монетизация' должен быть виден"
        assert self.is_help_button_visible(), "Кнопка 'Справка' должна быть видна"
        assert self.is_nav_create_button_visible(), "Кнопка 'Перейти в кабинет' должна быть видна"

    def assert_redirect_to_cases(self, timeout=10):
        pattern = r"ads\.vk\.com/cases/.+"
        WebDriverWait(self.driver, timeout).until(lambda d: re.search(pattern, d.current_url))
        assert re.search(pattern, self.driver.current_url), f"URL должен содержать '{pattern}', но получен '{self.driver.current_url}'"

    def assert_footer_elements_visible(self):
        assert self.is_footer_logo_visible(), "Логотип в футере должен быть виден"
        assert self.is_footer_cabinet_button_visible(), "Кнопка 'Перейти в кабинет' в футере должна быть видна"
        
        footer_nav_items = [
            "Новости",
            "Обучение для бизнеса",
            "Полезные материалы",
            "Кейсы",
            "Мероприятия",
            "Помощь",
            "Документы",
            "Монетизация"
        ]
        for item in footer_nav_items:
            assert self.is_footer_nav_item_visible(item), f"Элемент навигации '{item}' в футере должен быть виден"
        
        footer_social_links = [
            "https://vk.com/vk_ads",
            "https://ok.ru/group/64279825940712",
            "https://dzen.ru/vk_ads",
            "https://t.me/vk_ads"
        ]
        for link in footer_social_links:
            assert self.is_footer_social_visible(link), f"Ссылка на соц. сеть '{link}' в футере должна быть видна"

        assert self.is_footer_language_selector_visible(), "Селектор языка в футере должен быть виден"
        assert self.is_footer_about_company_visible(), "Информация о компании в футере должна быть видна"
        assert self.is_footer_copyright_visible(), "Копирайт в футере должен быть виден"