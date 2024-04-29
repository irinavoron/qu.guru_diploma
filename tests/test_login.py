import os
import allure
from selene import browser, be, have
from dotenv import load_dotenv

from saucedemo_test.data import products
from saucedemo_test.utils.helpers import standard_user_login, add_to_cart, remove_from_cart


def test_standard_user_login():
    standard_user_login()

    with allure.step('The catalogue is opened after logging in'):
        browser.element('.inventory_list').should(be.visible)


def test_cart_badge_displays_the_items_number():

    standard_user_login()
    add_to_cart(products.backpack)

    with allure.step('The cart badge shows number of added items - 1'):
        browser.element('.shopping_cart_badge').should(have.text('1'))

    add_to_cart(products.bike_light)

    with allure.step('The cart badge shows number of added items - 2'):
        browser.element('.shopping_cart_badge').should(have.text('2'))



