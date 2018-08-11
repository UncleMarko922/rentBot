from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class Dashboard(BasePage):
    PAY_AMOUNT = (By.CLASS_NAME, 'pay-amount')
    PAYMENT = (By.CLASS_NAME, 'payment')


    def __init__(self, driver):
        super().__init__(driver)
        self.get_clickable_element(self.PAY_AMOUNT)

    
    def click_pay_btn(self):
        """
        click button to submit payment
        """
        pay_btn = self.driver.find_element(*self.PAYMENT)
        pay_btn.click()
    
    def get_outstanding_amount(self):
        """
        grab the value of the total rent amount from the element
        :return: String outstanding rent amount
        """
        amount = self.driver.find_element(*self.PAY_AMOUNT)
        return amount.text
