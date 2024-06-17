from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException, \
    ElementNotVisibleException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def safe_click(element):
    try:
        WebDriverWait(element, 10).until(EC.element_to_be_clickable(element))
        element.click()
    except (NoSuchElementException, TimeoutException) as e:
        print(f"Error clicking element: {e}")


def safe_read(element):
    try:
        WebDriverWait(element, 10).until(EC.visibility_of(element))
        return element.text
    except (NoSuchElementException, TimeoutException) as e:
        print(f"Error reading element: {e}")
        return None


def safe_find_element(driver, by, value, wait_for_visibility=True, timeout=15):
    try:
        if wait_for_visibility:
            element = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((by, value)))
        else:
            element = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))
        return element
    except (NoSuchElementException, TimeoutException, ElementNotVisibleException) as e:
        print(f"Error finding element by {by} with value {value}: {e}")
        return None



def safe_send_keys(element, keys):
    try:
        WebDriverWait(element, 10).until(EC.visibility_of(element))
        element.clear()
        element.send_keys(keys)
        return True
    except (NoSuchElementException, TimeoutException, ElementNotInteractableException) as e:
        print(f"Error sending keys to element: {e}")
        return False