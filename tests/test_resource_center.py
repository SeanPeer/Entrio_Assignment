import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from pages.resource_center_page import ResourceCenterPage
from utils.helpers import safe_click, safe_read, safe_send_keys


@pytest.fixture
def setup():
    options = Options()
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument("start-maximized")
    options.add_argument("--disable-extensions")
    path = Service('C:/Users/seanp/Desktop/Self Improvement/chromedriver-win64/chromedriver-win64/chromedriver.exe')
    driver = webdriver.Chrome(service=path, options=options)
    driver.get("http://www.entrio.io/resource-center")
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def test_contact_resource(setup):
    page = ResourceCenterPage(setup)
    expected_text = 'How Entrio Can Enrich Your IT Catalog'

    accept_cookie = page.find_element('accept_cookie')
    safe_click(accept_cookie)

    ebook_element = page.find_element('how_entrio_can_enrich')
    safe_click(ebook_element)

    title_element = page.find_element('contact_info_page')
    actual_text = safe_read(title_element)

    assert actual_text == expected_text


def test_refresh(setup):
    page = ResourceCenterPage(setup)
    expected_text = 'How Entrio Can Enrich Your IT Catalog'

    accept_cookie = page.find_element('accept_cookie')
    safe_click(accept_cookie)

    ebook_element = page.find_element('how_entrio_can_enrich')
    safe_click(ebook_element)

    setup.refresh()

    title_element = page.find_element('contact_info_page')
    actual_text = safe_read(title_element)

    assert actual_text == expected_text


def test_video1_visibility(setup):
    page = ResourceCenterPage(setup)
    flag = False

    accept_cookie = page.find_element('accept_cookie')
    safe_click(accept_cookie)

    video_link_element = page.find_element('video1_link')
    safe_click(video_link_element)

    video_element = page.find_element('video1_frame')
    if video_element:
        flag = True

    assert flag


def test_video2_visibility(setup):
    page = ResourceCenterPage(setup)
    flag = False

    accept_cookie = page.find_element('accept_cookie')
    safe_click(accept_cookie)

    video_link_element = page.find_element('video2_link')
    safe_click(video_link_element)

    video_element = page.find_element('video2_frame')
    if video_element:
        flag = True

    assert flag


def test_blog_accessibility(setup):
    page = ResourceCenterPage(setup)
    expected_text = 'It’s been “tech up or tap out.”'

    accept_cookie = page.find_element('accept_cookie')
    safe_click(accept_cookie)

    blog_link_element = page.find_element('blog_link')
    safe_click(blog_link_element)

    blog_text_element = page.find_element('blog_sample')
    actual_text = safe_read(blog_text_element)

    assert expected_text == actual_text


def test_resource_blog(setup):
    page = ResourceCenterPage(setup)
    expected_url1 = 'https://www.entrio.io/blog/8-common-data-issues-preventing-tech-visibility'
    expected_url2 = 'https://www.entrio.io/blog/approach-execute-vendor-consolidations'
    expected_url3 = 'https://www.entrio.io/blog/implementing-llm-agnostic-architecture-generative-ai-module'
    flag = False

    accept_cookie = page.find_element('accept_cookie')
    safe_click(accept_cookie)

    first_blog_element = page.find_element('first_blog')
    safe_click(first_blog_element)
    time.sleep(3)
    actual_url1 = setup.current_url
    setup.back()

    second_blog_element = page.find_element('second_blog')
    safe_click(second_blog_element)
    time.sleep(3)
    actual_url2 = setup.current_url
    setup.back()

    third_blog_element = page.find_element('third_blog')
    safe_click(third_blog_element)
    time.sleep(3)
    actual_url3 = setup.current_url

    if actual_url1 == expected_url1 and actual_url2 == expected_url2 and expected_url3 == actual_url3:
        flag = True

    assert flag


def test_view_all(setup):
    page = ResourceCenterPage(setup)
    expected_url = "https://www.entrio.io/blog"
    view_element = page.find_element('view_all')
    safe_click(view_element)

    actual_url = setup.current_url

    assert actual_url == expected_url

