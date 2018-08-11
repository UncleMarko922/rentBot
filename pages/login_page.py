from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    USER_FIELD = (By.ID,'email')
    PASS_FIELD = (By.ID, 'password')
    SUBMIT_BTN = (By.ID, 'submit-button')

    def __init__(self, driver):
        super().__init__(driver)
        self.PAGE_URL = f'https://themarkapts.residentportal.com/resident_portal/?module=authentication&action=view_login'
        self.go_to()
        self.get_clickable_element(self.USER_FIELD)
    
    
    
    def login(self, user_name, password):
        user = self.driver.find_element(*self.USER_FIELD)
        user.send_keys(user_name)
        pwd = self.driver.find_element(*self.PASS_FIELD)
        pwd.send_keys(password)
        submit = self.driver.find_element(*self.SUBMIT_BTN)
        submit.click()

