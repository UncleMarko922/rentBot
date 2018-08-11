from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time

class PaymentPage(BasePage):
    PAY_TEXTBOX = (By.ID, 'pay-amount')
    CLICK_OFF_PAY = (By.CLASS_NAME, 'pay-steps')
    PAY_METHOD = (By.ID,'1119452')
    AGREE_RADIO = (By.ID, 'agree-terms')
    SUBMIT_PAYMENT = (By.ID, 'submitPayment')

    def __init__(self, driver):
        super().__init__(driver)
        self.get_clickable_element(self.PAY_TEXTBOX)

    

    def make_payment(self, amount):
        pay = self.driver.find_element(*self.PAY_TEXTBOX)
        pay.send_keys(amount)
        off_pay = self.driver.find_element(*self.CLICK_OFF_PAY)
        off_pay.click()
        method_of_payment = self.get_clickable_element(self.PAY_METHOD)
        method_of_payment.click()
        agree_radio_btn = self.driver.find_element(*self.AGREE_RADIO)
        self.click_with_js(agree_radio_btn)
        time.sleep(1)
        submit_payment_btn = self.driver.find_element(*self.SUBMIT_PAYMENT)
        self.click_with_js(submit_payment_btn)


        
         
