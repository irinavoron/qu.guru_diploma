import os

import allure
from allure_commons.types import Severity
from selene import browser, have
from dotenv import load_dotenv

from saucedemo_test.data import products
from saucedemo_test.pages import login_page
from saucedemo_test.pages.common import select_product, product_details_match_selected_product
from saucedemo_test.pages.inventory_page import InventoryPage
from saucedemo_test.pages.cart_page import Cart

inventory_page = InventoryPage()
cart = Cart()

load_dotenv()
user_name = os.getenv('USER_NAME')
user_password = os.getenv('USER_PASSWORD')


@allure.title('Cart badge displays items number')
@allure.tag('web')
@allure.story('The user can see the number of the added products on the cart icon')
@allure.feature('Inventory page')
@allure.label('owner', 'irinaV')
@allure.severity(Severity.MINOR)
def test_cart_badge_displays_items_number():
    login_page.successful_login()
    inventory_page.add_product_to_cart(products.backpack)

    with allure.step('The cart badge shows number of added items - 1'):
        browser.element('.shopping_cart_badge').should(have.text('1'))

    inventory_page.add_product_to_cart(products.bike_light)

    with allure.step('The cart badge shows number of added items - 2'):
        browser.element('.shopping_cart_badge').should(have.text('2'))

    cart.clear_cart(2)


@allure.title('Product can be added to cart')
@allure.tag('web', 'smoke')
@allure.story('The user can see the added product in the cart')
@allure.feature('Inventory page')
@allure.label('owner', 'irinaV')
@allure.severity(Severity.BLOCKER)
def test_product_is_added_to_cart():
    login_page.successful_login()
    inventory_page.add_product_to_cart(products.backpack)
    inventory_page.open_cart()

    product_details_match_selected_product(products.backpack)

    cart.clear_cart(1)


@allure.title('The product page is opened after clicking the product')
@allure.tag('web')
@allure.story('The user can open product page from the inventory page')
@allure.feature('Inventory page')
@allure.label('owner', 'irinaV')
@allure.severity(Severity.NORMAL)
def test_product_page_can_be_opened_from_inventory_page():
    login_page.successful_login()

    select_product(products.bike_light)

    product_details_match_selected_product(products.bike_light)


