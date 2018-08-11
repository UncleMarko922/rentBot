from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.PAGE_URL = None

    def go_to(self):
        self.driver.get(self.PAGE_URL)

    def get_clickable_element(self, *selector):
        """
        Method will obtain a clickable element once the page
         is loaded and element becomes available.
        """
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((*selector)))

    def click_with_js(self, locator):
        self.driver.execute_script("arguments[0].click();", locator)
        

