from utils.base_page import BasePage
from selenium.webdriver.common.by import By


class ROICalculatorPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.elements = {
            "accept_cookie": [By.XPATH, "/html/body/div[2]/div/div/div/div[2]/button[2]"],
            'roi_frame': [By.XPATH, """/html/body/section[2]/div/iframe"""],
            "global": [By.XPATH, "/html/body/tf-root/div/tf-roi-calculator/div/div/div[1]/div/form/div[2]/div[2]/label[1]"],
            "regional": [By.XPATH, "/html/body/tf-root/div/tf-roi-calculator/div/div/div[1]/div/form/div[2]/div[2]/label[2]"],
            "local": [By.XPATH, "/html/body/tf-root/div/tf-roi-calculator/div/div/div[1]/div/form/div[2]/div[2]/label[3]"],
            "number_of_employees": [By.XPATH, "/html/body/tf-root/div/tf-roi-calculator/div/div/div[1]/div/form/div[1]/div[1]/input"],
            "estimated_savings": [By.XPATH, """/html/body/tf-root/div/tf-roi-calculator/div/div/div[2]/div[1]/div"""],
            "annual_cost_avoidance": [By.XPATH, """/html/body/tf-root/div/tf-roi-calculator/div/div/div[2]/div[2]/div"""],
            "to_scroll":    [By.XPATH, "/html/body/section[2]/div"],
            "start_saving_button":  [By.XPATH, """/html/body/tf-root/div/tf-roi-calculator/div/div/div[2]/div[3]/a"""],
            "contact_page_text":    [By.XPATH, """//*[@id="w-node-b328a6bd-8303-3fd7-b4e0-85c6377fe2a4-c13b6c9b"]/h1"""],
            "info_frame":   [By.XPATH, """//iframe[@id='hs-form-iframe-0']"""],
            'first_name':   [By.XPATH,"""//input[@id='firstname-74dcff1c-1b32-47b7-9130-93f5fda4f58e']"""],
            'last_name':    [By.XPATH,"""//input[@id='lastname-74dcff1c-1b32-47b7-9130-93f5fda4f58e']"""],
            'email': [By.XPATH, """//input[@id='email-74dcff1c-1b32-47b7-9130-93f5fda4f58e']"""],
            'phone': [By.XPATH, """//input[@id='phone-74dcff1c-1b32-47b7-9130-93f5fda4f58e']"""],
            'message': [By.XPATH, """//textarea[@id='message-74dcff1c-1b32-47b7-9130-93f5fda4f58e']"""],
            'submit': [By.XPATH, """//input[@value='Submit']"""],
            'error_message':    [By.CSS_SELECTOR, """label[class='hs-main-font-element']"""],
            'email_error':  [By.XPATH, """//label[normalize-space()='Email must be formatted correctly.']"""]

        }

