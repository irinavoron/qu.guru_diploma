import allure
from selene import browser

from saucedemo_diploma_project_test.data.products import Product


@allure.feature('Cart')
class Cart:
    def remove_product(self, product: Product):
        with allure.step('Remove product from the cart'):
            browser.element(f'{product.remove_id}').click()

    def clear_cart(self, products_qty):
        with allure.step('Clear cart'):
            browser.open('/cart.html')
            for product in range(products_qty):
                browser.element('[name^=remove]').click()
