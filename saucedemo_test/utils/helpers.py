import os
import allure
from selene import browser, have

from saucedemo_test.data.products import backpack, Product
from dotenv import load_dotenv

load_dotenv()
user_name = os.getenv('USER_NAME')
user_password = os.getenv('USER_PASSWORD')


def successful_login():
    with allure.step('Open main page'):
        browser.open('/')

    with allure.step('Fill the login form'):
        browser.element('#user-name').type(user_name)
        browser.element('#password').type(user_password)
    with allure.step('Submit the login form'):
        browser.element('#login-button').click()


def add_to_cart(product: Product):
    with allure.step('Add product to cart'):
        browser.element(f'{product.add_id}').click()


def remove_product_from_cart(product: Product):
    with allure.step('Remove product from the cart'):
        browser.element(f'{product.remove_id}').click()


def clear_cart(products_qty):
    with allure.step('Clear cart'):
        browser.open('/cart.html')
        for product in range(products_qty):
            browser.element('[name^=remove]').click()


def open_cart_from_catalogue():
    with allure.step('Open cart by clicking cart item'):
        browser.element('.shopping_cart_link').click()


def select_product(product: Product):
    with allure.step('Select product'):
        browser.element(product.id).click()


def product_details_match_selected_product(product: Product):
    with allure.step('Verify product details match selected product'):
        browser.element('[data-test=inventory-item-name]'
                        ).should(have.text(product.name))
        browser.element('[data-test=inventory-item-price]'
                        ).should(have.text(product.price))
