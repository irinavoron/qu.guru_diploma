import allure
from selene import browser, have

from swagLabs_ui_tests.data.products import Product


class Common:
    def select_product(self, product: Product):
        with allure.step('Select product'):
            browser.element(product.id).click()


    def product_details_match_selected_product(self, product: Product):
        with allure.step('Verify product details match selected product'):
            browser.element('[data-test=inventory-item-name]'
                            ).should(have.text(product.name))
            browser.element('[data-test=inventory-item-price]'
                            ).should(have.text(product.price))
