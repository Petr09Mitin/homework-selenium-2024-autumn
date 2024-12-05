import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from ui.pages.base_page import BasePage, DEFAULT_TIMEOUT
from ui.locators.auth_page_locators import AuthPageLocators
from ui.pages.base_page import WAIT_TIMEOUT

class AuthPage(BasePage):
    locators = AuthPageLocators()

    def login(self, login, password):
        self.click(self.locators.NAV_CABINET_BUTTON)
        WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(
            EC.element_to_be_clickable(self.locators.MAIL_RU_AUTH_BUTTON)
        )
        
        self.click(self.locators.MAIL_RU_AUTH_BUTTON)
        WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(
            EC.visibility_of_element_located(self.locators.MAIL_RU_LOGIN)
        )

        login_input = self.find(self.locators.MAIL_RU_LOGIN)
        login_input.clear()
        login_input.send_keys(login)
        WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(
            EC.element_to_be_clickable(self.locators.MAIL_RU_NEXT_BUTTON)
        )

        self.click(self.locators.MAIL_RU_NEXT_BUTTON)

        if self.is_element_clickable(self.locators.MAIL_RUN_OTHER_WAY_BUTTON, timeout=DEFAULT_TIMEOUT):
            self.click(self.locators.MAIL_RUN_OTHER_WAY_BUTTON)
        else:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.locators.MAIL_RU_AUTH_PROBLEMS_BUTTON)
            )
            self.click(self.locators.MAIL_RU_AUTH_PROBLEMS_BUTTON)

            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.locators.MAIL_RU_ENTER_PASSWORD_BUTTON)
            )
            self.click(self.locators.MAIL_RU_ENTER_PASSWORD_BUTTON)

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.locators.MAIL_RU_PASSWORD)
        )

        password_input = self.find(self.locators.MAIL_RU_PASSWORD)
        password_input.clear()
        password_input.send_keys(password)
        WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(
            EC.element_to_be_clickable(self.locators.MAIL_RU_SUBMIT_BUTTON)
        )

        self.click(self.locators.MAIL_RU_SUBMIT_BUTTON)

    def wait_for_redirect_to_cabinet(self):
        try:
            return WebDriverWait(self.driver, 20).until(lambda d: "ads.vk.com/hq/overview" in d.current_url)
        except TimeoutException:
            return False
