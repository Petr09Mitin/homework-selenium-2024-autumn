import time
import allure
from selenium.common import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from os import path

from ui.locators.base_page_locators import BasePageLocators

DEFAULT_TIMEOUT = 30
WAIT_TIMEOUT = 30
WAIT_TIMEOUT_10 = 10

class PageNotOpenedException(Exception):
    pass

class BasePage(object):
    locators = BasePageLocators()
    url = 'https://ads.vk.com/'

    def _get_static_filepath(self, filename):
        return path.abspath(
            path.join(path.curdir, 'hw', 'static', filename)
        )

    def is_opened(self, timeout=100):
        started = time.time()
        while time.time() - started < timeout:
            current_url = self.driver.current_url.rstrip('/')
            expected_url = self.url.rstrip('/')
            if current_url == expected_url:
                return True
        raise PageNotOpenedException(f'{self.url} did not open in {timeout} sec, current url {self.driver.current_url}')
    
    def subpage_is_opened(self, url=None, timeout=DEFAULT_TIMEOUT):
        if not url:
            url = self.url
        started = time.time()
        while time.time() - started < timeout:
            if url in self.driver.current_url:
                return True
        raise PageNotOpenedException(f'{url} did not open in {timeout} sec, current url {self.driver.current_url}')

    def close_cookie_banner(self):
        try:
            self.click(self.locators.COOKIE_BUTTON)
        except TimeoutException:
            pass

    def __init__(self, driver):
        self.driver = driver
        self.is_opened()
        self.close_cookie_banner()

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=None) -> WebElement:
        return self.wait(timeout).until(ec.presence_of_element_located(locator))

    def find_multiple(self, locator, timeout=None):
        return self.wait(timeout).until(ec.visibility_of_all_elements_located(locator))

    @allure.step('Click')
    def click(self, locator, timeout=None) -> WebElement:
        elem = self.wait(timeout).until(ec.element_to_be_clickable(locator))
        elem.click()
        return elem

    def scroll_and_click(self, locator, timeout=None) -> WebElement:
        elem = self.wait(timeout).until(ec.presence_of_element_located(locator))
        ActionChains(self.driver).move_to_element(elem).click(elem).perform()
        return elem

    def go_to_new_tab(self):
        handles = self.driver.window_handles
        assert len(handles) > 1
        self.driver.switch_to.window(handles[1])

    def hover(self, locator, timeout=None):
        elem = self.wait(timeout).until(ec.presence_of_element_located(locator))
        ActionChains(self.driver).move_to_element(elem).perform()

    def became_invisible(self, locator, timeout=None):
        try:
            self.wait(timeout).until(ec.invisibility_of_element(locator))
            return True
        except TimeoutException:
            return False

    def became_visible(self, locator, timeout=None):
        try:
            self.wait(timeout).until(ec.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
    
    def is_element_visible(self, locator, timeout=5):
        try:
            self.find(locator, timeout)
            return True
        except TimeoutException:
            return False
    
    def send_keys_to_input(self, locator, keys, timeout):
        inp = self.find(locator=locator, timeout=timeout)
        inp.clear()
        inp.send_keys(keys)
