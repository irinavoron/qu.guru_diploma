import os
import allure
from selene import browser, be
from dotenv import load_dotenv

load_dotenv()
user_name = os.getenv('USER_NAME')
user_password = os.getenv('USER_PASSWORD')


class LoginPage:

    def open_login_page(self):
        with allure.step('Open login page'):
            browser.open('/')

    def fill_user_name(self, value):
        with allure.step('Fill user name'):
            browser.element('#user-name').type(value)

    def fill_password(self, value):
        with allure.step('Fill password'):
            browser.element('#password').type(value)

    def submit_login_form(self):
        with allure.step('Submit the login form'):
            browser.element('#login-button').click()

    def verify_error_message_is_displayed(self):
        with allure.step('Verify that error message is displayed'):
            browser.element('.error-button').should(be.visible)
