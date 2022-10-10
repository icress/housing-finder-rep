from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class Drive:

    def __init__(self):

        self.DRIVER_LOCATION = "insert/driver/location"
        self.URL = "insert url for Google form"

        self.service = Service(executable_path=self.DRIVER_LOCATION)
        self.driver = webdriver.Chrome(service=self.service)

    def post_info(self, address, price, link):

        self.driver.get(self.URL)

        answer_boxes = self.driver.find_elements(By.CSS_SELECTOR, value=".whsOnd")

        address_answer = answer_boxes[0]
        price_answer = answer_boxes[1]
        link_answer = answer_boxes[2]

        address_answer.send_keys(address)
        price_answer.send_keys(price)
        link_answer.send_keys(link)

        submit = self.driver.find_element(By.CSS_SELECTOR, value=".uArJ5e")
        submit.click()
