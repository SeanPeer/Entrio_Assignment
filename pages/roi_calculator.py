from utils.base_page import BasePage
from selenium.webdriver.common.by import By


class ROICalculatorPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.elements = {
            "accept_cookie": [By.XPATH, "/html/body/div[2]/div/div/div/div[2]/button[2]"],
            "global": [By.ID, "global"],
            "regional": [By.ID, "regional"],
            "local": [By.ID, "local"],
            "number_of_employees": [By.XPATH, "/html/body/tf-root/div/tf-roi-calculator/div/div/div[1]/div/form/div[1]/div[1]/input"],
            "estimated_savings": [By.XPATH, "//div[@class='roi-result']/div[1]/div"],
            "annual_cost_avoidance": [By.XPATH, "//div[@class='roi-result']/div[2]/div"],
            "to_scroll":    [By.XPATH, "/html/body/section[2]/div"],
            "start_saving_button":  [By.XPATH, """/html/body/tf-root/div/tf-roi-calculator/div/div/div[2]/div[3]/a"""],
            "contact_page_text":    [By.XPATH, """//*[@id="w-node-b328a6bd-8303-3fd7-b4e0-85c6377fe2a4-c13b6c9b"]/h1"""]
        }
