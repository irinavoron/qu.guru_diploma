import allure
from selene import browser


class ProductPage:
    def go_to_cart(self):
        with allure.step('Go back to cart from the product page'):
            browser.element('#shopping_cart_container').click()