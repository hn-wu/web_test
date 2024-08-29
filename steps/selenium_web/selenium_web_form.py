from pages.selenium_web.selenium_web_form import Page
from steps.base import TestStep

class Step(TestStep):

    selenium_web_form = Page()

    def text_box_send_keys(self, config):
        text = config.get("text")
        self.selenium_web_form.text_box_send_keys(text)
    
    def submit_button_click(self):
        self.selenium_web_form.submit_button_click()

if __name__ == "__main__":
    step = Step()
    step.text_box_send_keys({'text':'bgb'})
    step.selenium_web_form.driver_quit()
    