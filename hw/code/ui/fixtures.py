import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from ui.pages.auth_page import AuthPage
from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage
from ui.pages.registration_page import RegistrationPage
from ui.pages.welcome_page import WelcomePage
from ui.pages.cabinet_page import CabinetPage
from ui.pages.campaigns_page import CampaignsPage
from ui.pages.audience_page import AudiencePage
from ui.pages.mobile_apps_page import MobileAppsPage
from ui.pages.settings_page import SettingsPage
from ui.pages.support_page import SupportPage
from ui.pages.sites_page import SitesPage
import os
from dotenv import load_dotenv

@pytest.fixture()
def driver(config):
    browser = config['browser']
    url = config['url']
    selenoid = config['selenoid']
    vnc = config['vnc']
    options = Options()
    if selenoid:
        capabilities = {
            'browserName': 'chrome',
            'version': '118.0',
        }
        if vnc:
            capabilities['enableVNC'] = True
        driver = webdriver.Remote(
            'http://127.0.0.1:4444/wd/hub',
            options=options,
        )
    elif browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise RuntimeError(f'Unsupported browser: "{browser}"')
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)


@pytest.fixture
def main_page(driver):
    return MainPage(driver=driver)


@pytest.fixture(scope='session')
def credentials_without_cabinet():
    load_dotenv()
    return os.getenv('LOGIN_WITHOUT_CABINET'), os.getenv('PASSWORD_WITHOUT_CABINET')


@pytest.fixture(scope='session')
def credentials_with_cabinet():
    load_dotenv(dotenv_path='.env')
    return os.getenv('LOGIN'), os.getenv('PASSWORD')


@pytest.fixture
def auth_page(driver):
    return AuthPage(driver=driver)


@pytest.fixture
def cabinet_page(driver, credentials_with_cabinet, auth_page):
    driver.get(BasePage.url)
    auth_page.login(*credentials_with_cabinet)
    return CabinetPage(driver=driver)

@pytest.fixture
def campaigns_page(driver, cabinet_page):
    driver.get(CampaignsPage.url)
    return CampaignsPage(driver=driver)

@pytest.fixture
def audience_page(driver, cabinet_page):
    driver.get(AudiencePage.url)
    return AudiencePage(driver=driver)

@pytest.fixture
def mobile_apps_page(driver, cabinet_page):
    driver.get(MobileAppsPage.url)
    return MobileAppsPage(driver=driver)

@pytest.fixture
def support_page(driver, cabinet_page):
    driver.get(SupportPage.url)
    return SupportPage(driver=driver)

@pytest.fixture
def settings_page(driver, cabinet_page):
    driver.get(SettingsPage.url)
    return SettingsPage(driver=driver)

@pytest.fixture
def sites_page(driver, cabinet_page):
    driver.get(SitesPage.url)
    return SitesPage(driver=driver)


@pytest.fixture
def authorized_user(driver, auth_page, credentials_with_cabinet): 
    driver.get(BasePage.url)
    auth_page.login(*credentials_with_cabinet)
    return auth_page


@pytest.fixture
def registration_page(driver, authorized_user):
    driver.get(RegistrationPage.url)
    return RegistrationPage(driver=driver)

@pytest.fixture
def authorization_page(driver, auth_page, credentials_with_cabinet): 
    driver.get(BasePage.url)
    auth_page.login(*credentials_with_cabinet)
    return AuthPage(driver=driver)


@pytest.fixture
def welcome_page(driver, credentials_with_cabinet, auth_page):
    driver.get(BasePage.url)
    auth_page.login(*credentials_with_cabinet)
    return WelcomePage(driver=driver)


@pytest.fixture
def main_page(driver, auth_page, credentials_with_cabinet): 
    driver.get(BasePage.url)
    auth_page.login(*credentials_with_cabinet)
    return MainPage(driver=driver)
