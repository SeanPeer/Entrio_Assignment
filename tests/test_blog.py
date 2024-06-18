import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from utils.helpers import safe_click, safe_read

from pages.blog import BlogPage


@pytest.fixture
def setup():
    options = Options()
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument("start-maximized")
    options.add_argument("--disable-extensions")
    path = Service('C:/Users/seanp/Desktop/Self Improvement/chromedriver-win64/chromedriver-win64/chromedriver.exe')
    driver = webdriver.Chrome(service=path, options=options)
    driver.get("http://www.entrio.io/blog")
    time.sleep(5)
    return driver


# Clicking each article and checking if are reachable - validating its name
def test_blog_titles(setup):
    page = BlogPage(setup)
    expected_names = ['8 Common Data Issues Preventing Tech Visibility',
                      'How to Approach and Execute Vendor Consolidations',
                      'Implementing an LLM Agnostic Architecture for our Generative AI Module',
                      'Taxonomy for the Tech Stack', 'Navigating the Complexity of the Enterprise Tech Stack',
                      'Banking on Bytes: Achieving Success through Responsible Tech Adoption',
                      'Introducing Responsible Tech Adoption',
                      'Entrio’s 2023 Product Release Roundup',
                      'Entrio Unleashes the Future of Tech Adoption with Generative AI']

    actual_names = []
    accept_cookie = page.find_element('accept_cookie')
    safe_click(accept_cookie)

    for key in page.elements.keys():
        if key != 'accept_cookie' and key != 'title':
            element = page.find_element(key)
            safe_click(element)
            actual_title_element = page.find_element('title')
            actual_name = safe_read(actual_title_element)
            actual_names.append(actual_name)
            setup.back()

    assert expected_names == actual_names
