from swagLabs_ui_tests.application import app
from swagLabs_ui_tests.pages.login_page import user_name, user_password


def successful_login():
    app.login_page.open_login_page()

    app.login_page.fill_user_name(user_name)
    app.login_page.fill_password(user_password)
    app.login_page.submit_login_form()
