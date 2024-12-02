from selenium.webdriver.common.by import By


class SettingsNotificationsLocators:
    TAB_ITEM = (By.XPATH, '//*[@data-testid="tabs-item-settings.notifications"]')
    
    EMAILS_NOTIFICATIONS = (By.XPATH, '//*[contains(@class, "Emails_item__x1pUR")]')
    TG_NOTIFICATIONS = (By.XPATH, '//*[contains(@class, "Telegram_item__aNJ4k")]')
    
    WARNING_BLOCK = (By.XPATH, '//*[contains(@class, "Warning_warning__xKzW3")]')
