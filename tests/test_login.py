from selene import browser, be


def test_standard_user_login():
    browser.open('/')

    browser.element('#user-name').type('standard_user')
    browser.element('#password').type('secret_sauce')
    browser.element('#login-button').click()

    browser.element('.inventory_list').should(be.visible)