import os

import allure
from selene import browser, by

from saucedemo_test.data.products import backpack, Product
from dotenv import load_dotenv

load_dotenv()
standard_user_name = os.getenv('STANDARD_USER_NAME')
user_password = os.getenv('USER_PASSWORD')


def standard_user_login():
    with allure.step('Open main page'):
        browser.open('/')

    with allure.step('Fill the login form'):
        browser.element('#user-name').type(standard_user_name)
        browser.element('#password').type(user_password)
    with allure.step('Submit the login form'):
        browser.element('#login-button').click()


def add_to_cart(product: Product):
    with allure.step('Add product to cart'):
        browser.element(f'{product.add_id}').click()


def remove_from_cart(product: Product):
    with allure.step('Remove product from the cart'):
        browser.element(f'{product.remove_id}').click()
