from swagLabs_ui_tests.data.products import Product
import allure
from selene import browser, be, have


class InventoryPage:
    def add_product_to_cart(self, product: Product):
        with allure.step('Add product to cart'):
            browser.element(f'{product.add_id}').click()

    def open_cart(self):
        with allure.step('Open cart by clicking cart icon'):
            browser.element('.shopping_cart_link').click()

    def verify_is_opened(self):
        with allure.step('Verify that inventory page is opened'):
            browser.element('.inventory_list').should(be.visible)

    def verify_cart_badge_shows_added_items_qty(self, qty):
        with allure.step('The cart badge shows number of added items'):
            browser.element('.shopping_cart_badge').should(have.text(f'{qty}'))
