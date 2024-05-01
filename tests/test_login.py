import allure
import pytest
from allure_commons.types import Severity
from selene import browser, be

from saucedemo_test.pages import login_page
from tests.test_saucedemo import user_password, user_name


@allure.title('Successful login')
@allure.tag('web', 'smoke')
@allure.story('User can login with valid creds')
@allure.feature('Login')
@allure.label('owner', 'irinaV')
@allure.severity(Severity.BLOCKER)
def test_successful_login():
    login_page.successful_login()

    with allure.step('The catalogue is opened after logging in'):
        browser.element('.inventory_list').should(be.visible)


@allure.title('Unsuccessful login')
@allure.tag('web')
@allure.story('User can`t login with invalid creds')
@allure.feature('Login')
@allure.label('owner', 'irinaV')
@allure.severity(Severity.CRITICAL)
@pytest.mark.parametrize(
    'login, password', [
        ('wrong_name', {user_password}),
        ({user_name}, 'wrong_password'),
        ('', ''),
        ('locked_out_user', {user_password})
    ],
    ids=['invalid name', 'invalid password', 'empty form', 'locked out user']
)
def test_unsuccessful_login(login, password):
    login_page.unsuccessful_login(login, password)

    with allure.step('Verify that error message is displayed'):
        browser.element('.error-button').should(be.visible)
