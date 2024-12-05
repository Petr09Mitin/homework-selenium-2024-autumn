from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ес

from ui.pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ui.pages.base_page import BasePage, DEFAULT_TIMEOUT
from ui.locators.cabinet_page_locators import CabinetPageLocators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException

class CabinetPage(BasePage):
    locators = CabinetPageLocators()
    url = 'https://ads.vk.com/hq/overview'
    courses_url = 'https://expert.vk.com/courses'
    adblogger_url = 'https://adblogger.vk.com'
    
    def open_learning_modal(self, timeout=DEFAULT_TIMEOUT):
        self.hover(locator=self.locators.HELP_MENU_ITEM, timeout=timeout)
        self.click(locator=self.locators.HELP_MENU_ITEM, timeout=timeout)
        self.click(locator=self.locators.ONBOARDING_BUTTON, timeout=timeout)
    
    def choose_site_target(self, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.locators.SITES_TARGET, timeout=timeout)

    def open_learning_and_choose_site(self, timeout=DEFAULT_TIMEOUT):
        self.open_learning_modal(timeout=timeout)
        self.choose_site_target(timeout=timeout)
    
    def learn_through_video(self, timeout=DEFAULT_TIMEOUT):
        self.open_learning_and_choose_site(timeout=timeout)
        self.click(locator=self.locators.VIDEO_OPTION, timeout=timeout)
    
    def assert_video_opened(self, timeout=DEFAULT_TIMEOUT):
        assert self.became_visible(locator=self.locators.VIDEO, timeout=timeout)
    
    def close_video(self, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.locators.DISMISS_BUTTON, timeout=timeout)
    
    def learn_through_course(self, timeout=DEFAULT_TIMEOUT):
        self.open_learning_and_choose_site(timeout=timeout)
        self.click(locator=self.locators.COURSE_OPTION, timeout=timeout)
        self.go_to_new_tab()
    
    def assert_course_page_opened(self, timeout=DEFAULT_TIMEOUT):
        assert self.subpage_is_opened(url=self.courses_url, timeout=timeout)
    
    def close_course_page(self, timeout=DEFAULT_TIMEOUT):
        self.driver.close()
    
    def open_adblogger(self, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.locators.OPEN_ADBLOGGER, timeout=timeout)
        self.go_to_new_tab()
        
    def assert_adblogger_opened(self, timeout=DEFAULT_TIMEOUT):
        assert self.subpage_is_opened(url=self.adblogger_url, timeout=timeout)
        
    def close_adblogger_page(self, timeout=DEFAULT_TIMEOUT):
        self.driver.close()
        
    def dismiss_adblogger(self, timeout=DEFAULT_TIMEOUT):
        self.click(locator=self.locators.DISMISS_ADBLOGGER, timeout=timeout)
        
    def assert_adblogger_invisible(self, timeout=DEFAULT_TIMEOUT):
        assert self.became_invisible(locator=self.locators.OPEN_ADBLOGGER, timeout=timeout)
        
    # Нажатие на кнопку "Задать вопрос" в меню "Помощь и обучение"
    def open_chat_from_help_menu(self):
        help_menu = self.find(self.locators.HELP_MENU_ITEM)
        actions = ActionChains(self.driver)
        actions.move_to_element(help_menu).perform() # имитация наведения мыши на элемент
        chat_button = WebDriverWait(self.driver, 10).until(ес.presence_of_element_located(CabinetPageLocators.CHATBOT_OPEN_BUTTON))
        actions.move_to_element(chat_button).perform()
        actions.click().perform()

    def is_chatbot_window_visible(self):
        return self.is_element_visible(self.locators.CHATBOT_WINDOW)
    
    def wait_for_redirect_to_vk(self):
        try:
            return WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(lambda d: "vk.com" in d.current_url)
        except TimeoutException:
            return False
        
    def assert_redirect_to_vk(self):
        assert self.wait_for_redirect_to_vk(), "Ожидался редирект на vk.com, но он не произошел"
