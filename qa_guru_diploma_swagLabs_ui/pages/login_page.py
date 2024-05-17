import os
import allure
from selene import browser
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


login_page = LoginPage()


def successful_login():
    login_page.open_login_page()

    login_page.fill_user_name(user_name)
    login_page.fill_password(user_password)
    login_page.submit_login_form()


def unsuccessful_login(login, password):
    login_page.open_login_page()

    login_page.fill_user_name(login)
    login_page.fill_password(password)
    login_page.submit_login_form()
