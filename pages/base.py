from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestPage:

    def __init__(self, url):
        """
        初始化方法
        """
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get(url)
    
    def driver_quit(self):
        self.driver.quit()