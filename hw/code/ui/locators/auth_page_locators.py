from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import BasePageLocators


class AuthPageLocators(BasePageLocators):
    NAV_CABINET_BUTTON = (By.XPATH, "//a[contains(@class, 'ButtonCabinet_primary__')]")
    MAIL_RU_AUTH_BUTTON = (By.XPATH, "//button[@data-test-id='oAuthService_mail_ru']")
    MAIL_RU_LOGIN = (By.NAME, 'username')
    MAIL_RUN_OTHER_WAY_BUTTON = (By.XPATH, "//*[@data-test-id='auth-screen-vkid-change-restore-type-btn']")
    MAIL_RU_PASSWORD = (By.NAME, "password")
    MAIL_RU_NEXT_BUTTON = (By.XPATH, "//*[@data-test-id='next-button']")
    MAIL_RU_SUBMIT_BUTTON = (By.XPATH, "//*[@data-test-id='submit-button']")

    MAIL_RU_AUTH_PROBLEMS_BUTTON = (By.XPATH, "//a[contains(@data-test-id, 'auth-problems')]")
    MAIL_RU_ENTER_PASSWORD_BUTTON = (By.XPATH, "//a[contains(text(), 'Использовать пароль')]")

