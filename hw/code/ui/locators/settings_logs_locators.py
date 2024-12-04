from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import BasePageLocators


class SettingsLogsLocators(BasePageLocators):
    TAB_ITEM = (By.ID, 'tab-settings.logs')
    
    FILTER_BUTTON = (By.XPATH, '//*[@data-testid="filter-button"]')
    CALENDAR_BUTTON = (By.XPATH, '//*[@class="ActionsBlock_filterAndSearch__9pVMm"]//button[span//div[@class="RangeDatePickerManager_rangeText__VQM6k"]]')
    SEARCH_INPUT = (By.XPATH, '//*[@data-testid="search"]')
    NOT_FOUND = (By.XPATH, '//span[contains(text(), "Ничего не нашлось")]')
    EMPTY_LOGS_HISTORY = (By.XPATH, '//span[contains(text(), "Здесь будет храниться история изменений в кабинете")]')
    RANGE_DATE_CANCEL_BUTTON = (By.XPATH, '//div[@class="RangeDatePicker_buttons__Z+Ue8"]/button[@class="vkuiButton--size-l vkuiButton--mode-secondary"]')
    RANGE_DATE_ACCEPT_BUTTON = (By.XPATH, '//div[@class="RangeDatePicker_buttons__Z+Ue8"]/button[@class="vkuiButton--size-l vkuiButton--mode-primary"]')

    def filter_section_button(text: str):
        return (By.XPATH, f'//button[span//span[contains(text(), "{text}")]]')

    CALENDAR_MODAL = (By.XPATH, '//div[contains(@class, "RangeDatePicker_tooltipContainer__9ztm6")]')

    OBJECT_TYPE_BUTTON = filter_section_button('Тип объекта')
    WHAT_CHANGED_BUTTON = filter_section_button('Что изменилось')
    CHANGE_AUTHOR_BUTTON = filter_section_button('Автор изменения')

    CHECKBOX = (By.XPATH, '//input[@type="checkbox"]')

    COMPANY_CHECKBOX = (By.XPATH, '//span[text()="Кампания"]/../../../input')
    COMPANY_CHECKBOX_BUTTON = (By.XPATH, '//span[text()="Кампания"]/../../..')

    TODAY_BUTTON = (By.XPATH, '//button[span/text()="Сегодня"]')

    START_DATE_INPUT = (By.NAME, 'startDate')
    END_DATE_INPUT = (By.NAME, 'endDate')

    def modal_button(text: str):
        return (By.XPATH, f'//button[span//text()="{text}"]')

    SELECT_ALL_BUTTON = modal_button('Выбрать все')
    RESET_BUTTON = modal_button('Сбросить')
    RESET_ALL_BUTTON = modal_button('Сбросить все')

    SAVE_BUTTON = modal_button('Применить')
    CANCEL_BUTTON = modal_button('Отмена')
    CALENDAR_CANCEL_BUTTON = modal_button('Отменить')
    FILTERED_GROUPS = (By.XPATH, '//div[@class="SelectedFilter_list__VY8L4"]')
    RESET_FILTERED_GROUP = (By.XPATH, '//button[contains(@class, "SelectedFilter_control__MIe9W")]')
