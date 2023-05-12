import pytest
from pytest_bdd import when, given, then, parsers
from selenium import webdriver
from constants.constants import website_url
from libs.login_page import Login_page


@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    driver.get(website_url)
    driver.maximize_window()

    yield driver
    driver.close()


@given("user launch browser")
@given("user enters the swag labs url and is taken to the swag labs web page")
@when("The user should check their credentials on the login page.")
def login_homepage(browser):
    login_pages = Login_page(browser)
    login_pages.login_page()


@then("I validate login credentials on the login page")
def login_credentials_label(browser):
    login_pages = Login_page(browser)
    login_pages.login_credentials_label()


@when(parsers.parse("I fill the username <username> and password <password> on login page"))
def username_textbox(browser, username, password):
    login_pages = Login_page(browser)
    login_pages.username_credentials(username)
    login_pages.password_credentials(password)


@when("click on the login Button")
def login_button(browser):
    login_pages = Login_page(browser)
    login_pages.login_button()


@then('I validate the home_page')
def home_page(browser):
    login_pages = Login_page(browser)
    login_pages.swag_homepage()

