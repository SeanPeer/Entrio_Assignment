from selenium.webdriver.common.by import By

from utils.base_page import BasePage


class ResourceCenterPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.elements = {
            "accept_cookie": [By.XPATH, "/html/body/div[2]/div/div/div/div[2]/button[2]"],
            "how_entrio_can_enrich": [By.XPATH,"""//*[@id="w-node-_4b95ebbe-73f3-97a7-2f1a-1003b5010c57-d53a0e38"]/a/div[1]"""],
            "contact_info_page":[By.XPATH, """//*[@id="w-node-b328a6bd-8303-3fd7-b4e0-85c6377fe2a4-331da5ef"]/h1"""],
            "first_name": [By.XPATH, """//*[@id="hsForm_7e88bdc6-7a1c-4473-8759-7dd477e6c5ba"]/div[1]"""],
            "last_name": [By.XPATH, """//div[@id='hbspt-form-7d8625b1-e887-46dc-94af-6dfdd97b57c4']/form/div[2]/div"""],
            "company_name": [By.XPATH, """//*[@id="company-7e88bdc6-7a1c-4473-8759-7dd477e6c5ba"]"""],
            "email": [By.XPATH, """//*[@id="email-7e88bdc6-7a1c-4473-8759-7dd477e6c5ba"]"""],
            "video1_link": [By.XPATH,"""//*[@id="w-node-_28a3d23f-4dec-0bce-fad7-309696b4b5a4-96b4b5a4"]"""],
            "video1_frame": [By.XPATH, """/html/body/section[2]/div[1]/div/iframe"""],
            "blog_link":   [By.XPATH, """//div[@class="w-layout-blockcontainer collection-list w-container"]/div[4]/a"""],
            "blog_sample":   [By.XPATH, """//*[@id="w-node-f910326f-11e9-7bcb-94cb-a137edb2b9bf-7d038123"]/p[3]"""],
            "video2_link": [By.XPATH, """//*[@id="w-node-_5b386345-acd1-58a3-e99e-452279f26064-d53a0e38"]"""],
            "video2_frame": [By.XPATH, """/html/body/section[2]/div[1]/div/iframe"""],
            "first_blog":   [By.XPATH, """/html/body/section[2]/div/div[3]/div/div[1]/a"""],
            "second_blog": [By.XPATH, """/html/body/section[2]/div/div[3]/div/div[2]/a"""],
            "third_blog": [By.XPATH, """/html/body/section[2]/div/div[3]/div/div[3]/a"""],
            "view_all": [By.XPATH, """/html/body/section[2]/div/div[2]/div/a"""],
            "title": [By.XPATH, """//*[@id="w-node-a44f357e-25e5-d255-ca73-81fbea97bffe-7d038123"]/h1"""],

        }
