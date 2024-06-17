from selenium.webdriver.common.by import By
from utils.helpers import safe_click, safe_read, safe_find_element, safe_send_keys


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.elements = {}

    def find_element(self, key, wait_for_visibility=True):
        value = self.elements[key][1]
        return safe_find_element(self.driver, self.elements[key][0], value, wait_for_visibility)

    def click(self, key):
        element = self.find_element(key)
        if element:
            safe_click(element)

    def read_text(self, key):
        element = self.find_element(key)
        if element:
            return safe_read(element)
        return None

    def send_keys(self, element, keys):
        if element:
            safe_send_keys(element, keys)
