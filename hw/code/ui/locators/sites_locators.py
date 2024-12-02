from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import BasePageLocators


class SitePageLocators(BasePageLocators):
    MENU_ITEM = (By.XPATH, '//a[@data-entityid="pixels"]')
    
    NOONE_PIXELS = (By.XPATH, '//h2[contains(text(), "Нет привязанных пикселей трекинга")]')
    ADD_PIXEL_BUTTON = (By.XPATH, '//div[@class="vkuiPlaceholder__action"]//button')
    MODAL_ADD_PIXEL = (By.XPATH, '//div[@class="ModalRoot_componentWrapper__uzHTL"]')
    CLOSE_MODAL_ADD_PIXEL = (By.XPATH, '//div[contains(@class, "vkuiModalDismissButton ")]')
    INPUT_SITE_DOMAIN = (By.XPATH, '//input[@placeholder="Домен сайта"]')
    ADD_SITE_BUTTON = (By.XPATH, '//div[contains(@class, "DomainCheckStep_actionsWrapper__QAgRn")]//button')
    INCORRECT_SITE_DOMAIN = (By.XPATH, '//span[contains(text(), "Введите корректный адрес сайта (вида: example.ru)")]')
    ADD_NEW_PIXEL_BUTTON = (By.XPATH, '//div[contains(@class, "FlowSelectStep_cell__LXV8m") and div//span[contains(text(), "Создать новый пиксель")]]')
    CREATED_PIXEL_MODAL = (By.XPATH, '//h2[contains(text(), "Создан ID пикселя")]')
    CLOSE_CREATED_PIXEL_MODAL = (By.XPATH, '//div[@aria-label="Закрыть"]')
    
    PIXEL_ITEM_RAW = (By.XPATH, '//div[@class="BaseTable__row PixelsList__row"]')
    PIXEL_ITEM_MORE_SYMBOL = (By.XPATH, '//button[@aria-label="More"]')
    REMOVE_PIXEL_BUTTON = (By.XPATH, '//label[@data-testid="dropdown-item" and div//span[contains(text(), "Удалить пиксель")]]')
    REMOVE_PIXEL_MODAL = (By.XPATH, '//div[@class="vkuiModalCardBase__container"]')
    ACCEPT_REMOVE_PIXEL_BUTTON = (By.XPATH, '//button[span//span[contains(text(), "Удалить")]]')
    
    PIXEL_SETTINGS_BUTTON = (By.XPATH, '//a[@data-route="pixels.events"]')
    
    SITE_AUDIENCE_TAB = (By.XPATH, '//div[@id="tab_pixels.portrait"]')
    SITE_DIAGNOSTIC_TAB = (By.XPATH, '//div[@id="tab_pixels.review"]')
    SITE_CODE_TAB = (By.XPATH, '//div[@id="tab_pixels.code"]')
    SITE_EVENTS_TAB = (By.XPATH, '//div[@id="tab_pixels.events"]')
    
    NO_EVENTS = (By.XPATH, '//h2[text()="Нет добавленных событий"]')
    ADD_EVENT_BUTTON = (By.XPATH, '//div[@class="vkuiPlaceholder__action"]/button')
    NAME_EVENT_INPUT = (By.XPATH, '//input[@placeholder="Введите название"]')
    PURCHASE_CATEGORY_OPTION = (By.XPATH, '//option[@value="purchase"]')
    PAGE_VISITED_OPTION = (By.XPATH, '//option[@value="uss"]')
    URL_EVENT_INPUT = (By.XPATH, '//input[@placeholder="Введите значение"]')
    ACCEPT_ADD_EVENT_BUTTON = (By.XPATH, '//button[@data-testid="submit"]')
    INSTRUCTION_VISUAL_CONSTRUCTOR_BUTTON = (By.XPATH, '//a[@href="/help/articles/visual_event"]')
    
    def category_by_name(name):
        return (By.XPATH, f'//div[contains(@class, "EventList_doubleCellWrapper__jFr8X")]//span[text()="{name}"]')
    
    GATHERING_DATA_LAYER_INPUT = (By.XPATH, '//label[@class="SwitchWithText_wrap__WuV8t" and div//div[text()="Сбор событий из слоя данных (data-layer)"]]/label')
    GATHERING_DATA_DESCRIBING = (By.XPATH, '//span[text()="Убедитесь что на вашем сайте размещён код с правильным названием слоя данных"]')
    SYNCRONIZATION_INPUT = (By.XPATH, '//label[@class="SwitchWithText_wrap__WuV8t" and div//div[text()="Синхронизация пользователей"]]/label')
    SYNCRONIZATION_DESCRIBING = (By.XPATH, '//div[text()="Настройте подмену шаблонного USER_ID на реальные данные при установке кода на сайт"]')
    INSTRUCTION_BUTTON = (By.XPATH, '//button[span/span[text()="Инструкция по установке"]]')
    INSTRUCTION_MODAL = (By.XPATH, '//div[@class="ModalRoot_componentWrapper__uzHTL"]')
    CLOSE_INSTRUCTION_MODAL = (By.XPATH, '//div[contains(@class, "vkuiModalDismissButton")]')
    
    NOT_ENOUGH_AUDIENCE = (By.XPATH, '//h2[text()="Недостаточно посетителей сайта"]')
    
    NO_DIAGNOSTIC_EARLIER = (By.XPATH, '//h2[text()="Диагностика ещё не проводилась"]')
    CHECK_SITE = (By.XPATH, '//div[@class="vkuiPlaceholder__action"]/button')
    