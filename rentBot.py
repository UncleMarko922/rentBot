import os
import time
from os import environ

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.dashboard import Dashboard
from pages.payment_page import PaymentPage
chrome_driver = os.path.join('drivers', 'chromedriver.exe')
driver = webdriver.Chrome(chrome_driver)

driver.implicitly_wait(3)

def pay_rent(driver):

    login_page = LoginPage(driver)
    login_page.login(os.environ['rentUser'],os.environ['rentPass'])

    dashboard_page = Dashboard(driver)
    amount = dashboard_page.get_outstanding_amount()
    dashboard_page.click_pay_btn()
    
    
    print(amount)
    amount = '.01'

    payment_page = PaymentPage(driver)
    payment_page.make_payment(amount)
    

pay_rent(driver)