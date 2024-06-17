import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from pages.roi_calculator import ROICalculatorPage
from utils.helpers import safe_click, safe_read, safe_find_element
from selenium.webdriver.common.by import By


@pytest.fixture
def setup():
    options = Options()
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument("start-maximized")
    # options.add_argument("--disable-extensions")
    path = Service('C:/Users/seanp/Desktop/Self Improvement/chromedriver-win64/chromedriver-win64/chromedriver.exe')
    driver = webdriver.Chrome(service=path, options=options)

    driver.get("https://www.entrio.io/contact")
    driver.implicitly_wait(10)

    return driver


def test_contact(setup):
    page = ROICalculatorPage(setup)
    expected_value = 'See how Entrio can help your organization'

    accept_cookie = page.find_element('accept_cookie')
    safe_click(accept_cookie)
    time.sleep(3)

    # iframe switch to find the important elements
    page.switch_to_correct_frame('info_frame')

    first_name_element = page.find_element('first_name')
    page.send_keys(first_name_element, 'Sean')

    first_name_element = page.find_element('last_name')
    page.send_keys(first_name_element, 'Sean')

    first_name_element = page.find_element('email')
    page.send_keys(first_name_element, 'Sean')

    first_name_element = page.find_element('phone')
    page.send_keys(first_name_element, 'Sean')

    first_name_element = page.find_element('message')
    page.send_keys(first_name_element, 'Sean')

    # ToDO test error messages by editing data
    # add submit > read error

    #do the dame on ROI

    assert actual_value == expected_value
