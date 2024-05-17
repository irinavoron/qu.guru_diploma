import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from config import config
from swagLabs_ui_tests.utils import attach


@pytest.fixture(autouse=True, scope='function')
def browser_management():
    options = Options()

    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "120.0",
        "selenoid:options": {
            "enableVideo": True,
            "enableVNC": True
        }
    }

    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f'https://{config.SELENOID_LOGIN}:{config.SELENOID_PASSWORD}@{config.SELENOID_URL}/wd/hub',
        options=options)
    browser.config.driver = driver

    browser.config.base_url = config.BASE_URL
    browser.config.window_width = config.WINDOW_WIDTH
    browser.config.window_height = config.WINDOW_HEIGHT

    yield

    attach.add_screenshot()
    attach.add_logs()
    attach.add_html()
    attach.add_video()

    browser.quit()
