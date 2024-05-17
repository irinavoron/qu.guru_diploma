import allure
from allure_commons.types import Severity

from swagLabs_ui_tests.utils.helpers import successful_login
from swagLabs_ui_tests.application import app
from swagLabs_ui_tests.data import products
from swagLabs_ui_tests.utils.allure_marks import feature, owner

pytestmark = [
    feature('Cart'),
    owner('irinaV')
]


@allure.title('The added product can be removed from the cart')
@allure.tag('web')
@allure.story('The cart is empty after deleting the added product from it')
@allure.severity(Severity.NORMAL)
def test_product_can_be_removed_from_cart():
    successful_login()
    app.inventory_page.add_product_to_cart(products.backpack)
    app.inventory_page.open_cart()

    app.cart.remove_product(products.backpack)

    app.cart.verify_is_empty()


@allure.title('The user can proceed to checkout from the cart')
@allure.tag('web')
@allure.story('The user gets redirected to the checkout page after clicking "Checkout"')
@allure.severity(Severity.NORMAL)
def test_user_can_proceed_to_checkout_from_cart():
    successful_login()
    app.inventory_page.add_product_to_cart(products.backpack)
    app.inventory_page.open_cart()
    app.cart.go_to_checkout()

    app.checkout_page.verify_is_opened()

    app.cart.clear_cart(1)


@allure.title('The user can continue shopping from the cart')
@allure.tag('web')
@allure.story('The user gets redirected to the inventory page after clicking "Continue shopping"')
@allure.severity(Severity.NORMAL)
def test_user_can_continue_shopping_from_cart():
    successful_login()
    app.inventory_page.add_product_to_cart(products.backpack)
    app.inventory_page.open_cart()
    app.cart.continue_shopping()

    app.inventory_page.verify_is_opened()

    app.cart.clear_cart(1)


@allure.title('The cart stays persistent when switching between pages')
@allure.tag('web')
@allure.story('The added product stays in cart after switching to another page and back')
@allure.severity(Severity.CRITICAL)
def test_cart_persistence():
    successful_login()
    app.inventory_page.add_product_to_cart(products.backpack)
    app.inventory_page.open_cart()
    app.common.select_product(products.backpack)
    app.product_page.go_to_cart()

    app.common.product_details_match_selected_product(products.backpack)

    app.cart.clear_cart(1)
