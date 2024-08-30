from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestPage:

    def __init__(self, url):
        """
        初始化方法，输入的url需要为用例初始化首页，后续切换使用switch_to_tab函数
        """
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get(url)

    def element_wait(self, locator, timeout=10):
        """
        等待元素出现
        """
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def switch_to_tab(self, tab_index=-1):
        """
        切换要执行的页面，默认切换到最新的窗口
        """
        tabs = self.driver.window_handles
        if len(tabs) > tab_index:
            self.driver.switch_to.window(tabs[tab_index])

    def driver_quit(self):
        self.driver.quit()