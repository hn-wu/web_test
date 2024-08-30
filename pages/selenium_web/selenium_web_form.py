from pages.base import TestPage
from selenium.webdriver.common.by import By

class Page(TestPage):

    def __init__(self):
        """
        初始化方法
        """
        url = "https://www.selenium.dev/selenium/web/web-form.html"
        super().__init__(url)
        text_box_locator = (By.NAME, "my-text")
        self.text_box = self.element_wait(text_box_locator)
        submit_button_locator = (By.CSS_SELECTOR, "button")
        self.submit_button = self.element_wait(submit_button_locator)
    
    def text_box_send_keys(self, text):
        self.text_box.send_keys(text)
    
    def submit_button_click(self):
        self.submit_button.click()