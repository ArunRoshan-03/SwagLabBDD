import time
from faker import Faker
from selenium.common import NoSuchElementException

from libs.driver_commands import BasicActions

fake = Faker()


class Product_Page(BasicActions):

    def __init__(self, driver):
        super().__init__(driver)
        self.add_cart_product = None
        self.product_list_name = None
        self.driver = driver
        self.first_name = fake.first_name()
        self.last_name = fake.last_name()
        self.pin_code = fake.zipcode()
        self.product_page_Xpath = "//span[@class='title']"
        self.filter_button_Xpath = "//select[@class='product_sort_container']"
        self.name_Z_to_A_button_Xpath = "//*[text()='Name (Z to A)']"
        self.product_list_Xpath = "//*[@class='inventory_item_name']"
        self.add_cart_label_Xpath = "//button[text()='Add to cart']"
        self.add_cart_button_Xpath = "//a[@class='shopping_cart_link']"
        self.check_out_button_Xpath = "//button[@id='checkout']"
        self.first_name_textbox_Xpath = "//input[@id='first-name']"
        self.last_name_textbox_Xpath = "//input[@id='last-name']"
        self.pincode_textbox_Xpath = "//input[@id='postal-code']"
        self.continue_button_Xpath = "//input[@id='continue']"
        self.add_cart_product_text_Xpath = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div/div[2]/a[" \
                                           "1]/div[1]"
        self.finish_button_Xpath = "//button[@id='finish']"
        self.order_placed_text_Xpath = "//h2[@class='complete-header'] | //div[@class='complete-text']"
        self.product_price_text_Xpath = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[" \
                                        "2]/div[2]/div[1]"
        self.cart_page_title_Xpath = "//span[@class='title']"
        self.continue_shopping_Button_Xpath = "//button[@id='continue-shopping']"
        self.remove_button_Xpath = "//*[@class='btn btn_secondary btn_small cart_button']"

    def product_page_title(self):
        self.wait_element(10)
        product_title_text = self.get_text_element(self.product_page_Xpath)
        print("Product page title :", product_title_text)
        self.verify_text(self.product_page_Xpath, "Products")

    def product_list(self):
        self.wait_element(10)
        self.product_list_name = self.get_text_elements(self.product_list_Xpath)
        print(self.product_list_name)
        return self.product_list_name

    def click_add_cart_label(self, count):
        self.wait_element(10)
        self.find_elements_to_random_click(self.add_cart_label_Xpath, count)

    def click_add_cart_button(self):
        self.wait_element(10)
        self.click_element(self.add_cart_button_Xpath)
        self.wait_element(10)
        self.add_cart_product = self.get_text_elements(self.add_cart_product_text_Xpath)
        self.element_is_displayed(self.add_cart_product_text_Xpath)
        assert self.add_cart_product is not None
        print("Total product", self.add_cart_product)
        return self.add_cart_product

    def verify_cart_page_title(self):
        self.wait_element(10)
        self.get_text_elements(self.cart_page_title_Xpath)

    def click_check_out_button(self):
        self.wait_element(10)
        self.click_element(self.check_out_button_Xpath)

    def information_detail(self):
        self.wait_element(10)
        self.enter_text_field(self.first_name_textbox_Xpath, self.first_name)
        self.verify_textbox(self.first_name_textbox_Xpath, self.first_name)

        self.enter_text_field(self.last_name_textbox_Xpath, self.last_name)
        self.verify_textbox(self.last_name_textbox_Xpath, self.last_name)

        self.enter_text_field(self.pincode_textbox_Xpath, self.pin_code)
        self.verify_textbox(self.pincode_textbox_Xpath, self.pin_code)

        self.wait_element(10)
        self.click_element(self.continue_button_Xpath)

    def verify_checkout_overview(self):
        checkout_products = self.get_text_elements(self.add_cart_product_text_Xpath)
        assert checkout_products is not None
        print("checkout", checkout_products)

    def click_finish_button(self):
        self.click_element(self.finish_button_Xpath)

    def verify_order_placed(self):
        order_placed_message = self.get_text_elements(self.order_placed_text_Xpath)
        print(order_placed_message)

    def verify_product_price(self):
        product_price = self.get_text_elements(self.product_price_text_Xpath)
        print(product_price)
        price_values = [price[1:] for price in product_price]
        sorted_prices = sorted(price_values, key=float)
        min_price = min(sorted_prices, key=float)
        self.scroll_to_element_by_text(min_price)
        self.click_add_cart_by_product_price(min_price)

    def click_continue_shopping_button(self):
        self.click_element(self.continue_shopping_Button_Xpath)

    def click_remove_button(self):
        self.wait_element(10)
        self.remove_cart_button(self.product_list_Xpath, 0)

    def click_remove_button_all_items(self):
        self.wait_element(10)
        self.click_all_button(self.remove_button_Xpath)

    def verify_all_product_removed(self):
        try:
            product_lists = self.find_elements(self.product_list_Xpath)
            if not product_lists:
                print("All your products have been removed from the cart")
            else:
                print("Something went wrong. Products were not removed.")
        except NoSuchElementException:
            print("Product list elements not found. Something went wrong.")
