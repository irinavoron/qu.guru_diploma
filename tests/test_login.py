import allure
from selene import browser, be, have

from saucedemo_test.data import products
from saucedemo_test.utils.helpers import standard_user_login, add_to_cart, remove_product_from_cart, clear_cart, \
    open_cart_from_catalogue


def test_standard_user_login():
    standard_user_login()

    with allure.step('The catalogue is opened after logging in'):
        browser.element('.inventory_list').should(be.visible)


def test_cart_badge_displays_items_number():
    standard_user_login()
    add_to_cart(products.backpack)

    with allure.step('The cart badge shows number of added items - 1'):
        browser.element('.shopping_cart_badge').should(have.text('1'))

    add_to_cart(products.bike_light)

    with allure.step('The cart badge shows number of added items - 2'):
        browser.element('.shopping_cart_badge').should(have.text('2'))

    clear_cart(2)


def test_product_is_added_to_cart():
    standard_user_login()
    add_to_cart(products.backpack)
    open_cart_from_catalogue()

    with ((allure.step('Verify cart product details match added product'))):
        browser.element('[data-test=inventory-item-name]'
                        ).should(have.text(products.backpack.name))
        browser.element('[data-test=inventory-item-price]'
                        ).should(have.text(products.backpack.price))

    clear_cart(1)


def test_product_can_be_deleted_from_cart():
    standard_user_login()
    add_to_cart(products.backpack)
    open_cart_from_catalogue()

    remove_product_from_cart(products.backpack)

    items_list = browser.all('.cart_item')
    with allure.step('Verify the cart is empty'):
        items_list.should(have.size(0))
