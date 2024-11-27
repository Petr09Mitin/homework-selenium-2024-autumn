from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import BasePageLocators


class CampaignPageLocators(BasePageLocators):
    LEARNING_MODAL_DISMISS_BUTTON = (By.XPATH, '//div[@role="button" and @aria-label="Закрыть"]')
    CREATE_CAMPAIGN_BUTTON = (By.XPATH, "//*[@data-testid='create-button']")
    CAMPAIGN_NAME_INPUT = (By.XPATH, '//div[starts-with(@class, "EditableTitle")]')
    SITE_OPTION = (By.XPATH, '//div[@data-id="site_conversions"]')
    CATALOGUE_OPTION = (By.XPATH, '//div[@data-id="ecomm"]')
    ADVERTISED_SITE_FIELD = (By.XPATH, '//input[@placeholder="Введите ссылку на сайт"]')
    BUDGET = (By.XPATH, '//*[@data-testid="targeting-not-set"]')
    START_DATE = (By.XPATH, '//*[@data-testid="start-date"]')
    END_DATE = (By.XPATH, '//*[@data-testid="end-date"]')
    CONTINUE = (By.XPATH, '//span[contains(text(), "Продолжить")]')
    REGION = (By.XPATH, '//span[contains(text(), "Россия")]')
    AD_LOGO_UPLOAD = (By.XPATH, '//*[@data-testid="set-global-image"]')
    AD_HEADER = (By.XPATH, '//*[@data-testid="заголовок, макс. 40 символов"]')
    AD_SHORT_DESCRIPTION = (By.XPATH, '//*[@data-testid="описание, макс. 90 символов"]')
    AD_MEDIATEKA = (By.XPATH, '//span[contains(text(), "Медиатека")]')
    MEDIATEKA_FILE = (By.XPATH, '//div[starts-with(@class, "ImageItem")]')
    CLOSE_BUTTON = (By.XPATH, '//button[@aria-label="Close"]')
    ADD_BUTTON = (By.XPATH, '//span[contains(text(), "Добавить")]')
    AD_LOAD_MEDIAFILES = (By.XPATH, '//div[contains(@class, "Loading_loading")]')
    FILE_INPUT = (By.XPATH, '//input[@type="file"]')
    ADD_MEDIA_FILE_INPUT = (By.XPATH, '//label[starts-with(@class, "LocalFileSelector_file")]//input[@type="file"]')
    LOADED_MEDIA_PREVIEW = (By.XPATH, '//*[contains(@class, "MediaContainer_image") or contains(@class, "VideoContainer_video")]')
    AD_LOGO_PREVIEW = (By.XPATH, '//img[@alt="media preview" and contains(@class, "AdMediaPreview_img")]')
    ADD_MEDIA_AI = (By.XPATH, '//span[contains(text(), "Созданное нейросетью")]')
    MEDIA_PLACEHOLDER = (By.XPATH, '//*[contains(@class, "MediaPlaceholder")]')
    ADD_MEDIA_AI_ELEMENT = (By.XPATH, '//div[contains(@class, "ImageItem_imageItem")]')
    ADD_MEDIA_AI_BUTTON = (By.XPATH, '//span[contains(text(), "Добавить (")]')
    PUBLISH_BUTTON = (By.XPATH, '//span[contains(text(), "Опубликовать")]')
    
    ACTIONS_ICON = (By.XPATH, '//*[@data-testid="actions"]')
    DELETE_BUTTON = (By.XPATH, '//*[contains(text(), "Удалить")]')
    CAMPAIGNS_MENU_TAB = (By.XPATH, '//*[@id="dashboardV2.plans"]')
    
    def get_campaign_name_locator(name):
        return (By.XPATH, f'//div[starts-with(@class, "nameCellContent_content")]//button[contains(text(), "{name}")]')
    