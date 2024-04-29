import allure
from selene import browser, be, have

from saucedemo_test.data import products
from saucedemo_test.utils.helpers import standard_user_login, add_to_cart, remove_product_from_cart, clear_cart, \
    open_cart_from_catalogue, select_product, product_details_match_selected_product


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

    product_details_match_selected_product(products.backpack)

    clear_cart(1)


def test_product_page_can_be_opened_from_inventory_page():
    standard_user_login()

    select_product(products.bike_light)

    product_details_match_selected_product(products.bike_light)


def test_product_can_be_removed_from_cart():
    standard_user_login()
    add_to_cart(products.backpack)
    open_cart_from_catalogue()

    remove_product_from_cart(products.backpack)

    items_list = browser.all('.cart_item')
    with allure.step('Verify the cart is empty'):
        items_list.should(have.size(0))


def test_user_can_proceed_to_checkout():
    standard_user_login()
    add_to_cart(products.backpack)
    open_cart_from_catalogue()

    with allure.step('Click "checkout" button'):
        browser.element('#checkout').click()

    with allure.step('Verify that checkout page is opened'):
        browser.element('[data-test=title]').should(have.text('Checkout: Your Information'))

    clear_cart(1)


def test_user_can_continue_shopping_from_cart():
    standard_user_login()
    add_to_cart(products.backpack)
    open_cart_from_catalogue()

    with allure.step('Click "checkout" button'):
        browser.element('#continue-shopping').click()

    with allure.step('Verify that catalogue page is opened'):
        browser.element('.inventory_list').should(be.visible)

    clear_cart(1)


def test_cart_persistence():
    standard_user_login()
    add_to_cart(products.backpack)
    open_cart_from_catalogue()

    select_product(products.backpack)
    with allure.step('Go back to cart from the product page'):
        browser.element('#shopping_cart_container').click()

    product_details_match_selected_product(products.backpack)

    clear_cart(1)
