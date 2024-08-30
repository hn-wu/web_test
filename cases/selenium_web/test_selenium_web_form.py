import pytest
import logging
from cases.base import TestCase
from steps.selenium_web.step import Step as SeleniumStep

class TestSeleniumWebForm(TestCase):

    selenium_step = SeleniumStep()

    def setup_class(self):
        logging.info("前置条件")

    def teardown_class(self):
        logging.info("后置条件")
        self.selenium_step.selenium_web_form.driver_quit()

    def test_login(self):
        self.selenium_step.selenium_web_form.text_box_send_keys({'text':'bgb'})