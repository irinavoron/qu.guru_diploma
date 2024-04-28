import os

from selene import browser, be
from dotenv import load_dotenv

load_dotenv()
standard_user_name = os.getenv('STANDARD_USER_NAME')
user_password = os.getenv('USER_PASSWORD')


def test_standard_user_login():
    browser.open('/')

    browser.element('#user-name').type(standard_user_name)
    browser.element('#password').type(user_password)
    browser.element('#login-button').click()

    browser.element('.inventory_list').should(be.visible)
