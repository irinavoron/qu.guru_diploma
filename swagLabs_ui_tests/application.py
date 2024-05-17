from swagLabs_ui_tests.pages.cart import Cart
from swagLabs_ui_tests.pages.checkpout_page import CheckoutPage
from swagLabs_ui_tests.pages.common import Common
from swagLabs_ui_tests.pages.inventory_page import InventoryPage
from swagLabs_ui_tests.pages.login_page import LoginPage
from swagLabs_ui_tests.pages.product_page import ProductPage


class ApplicationManager:
    def __init__(self):
        self.cart = Cart()
        self.login_page = LoginPage()
        self.inventory_page = InventoryPage()
        self.product_page = ProductPage()
        self.checkout_page = CheckoutPage()
        self.common = Common()


app = ApplicationManager()
