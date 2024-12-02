from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import BasePageLocators

class MainPageLocators(BasePageLocators):
    VK_ADS_LOGO = (By.XPATH, "//*[contains(@class, 'HeaderLeft_home__')]")

    VK_BUSINESS_LOGO = (
        By.XPATH,
        "//*[contains(@class, 'Footer_controls__')]/a[contains(@href, 'https://vk.company/ru/company/business/')]"
    )

    NAV_CABINET_BUTTON = (
        By.XPATH,
        "//*[contains(@class, 'NavigationVKAds_right__')]/a[contains(@class, 'ButtonCabinet_primary__')]"
    )

    FOOTER_CABINET_BUTTON = (
        By.XPATH,
        "//*[contains(@class, 'Footer_leftContent__')]/a[contains(@class, 'ButtonCabinet_primary__')]"
    )

    NAV_VK_ADS_LOGO = (By.XPATH, "//div[contains(@class, 'content_logo__GA44t')]")
    NAV_EDUCATION_DROPDOWN = (By.XPATH, "//span[contains(@class, 'item_item__0CD1p') and contains(text(), 'Обучение')]")
    NAV_HELP_BUTTON = (By.XPATH, "//div[contains(@class, 'navigation_help__pOSFK')]//a[contains(@class, 'item_link__sbjAO') and contains(text(), 'Справка')]")
    NAV_CREATE_BUTTON = (By.XPATH, "//a[contains(@class, 'ButtonCabinet_primary__')]")
    
    @staticmethod
    def NAV_ITEM(item_name):
        return By.XPATH, f"//div[contains(@class, 'navigation_item__zSI_a')]//a[contains(@class, 'item_link__sbjAO') and contains(text(), '{item_name}')]"
    
    FIRST_SLIDE_BONUS_BUTTON = (By.XPATH, "//span[contains(@class, 'vkuiButton__in') and contains(., 'Получить бонус')]")
    SECOND_SLIDE_AD_BUTTON = (By.XPATH, "//span[contains(@class, 'vkuiButton__in') and contains(., 'Запустить рекламу')]")
    THIRD_SLIDE_MORE_BUTTON = (By.XPATH, "//span[contains(@class, 'vkuiButton__in') and contains(., 'Подробнее')]")
    CASES_VIEW_ALL_BUTTON = (By.XPATH, "//a[contains(@class, 'styles_all__wnH9i')]")
    ONE_CASE = (By.XPATH, "//div[contains(@class, 'Case_title__JAisY')]")
    WEBINARS_MORE_BUTTON = (By.XPATH, "//a[contains(@class, 'GetStarted_wrapper__cTNLj') and @href='/events']") # это не кнопка, а большая область
    NEWS_MORE_BUTTON = (By.XPATH, "//button[contains(@class, 'News_button__bnojH') and contains(., 'Подробнее')]")

    FOOTER_LOGO = (By.CLASS_NAME, "Footer_logo__pwCXU")
    FOOTER_CABINET_BUTTON = (By.CSS_SELECTOR, "a.ButtonCabinet_primary__LCfol")
    FOOTER_NAV_ITEMS = (By.CSS_SELECTOR, "ul.Footer_items__gaWoZ li a")
    FOOTER_SOCIAL_LINKS = (By.CSS_SELECTOR, ".Footer_leftControls__25wO6 a")
    FOOTER_LANGUAGE_SELECTOR = (By.CLASS_NAME, "SelectLanguage_wrapper__id9eU")
    FOOTER_ABOUT_COMPANY = (By.CLASS_NAME, "Footer_about__i8sA6")
    FOOTER_COPYRIGHT = (By.CLASS_NAME, "Footer_copyrightWrap__jF5CC")
