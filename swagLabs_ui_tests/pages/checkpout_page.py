import allure
from selene import browser, have


class CheckoutPage:
    def verify_is_opened(self):
        with allure.step('Verify that checkout page is opened'):
            browser.element('[data-test=title]').should(have.text('Checkout: Your Information'))