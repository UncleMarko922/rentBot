from pages.base_page import BasePage

class Dashboard(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.locators = {
        'amount': driver.find_element_by_class_name('pay-amount'),
        'pay': driver.find_element_by_class_name('payment')
        }

    
    def click_pay_btn(self):
        """
        click button to submit payment
        """
        self.locators['pay'].click()
    
    def get_outstanding_amount(self):
        """
        grab the value of the total rent amount from the element
        :return: String outstanding rent amount
        """
        return self.locators['amount'].text