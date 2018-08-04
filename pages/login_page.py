from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.PAGE_URL = f'https://themarkapts.residentportal.com/resident_portal/?module=authentication&action=view_login'
        self.go_to()
        self.locators = {'user_field': driver.find_element_by_id('email'),
                         'pass_field': driver.find_element_by_id('password'), 
                         'submit_btn': driver.find_element_by_id('submit-button')}
        # self.user_txt = driver
        # self.user_pass = 
        # self.login = driver.find_element_by_id('submit-button')
    
    def login(self, user_name, password):
        self.locators['user_field'].send_keys(user_name)
        self.locators['pass_field'].send_keys(password)
        self.locators['submit_btn'].click()