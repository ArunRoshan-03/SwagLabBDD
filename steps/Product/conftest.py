from pytest_bdd import parsers, given, then, when

from libs.login_page import Login_page
from libs.product_page import Product_Page


@when(parsers.parse('I fill the username : {standard_user}  and password : {secret_sauce} on the login page'))
def login_details(browser, standard_user, secret_sauce):
    login_pages = Login_page(browser)
    login_pages.username_credentials(standard_user)
    login_pages.password_credentials(secret_sauce)


@when('I click login button on the loginpage')
def login_button(browser):
    login_pages = Login_page(browser)
    login_pages.login_button()


@when('I navigate to home page')
@then('I wil check that the product is visible on the product page.')
def product_page(browser):
    product_pages = Product_Page(browser)
    product_pages.product_title()


@when('I click the filter button and select "name (Z to A)".')
def filter_button(browser):
    product_pages = Product_Page(browser)
    product_pages.click_filter_button()
    product_pages.click_name_A_to_Z_button()


@then('I validate the product list by clicking the filter button.')
def product_list(browser):
    product_pages = Product_Page(browser)
    product_pages.verify_product_list()
