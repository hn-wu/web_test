from pages.base import TestPage
from selenium.webdriver.common.by import By

class Page(TestPage):

    def __init__(self):
        """
        初始化方法
        """
        url = "https://www.selenium.dev/selenium/web/web-form.html"
        super().__init__(url)
        self.text_box = self.driver.find_element(by=By.NAME, value="my-text")
        self.submit_button = self.driver.find_element(by=By.CSS_SELECTOR, value="button")
    
    def text_box_send_keys(self, text):
        self.text_box.send_keys(text)
    
    def submit_button_click(self):
        self.submit_button.click()