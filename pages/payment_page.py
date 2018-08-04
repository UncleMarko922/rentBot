from pages.base_page import BasePage
import time

class PaymentPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.locators = {
            'pay_txt_box': driver.find_element_by_id('pay-amount'),
            'click_pay': driver.find_element_by_class_name('pay-steps')
        }

    def update_locators(self):
        self.locators['payment_method'] = self.wait_for_id('1119452')
        self.locators['agree_radio'] = self.driver.find_element_by_id('agree-terms')
        self.locators['submit_payment'] = self.driver.find_element_by_id('submitPayment')

    def make_payment(self, amount):
        self.locators['pay_txt_box'].send_keys(amount)
        self.locators['click_pay'].click()
        self.update_locators()
        self.locators['payment_method'].click()
        self.click_with_js(self.locators['agree_radio'])
        time.sleep(1)
        self.click_with_js(self.locators['submit_payment'])


        
         
