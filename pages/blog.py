from selenium.webdriver.common.by import By

from utils.base_page import BasePage


class BlogPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.elements = {
            "accept_cookie": [By.XPATH, "/html/body/div[2]/div/div/div/div[2]/button[2]"],
            "title": [By.XPATH, """//*[@id="w-node-a44f357e-25e5-d255-ca73-81fbea97bffe-7d038123"]/h1"""],
            'common_data_article': [By.XPATH, "/html/body/section[2]/div/div/div/div[1]/a"],
            "how_to_approach": [By.XPATH, "/html/body/section[2]/div/div/div/div[2]/a"],
            "implement_an_LLm": [By.XPATH, "/html/body/section[2]/div/div/div/div[3]/a"],
            "taxonomy": [By.XPATH, "/html/body/section[2]/div/div/div/div[4]/a"],
            "navigating": [By.XPATH, "/html/body/section[2]/div/div/div/div[5]/a"],
            "banking": [By.XPATH, "/html/body/section[2]/div/div/div/div[6]/a"],
            "intro": [By.XPATH, "/html/body/section[2]/div/div/div/div[7]/a"],
            "products": [By.XPATH, "/html/body/section[2]/div/div/div/div[8]/a"],
            "unleash": [By.XPATH, "/html/body/section[2]/div/div/div/div[9]/a"],

        }

