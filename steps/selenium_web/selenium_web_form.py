import allure
from pages.selenium_web.selenium_web_form import Page
from steps.base import TestStep
class Step(TestStep):

    selenium_web_form = Page()

    @allure.step("设置keys值")
    def text_box_send_keys(self, config):
        text = config.get("text")
        self.selenium_web_form.text_box_send_keys(text)
    
    @allure.step("点击按钮")
    def submit_button_click(self):
        self.selenium_web_form.submit_button_click()
    
    @allure.step("关闭页面")
    def driver_quit(self):
        self.selenium_web_form.driver_quit()

if __name__ == "__main__":
    step = Step()
    step.text_box_send_keys({'text':'bgb'})
    step.selenium_web_form.driver_quit()
    