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

    @staticmethod
    def NAV_ITEM(item_name):
        return By.XPATH, f"//*[contains(@class, 'NavigationVKAdsItem_') and text()='{item_name}']"
