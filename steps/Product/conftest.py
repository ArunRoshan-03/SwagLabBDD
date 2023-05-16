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


@then('I navigate to product page')
@when('I navigate to product page')
def product_page(browser):
    product_pages = Product_Page(browser)
    product_pages.product_title()


@then('I wil check that the product is visible on the product page.')
def product_list(browser):
    product_pages = Product_Page(browser)
    product_pages.product_list()


@when('I click on random product')
def click_random_product(browser):
    product_pages = Product_Page(browser)
    product_pages.click_add_cart_label()


@when('I processed to cart with random product')
@then('I processed to cart with random product')
def add_cart_verification(browser):
    product_pages = Product_Page(browser)
    product_pages.click_add_cart_button()
    product_pages.click_check_out_button()
    product_pages.information_detail()


@then('I validate the product as successful ordered.')
def product_ordered_verification(browser):
    product_pages = Product_Page(browser)
    product_pages.verify_checkout_overview()
    product_pages.click_finish_button()
    product_pages.verify_order_placed()


@then('I validate the least product price on the product page')
def verify_least_product_price(browser):
    product_pages = Product_Page(browser)
    product_pages.verify_product_price()

