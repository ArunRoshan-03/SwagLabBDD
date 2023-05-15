import time

from selenium.common import NoSuchElementException

from libs.driver_commands import BasicActions


class Login_page(BasicActions):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.login_page_text_Xpath = "//div[@class='login_logo']"
        self.login_credentials_text_Xpath = "//div[@class='login_credentials_wrap-inner']"
        self.username_textbox_Xpath = "//input[@id='user-name']"
        self.password_textbox_Xpath = "//input[@id='password']"
        self.login_button_Xpath = "//input[@id='login-button']"
        self.homepage_Xpath = "//span[@class='title']"
        self.error_message = "//h3[@data-test='error']"

    def login_page(self):
        self.wait_element(12)
        self.element_is_displayed(self.login_page_text_Xpath)
        # assert status is True
        page_title = self.get_text_element(self.login_page_text_Xpath)
        print(page_title)

    def login_credentials_label(self):
        self.wait_element(12)
        self.element_is_displayed(self.login_credentials_text_Xpath)
        login_credentials_text = self.get_text_element(self.login_credentials_text_Xpath)
        print(login_credentials_text)

    def username_credentials(self, username):
        self.wait_element(10)
        if username == "standard_user":
            self.type_by_xpath(self.username_textbox_Xpath, username)
        elif username == "locked_out_user":
            try:
                self.type_by_xpath(self.username_textbox_Xpath, username)
            except NoSuchElementException as noSuchElementException:
                print(noSuchElementException)
            else:
                login_error_message_text = self.get_text_element(self.error_message)
                print(login_error_message_text)
        elif username == "problem_user":
            self.type_by_xpath(self.username_textbox_Xpath, username)
        elif username == "performance_glitch_user":
            self.type_by_xpath(self.username_textbox_Xpath, username)

    def password_credentials(self, password):
        self.type_by_xpath(self.password_textbox_Xpath, password)

    def login_button(self):
        self.wait_element(10)
        self.click_element(self.login_button_Xpath)

    def swag_homepage(self):
        self.wait_element(12)
        home_page_title_text = self.get_text_element(self.homepage_Xpath)
        print("Home page :", home_page_title_text)
        self.element_is_displayed(self.homepage_Xpath)
