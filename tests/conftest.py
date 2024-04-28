import os

import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv


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

    load_dotenv()
    url = os.getenv('SELENOID_URL')
    login = os.getenv('SELENOID_LOGIN')
    password = os.getenv('SELENOID_PASSWORD')
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f'https://{login}:{password}@{url}/wd/hub',
        options=options)
    browser.config.driver = driver

    browser.config.base_url = 'https://www.saucedemo.com'
    browser.config.window_width = 1896
    browser.config.window_height = 1096

    yield

    browser.quit()
