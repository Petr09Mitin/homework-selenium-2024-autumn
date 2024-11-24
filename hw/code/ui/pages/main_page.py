from ui.pages.base_page import BasePage
from ui.locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    locators = MainPageLocators()
    url = 'https://ads.vk.com/'

    def click_vk_ads_logo(self):
        self.click(self.locators.VK_ADS_LOGO)
