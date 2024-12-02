from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ес

from ui.pages.base_page import BasePage
from ui.locators.cabinet_page_locators import CabinetPageLocators

class CabinetPage(BasePage):
    locators = CabinetPageLocators()
    url = 'https://ads.vk.com/hq/overview'

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
