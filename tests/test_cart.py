import allure
from allure_commons.types import Severity
from selene import browser, have, be

from saucedemo_test.data import products
from saucedemo_test.pages import login_page, common
from tests.test_inventory_page import inventory_page, cart


@allure.title('The added product can be removed from the cart')
@allure.tag('web')
@allure.story('The cart is empty after deleting the added product from it')
@allure.feature('Cart')
@allure.label('owner', 'irinaV')
@allure.severity(Severity.NORMAL)
def test_product_can_be_removed_from_cart():
    login_page.successful_login()
    inventory_page.add_product_to_cart(products.backpack)
    inventory_page.open_cart()

    cart.remove_product(products.backpack)

    items_list = browser.all('.cart_item')
    with allure.step('Verify the cart is empty'):
        items_list.should(have.size(0))


@allure.title('The user can proceed to checkout from the cart')
@allure.tag('web')
@allure.story('The user gets redirected to the checkout page after clicking "Checkout"')
#@allure.feature('Cart')
@allure.label('owner', 'irinaV')
@allure.severity(Severity.NORMAL)
def test_user_can_proceed_to_checkout_from_cart():
    login_page.successful_login()
    inventory_page.add_product_to_cart(products.backpack)
    inventory_page.open_cart()

    with allure.step('Click "checkout" button'):
        browser.element('#checkout').click()

    with allure.step('Verify that checkout page is opened'):
        browser.element('[data-test=title]').should(have.text('Checkout: Your Information'))

    cart.clear_cart(1)


@allure.title('The user can continue shopping from the cart')
@allure.tag('web')
@allure.story('The user gets redirected to the inventory page after clicking "Continue shopping"')
#@allure.feature('Cart')
@allure.label('owner', 'irinaV')
@allure.severity(Severity.NORMAL)
def test_user_can_continue_shopping_from_cart():
    login_page.successful_login()
    inventory_page.add_product_to_cart(products.backpack)
    inventory_page.open_cart()

    with allure.step('Click "checkout" button'):
        browser.element('#continue-shopping').click()

    with allure.step('Verify that catalogue page is opened'):
        browser.element('.inventory_list').should(be.visible)

    cart.clear_cart(1)


@allure.title('The cart stays persistent when switching between pages')
@allure.tag('web')
@allure.story('The added product stays in cart after switching to another page and back')
#@allure.feature('Cart')
@allure.label('owner', 'irinaV')
@allure.severity(Severity.CRITICAL)
def test_cart_persistence():
    login_page.successful_login()
    inventory_page.add_product_to_cart(products.backpack)
    inventory_page.open_cart()

    common.select_product(products.backpack)
    with allure.step('Go back to cart from the product page'):
        browser.element('#shopping_cart_container').click()

    common.product_details_match_selected_product(products.backpack)

    cart.clear_cart(1)
