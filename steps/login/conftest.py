from pytest_bdd import when, then, parsers
from libs.login_page import Login_page


@when(parsers.parse("I fill the username {username} and password {password} on login_page"))
def login_details(browser, username, password):
    login_pages = Login_page(browser)
    login_pages.username_credentials(username)
    login_pages.password_credentials(password)


@when('I click login button on the loginpage')
def login_button(browser):
    login_pages = Login_page(browser)
    login_pages.login_button()


@then('I validate the home_page with various users.')
def home_page(browser):
    login_pages = Login_page(browser)
    login_pages.swag_homepage()
