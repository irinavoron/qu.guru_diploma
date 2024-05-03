from saucedemo_diploma_project_test.data.products import Product
import allure
from selene import browser


class InventoryPage:
    def add_product_to_cart(self, product: Product):
        with allure.step('Add product to cart'):
            browser.element(f'{product.add_id}').click()


    def open_cart(self):
        with allure.step('Open cart by clicking cart icon'):
            browser.element('.shopping_cart_link').click()
