import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from pages.roi_calculator import ROICalculatorPage
from utils.helpers import safe_click, safe_read, safe_find_element


@pytest.fixture
def setup():
    options = Options()
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument("start-maximized")
    options.add_argument("--disable-extensions")
    path = Service('C:/Users/seanp/Desktop/Self Improvement/chromedriver-win64/chromedriver-win64/chromedriver.exe')
    driver = webdriver.Chrome(service=path, options=options)

    driver.get("http://www.entrio.io/roi")
    time.sleep(5)

    return driver


# def test_calculate_roi(setup):
#     page = ROICalculatorPage(setup)
#     expected_value = 'See how Entrio can help your organization'
#
#     accept_cookie = page.find_element('accept_cookie')
#     safe_click(accept_cookie)
#
#     setup.execute_script("window.scrollTo(0, 1000);")
#
#     contact_button_element = page.find_element('start_saving_button')
#     safe_click(contact_button_element)
#
#     contact_page_title = page.find_element('contact_page_text')
#     actual_value = safe_read(contact_page_title)
#
#     assert actual_value == expected_value
