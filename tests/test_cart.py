import allure
from allure_commons.types import Severity
from selene import browser, have, be

from swagLabs_ui_tests.data import products
from swagLabs_ui_tests.pages import login_page
from swagLabs_ui_tests.pages.cart_page import Cart
from swagLabs_ui_tests.pages.common import Common
from swagLabs_ui_tests.pages.inventory_page import InventoryPage
from swagLabs_ui_tests.pages.product_page import ProductPage
from swagLabs_ui_tests.utils.allure_marks import feature, owner

pytestmark = [
    feature('Cart'),
    owner('irinaV')
]

inventory_page = InventoryPage()
cart = Cart()
common = Common()
product_page = ProductPage()


@allure.title('The added product can be removed from the cart')
@allure.tag('web')
@allure.story('The cart is empty after deleting the added product from it')
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
@allure.severity(Severity.NORMAL)
def test_user_can_proceed_to_checkout_from_cart():
    login_page.successful_login()
    inventory_page.add_product_to_cart(products.backpack)
    inventory_page.open_cart()
    cart.go_to_checkout()

    with allure.step('Verify that checkout page is opened'):
        browser.element('[data-test=title]').should(have.text('Checkout: Your Information'))

    cart.clear_cart(1)


@allure.title('The user can continue shopping from the cart')
@allure.tag('web')
@allure.story('The user gets redirected to the inventory page after clicking "Continue shopping"')
@allure.severity(Severity.NORMAL)
def test_user_can_continue_shopping_from_cart():
    login_page.successful_login()
    inventory_page.add_product_to_cart(products.backpack)
    inventory_page.open_cart()
    cart.continue_shopping()

    with allure.step('Verify that catalogue page is opened'):
        browser.element('.inventory_list').should(be.visible)

    cart.clear_cart(1)


@allure.title('The cart stays persistent when switching between pages')
@allure.tag('web')
@allure.story('The added product stays in cart after switching to another page and back')
@allure.severity(Severity.CRITICAL)
def test_cart_persistence():
    login_page.successful_login()
    inventory_page.add_product_to_cart(products.backpack)
    inventory_page.open_cart()
    common.select_product(products.backpack)
    product_page.go_to_cart()

    common.product_details_match_selected_product(products.backpack)

    cart.clear_cart(1)
