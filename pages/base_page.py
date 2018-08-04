from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.PAGE_URL = None

    def go_to(self):
        self.driver.get(self.PAGE_URL)

    def wait_for_id(self, id):
        """
        Method will perform a wait for 10 seconds when called and an ID is passed in.
        """
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, id)))

    def click_with_js(self, locator):
        self.driver.execute_script("arguments[0].click();", locator)
        

