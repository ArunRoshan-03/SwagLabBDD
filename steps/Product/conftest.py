from pytest_bdd import parsers, then, when

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
@then('I validate the product page')
def product_page(browser):
    product_pages = Product_Page(browser)
    product_pages.product_page_title()


@then('I wil check that the product is visible on the product page.')
def product_list(browser):
    product_pages = Product_Page(browser)
    product_pages.product_list()


@when('I click on random product')
def click_random_product(browser):
    product_pages = Product_Page(browser)
    product_pages.click_add_cart_label(1)


@when('I processed to cart with random product')
@then('I processed to cart with random product')
@when('I processed to cart with multiple products')
def add_cart_verification(browser):
    product_pages = Product_Page(browser)
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


@when('I add multiple_items to cart')
def add_multiple_cart(browser):
    product_pages = Product_Page(browser)
    product_pages.click_add_cart_label(2)


@when('I navigate to the cart_page')
@then('I navigate to the cart_page')
def verify_cart_page(browser):
    product_pages = Product_Page(browser)
    product_pages.click_add_cart_button()
    product_pages.verify_cart_page_title()


@when('I click continue_shopping on the cart_page')
def continue_shopping_verification(browser):
    product_pages = Product_Page(browser)
    product_pages.click_continue_shopping_button()


@then('I validate particular item remove from cart')
def verify_remove_product(browser):
    product_pages = Product_Page(browser)
    product_pages.click_remove_button()


@when('I remove all items from cart')
def remove_all_product(browser):
    product_pages = Product_Page(browser)
    product_pages.click_remove_button_all_items()


@then('I validate the empty cart_page')
def verify_empty_cart_page(browser):
    product_pages = Product_Page(browser)
    product_pages.verify_all_product_removed()
