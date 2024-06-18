import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from pages.roi_calculator import ROICalculatorPage


@pytest.fixture
def setup():
    options = Options()
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument("start-maximized")
    # options.add_argument("--disable-extensions")
    path = Service('C:/Users/seanp/Desktop/Self Improvement/chromedriver-win64/chromedriver-win64/chromedriver.exe')
    driver = webdriver.Chrome(service=path, options=options)

    driver.get("https://www.entrio.io/roi")
    driver.implicitly_wait(10)

    return driver


def test_start_saving(setup):
    page = ROICalculatorPage(setup)
    expected_url = 'https://www.entrio.io/contact'
    accept_cookie = page.find_element('accept_cookie')
    page.click(accept_cookie)
    time.sleep(3)

    page.switch_to_correct_frame('roi_frame')

    button_element = page.find_element('start_saving_button')
    page.click(button_element)
    actual_url = setup.current_url

    assert expected_url == actual_url


def test_default_dollars(setup):
    page = ROICalculatorPage(setup)
    expected_savings = '$27,500,000'
    expected_annual = '$22,825,000'
    accept_cookie = page.find_element('accept_cookie')
    page.click(accept_cookie)
    time.sleep(3)

    page.switch_to_correct_frame('roi_frame')

    savings_element = page.find_element('estimated_savings')
    annual_element = page.find_element('annual_cost_avoidance')

    actual_savings = page.read_text(savings_element)
    actual_annual = page.read_text(annual_element)

    assert actual_savings == expected_savings and actual_annual == expected_annual


def test_regional_button(setup):
    page = ROICalculatorPage(setup)
    expected_savings = '$26,750,000'
    expected_annual = '$$22,202,500'
    accept_cookie = page.find_element('accept_cookie')
    page.click(accept_cookie)
    time.sleep(3)

    page.switch_to_correct_frame('roi_frame')

    regional_button_element = page.find_element('regional')
    page.click(regional_button_element)

    savings_element = page.find_element('estimated_savings')
    annual_element = page.find_element('annual_cost_avoidance')

    actual_savings = page.read_text(savings_element)
    actual_annual = page.read_text(annual_element)

    assert actual_savings == expected_savings and actual_annual == expected_annual


def test_local_button(setup):
    page = ROICalculatorPage(setup)
    expected_savings = '$26,250,000'
    expected_annual = '$21,787,500'
    accept_cookie = page.find_element('accept_cookie')
    page.click(accept_cookie)
    time.sleep(3)

    page.switch_to_correct_frame('roi_frame')

    local_button_element = page.find_element('local')
    page.click(local_button_element)

    savings_element = page.find_element('estimated_savings')
    annual_element = page.find_element('annual_cost_avoidance')

    actual_savings = page.read_text(savings_element)
    actual_annual = page.read_text(annual_element)

    assert actual_savings == expected_savings and actual_annual == expected_annual


def test_global_button(setup):
    page = ROICalculatorPage(setup)
    expected_savings = '$27,500,000'
    expected_annual = '$22,825,000'
    accept_cookie = page.find_element('accept_cookie')
    page.click(accept_cookie)
    time.sleep(3)

    page.switch_to_correct_frame('roi_frame')

    global_button_element = page.find_element('global')
    page.click(global_button_element)

    savings_element = page.find_element('estimated_savings')
    annual_element = page.find_element('annual_cost_avoidance')

    actual_savings = page.read_text(savings_element)
    actual_annual = page.read_text(annual_element)

    assert actual_savings == expected_savings and actual_annual == expected_annual


def test_contact_no_first_name(setup):
    page = ROICalculatorPage(setup)

    setup.get("https://www.entrio.io/contact")
    expected_value = 'Please complete all required fields.'

    accept_cookie = page.find_element('accept_cookie')
    page.click(accept_cookie)
    time.sleep(3)

    # iframe switch to find the important elements
    page.switch_to_correct_frame('info_frame')

    last_name_element = page.find_element('last_name')
    page.send_keys(last_name_element, 'Peer')

    email_element = page.find_element('email')
    page.send_keys(email_element, 'Sean@gmail.com')

    phone_element = page.find_element('phone')
    page.send_keys(phone_element, '0547700823')

    message_element = page.find_element('message')
    page.send_keys(message_element, 'Nothing can stop me, Im all the way up')

    submit_element = page.find_element('submit')
    page.click(submit_element)

    error_message_element = page.find_element('error_message')
    error_message_text = page.read_text(error_message_element)

    assert error_message_text == expected_value


def test_contact_no_last_name(setup):
    page = ROICalculatorPage(setup)

    setup.get("https://www.entrio.io/contact")
    expected_value = 'Please complete all required fields.'

    accept_cookie = page.find_element('accept_cookie')
    page.click(accept_cookie)
    time.sleep(3)

    # iframe switch to find the important elements
    page.switch_to_correct_frame('info_frame')

    first_name_element = page.find_element('first_name')
    page.send_keys(first_name_element, 'Sean')

    email_element = page.find_element('email')
    page.send_keys(email_element, 'Sean@gmail.com')

    phone_element = page.find_element('phone')
    page.send_keys(phone_element, '0547700823')

    message_element = page.find_element('message')
    page.send_keys(message_element, 'Nothing can stop me, Im all the way up')

    submit_element = page.find_element('submit')
    page.click(submit_element)

    error_message_element = page.find_element('error_message')
    error_message_text = page.read_text(error_message_element)

    assert error_message_text == expected_value


def test_contact_no_email(setup):
    page = ROICalculatorPage(setup)

    setup.get("https://www.entrio.io/contact")
    expected_value = 'Please complete all required fields.'

    accept_cookie = page.find_element('accept_cookie')
    page.click(accept_cookie)
    time.sleep(3)

    # iframe switch to find the important elements
    page.switch_to_correct_frame('info_frame')

    first_name_element = page.find_element('first_name')
    page.send_keys(first_name_element, 'Sean')

    last_name_element = page.find_element('last_name')
    page.send_keys(last_name_element, 'Peer')

    phone_element = page.find_element('phone')
    page.send_keys(phone_element, '547700823')

    message_element = page.find_element('message')
    page.send_keys(message_element, 'Nothing can stop me, Im all the way up')

    submit_element = page.find_element('submit')
    page.click(submit_element)

    error_message_element = page.find_element('error_message')
    error_message_text = page.read_text(error_message_element)

    assert error_message_text == expected_value


def test_contact_invalid_email(setup):
    page = ROICalculatorPage(setup)

    setup.get("https://www.entrio.io/contact")
    expected_value = 'Email must be formatted correctly.'

    accept_cookie = page.find_element('accept_cookie')
    page.click(accept_cookie)
    time.sleep(3)

    # iframe switch to find the important elements
    page.switch_to_correct_frame('info_frame')

    last_name_element = page.find_element('last_name')
    page.send_keys(last_name_element, 'Peer')

    email_element = page.find_element('email')
    page.send_keys(email_element, 'Sean@gmail')

    phone_element = page.find_element('phone')
    page.send_keys(phone_element, '547700823')

    message_element = page.find_element('message')
    page.send_keys(message_element, 'Nothing can stop me, Im all the way up')

    submit_element = page.find_element('submit')
    page.click(submit_element)

    error_message_element = page.find_element('email_error')
    error_message_text = page.read_text(error_message_element)

    assert error_message_text == expected_value

# do the dame on ROI
