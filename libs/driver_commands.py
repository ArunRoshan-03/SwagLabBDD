from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasicActions:

    def __init__(self, web_driver):
        self.web_elements = None
        self.text = None
        self.title = None
        self.web_element = WebElement
        self.web_driver = web_driver

    def click_by_xpath(self, locator):
        try:
            self.web_element = self.web_driver.find_element(By.XPATH, locator)
        except NoSuchElementException:
            print("No Such element")
        finally:
            try:
                WebDriverWait(self.web_driver, 10). \
                    until(expected_conditions.element_to_be_clickable(self.web_element))
                self.web_element.click()
            except Exception as error:
                print(error)

    def type_by_xpath(self, locator, value):
        try:
            self.web_element = self.web_driver.find_element(By.XPATH, locator)
        except NoSuchElementException:
            print("No Such element")
            assert False
        finally:
            try:
                WebDriverWait(self.web_driver, 10).until(expected_conditions.element_to_be_clickable(self.web_element))
                self.web_element.send_keys(value)
            except Exception as error:
                print(error)

    def clear_by_xpath(self, locator):
        try:
            self.web_element = self.web_driver.find_element(By.XPATH, locator)
        except NoSuchElementException:
            print("No Such element")
            assert False
        finally:
            try:
                WebDriverWait(self.web_driver, 10).until(expected_conditions.element_to_be_clickable(self.web_element))
                self.web_element.clear()
            except Exception as error:
                print(error)

    def select_by_xpath(self, locator, value):
        try:
            self.web_element = self.web_driver.find_element(By.XPATH, locator)
        except NoSuchElementException:
            print("No Such element")
            assert False
        finally:
            try:
                WebDriverWait(self.web_driver, 10).until(expected_conditions.element_to_be_clickable(self.web_element))
                select = Select(self.web_element)
                select.select_by_visible_text(value)
            except Exception as error:
                print(error)

    def get_text_by_xpath(self, locator):
        text = None
        try:
            self.web_element = self.web_driver.find_element(By.XPATH, locator)
        except NoSuchElementException:
            print("No Such element")
            assert False
        finally:
            try:
                text = self.web_element.text

            except Exception as error:
                print(error)
        return text

    def move_by_xpath(self, locator):

        try:
            self.web_element = self.web_driver.find_element(By.XPATH, locator)
        except NoSuchElementException:
            print("No Such element")
            assert False
        finally:
            try:
                WebDriverWait(self.web_driver, 10).until(expected_conditions.element_to_be_clickable(self.web_element))
                action = ActionChains(self.web_driver)
                action.move_to_element(self.web_element).perform()
            except Exception as error:
                print(error)

    def get_title(self):
        self.title = self.web_driver.title
        return self.title

    def get_elements_text(self, locator):
        list_text = []
        web_elements = None
        try:
            web_elements = self.web_driver.find_elements(By.XPATH, locator)
        except NoSuchElementException:
            print("No Such element")
            assert False
        finally:
            try:
                if len(web_elements) > 1:
                    for web_element in web_elements:
                        self.web_element = web_element
                        self.text = self.web_element.text
                        list_text.append(self.text)
                else:
                    self.web_element = self.web_driver.find_element(By.XPATH, locator)
                    self.text = self.web_element.text
                    list_text.append(self.text)

            except Exception as error:
                print(error)
            return list_text

    def element_is_displayed(self, locator):
        self.web_element = self.web_driver.find_element(By.XPATH, locator)
        return self.web_element.is_displayed()

    def navigate_back(self):
        self.web_driver.back()

    def scroll_down(self):
        self.web_driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    def refresh(self):
        self.web_driver.refresh()

    def get_url(self, url):
        self.web_driver.get(url)

    def wait_element(self, wait_time):
        self.web_driver.implicitly_wait(wait_time)
