import allure
import pytest
from allure_commons.types import Severity

from config import config
from swagLabs_ui_tests.application import app
from swagLabs_ui_tests.utils.helpers import successful_login
from swagLabs_ui_tests.utils.allure_marks import feature, owner

pytestmark = [
    feature('Login'),
    owner('irinaV')
]


@allure.title('Successful login')
@allure.tag('web', 'smoke')
@allure.story('The user can login with valid creds')
@allure.severity(Severity.BLOCKER)
def test_successful_login():
    successful_login()

    app.inventory_page.verify_is_opened()


@allure.title('Unsuccessful login')
@allure.tag('web')
@allure.story('The user can`t login with invalid creds')
@allure.severity(Severity.CRITICAL)
@pytest.mark.parametrize(
    'login, password', [
        ('wrong_name', {config.USER_PASSWORD}),
        ({config.USER_NAME}, 'wrong_password'),
        ('', ''),
        ('locked_out_user', {config.USER_PASSWORD})
    ],
    ids=['invalid name', 'invalid password', 'empty form', 'locked out user']
)
def test_unsuccessful_login(login, password):
    app.login_page.open_login_page()
    app.login_page.fill_user_name(login)
    app.login_page.fill_password(password)
    app.login_page.submit_login_form()

    app.login_page.verify_error_message_is_displayed()
