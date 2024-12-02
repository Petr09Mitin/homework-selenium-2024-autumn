from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import BasePageLocators

class CabinetPageLocators(BasePageLocators):
    HELP_MENU_ITEM = (By.XPATH, '//*[@data-testid="help-menu-item"]')
    ONBOARDING_BUTTON = (By.XPATH, '//*[@data-testid="onboarding-button"]')
    SITES_TARGET = (By.XPATH, '//div[@role="button"]//span[text()="Сайт"]')
    VIDEO_OPTION = (By.XPATH, '//span[text()="Смотреть видеоурок от экспертов VK"]')
    COURSE_OPTION = (By.XPATH, '//span[text()="Смотреть курс на обучающей платформе"]')
    VIDEO = (By.XPATH, '//iframe[contains(@class, "VideoOnboardingModal_frame")]')
    DISMISS_BUTTON = (By.XPATH, '//div[@role="button" and @aria-label="Закрыть"]')
    OPEN_ADBLOGGER = (By.XPATH, '//span[text()="Открыть VK AdBlogger"]')
    DISMISS_ADBLOGGER = (By.XPATH, '//button[@aria-label="Close button"]')

    CHATBOT_OPEN_BUTTON = (By.XPATH, '//span[text()="Задать вопрос"]')
    CHATBOT_WINDOW = (By.XPATH, "//div[contains(@class, 'SAKWindow__container')]")
    CHATBOT_VK_MESSENGER_LOGO = (By.XPATH, "//*[contains(@class, 'vkuiIcon--messages_28')]")
