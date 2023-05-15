from libs.driver_commands import BasicActions


class Product_Page(BasicActions):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.product_page_Xpath = "//span[@class='title']"
        self.filter_button_Xpath = "//select[@class='product_sort_container']"
        self.name_A_to_Z_Xpath = "//*[@id='header_container']/div[2]/div/span/span"
        self.product_list_Xpath = "//*[@class='inventory_item_name']"

    def product_title(self):
        self.wait_element(10)
        product_title_text = self.get_text_element(self.product_page_Xpath)
        assert product_title_text in "Products"

    def click_filter_button(self):
        self.wait_element(10)
        self.click_element(self.filter_button_Xpath)

    def click_name_A_to_Z_button(self):
        self.wait_element(10)
        self.click_element(self.name_A_to_Z_Xpath)

    def verify_product_list(self):
        product_list = self.get_text_elements(self.product_list_Xpath)
        print(product_list)
