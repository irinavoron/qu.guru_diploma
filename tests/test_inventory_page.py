import allure
from allure_commons.types import Severity

from swagLabs_ui_tests.application import app
from swagLabs_ui_tests.data import products
from swagLabs_ui_tests.utils.helpers import successful_login
from swagLabs_ui_tests.utils.allure_marks import feature, owner

pytestmark = [
    feature('Inventory Page'),
    owner('irinaV')
]


@allure.title('Cart badge displays items number')
@allure.tag('web')
@allure.story('The user can see the number of the added products on the cart icon')
@allure.severity(Severity.MINOR)
def test_cart_badge_displays_items_number():
    successful_login()
    app.inventory_page.add_product_to_cart(products.backpack)

    app.inventory_page.verify_cart_badge_shows_added_items_qty(1)

    app.inventory_page.add_product_to_cart(products.bike_light)

    app.inventory_page.verify_cart_badge_shows_added_items_qty(2)

    app.cart.clear_cart(2)


@allure.title('Product can be added to cart')
@allure.tag('web', 'smoke')
@allure.story('The user can see the added product in the cart')
@allure.severity(Severity.BLOCKER)
def test_product_is_added_to_cart():
    successful_login()
    app.inventory_page.add_product_to_cart(products.backpack)
    app.inventory_page.open_cart()

    app.common.product_details_match_selected_product(products.backpack)

    app.cart.clear_cart(1)


@allure.title('The product page is opened after clicking the product')
@allure.tag('web')
@allure.story('The user can open product page from the inventory page')
@allure.severity(Severity.NORMAL)
def test_product_page_can_be_opened_from_inventory_page():
    successful_login()
    app.common.select_product(products.bike_light)

    app.common.product_details_match_selected_product(products.bike_light)
