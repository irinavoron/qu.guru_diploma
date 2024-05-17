import allure
from selene import browser, have

from swagLabs_ui_tests.data.products import Product


class Cart:
    def remove_product(self, product: Product):
        with allure.step('Remove product from the cart'):
            browser.element(f'{product.remove_id}').click()

    def clear_cart(self, products_qty):
        with allure.step('Clear cart'):
            browser.open('/cart.html')
            for product in range(products_qty):
                browser.element('[name^=remove]').click()

    def go_to_checkout(self):
        with allure.step('Click "checkout" button'):
            browser.element('#checkout').click()

    def continue_shopping(self):
        with allure.step('Click "continue-shopping" button'):
            browser.element('#continue-shopping').click()


    def verify_is_empty(self):
        items_list = browser.all('.cart_item')
        with allure.step('Verify the cart is empty'):
            items_list.should(have.size(0))
