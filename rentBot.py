import os
import time
from os import environ
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
chrome_driver = os.path.join('drivers', 'chromedriver.exe')
driver = webdriver.Chrome(chrome_driver)


def pay_rent(driver):
    wait = WebDriverWait(driver, 10)
    
    url = f'https://themarkapts.residentportal.com/resident_portal/?module=authentication&action=view_login'
    driver.get(url)
    user = os.environ['rentUser']
    pwd = os.environ['rentPass']

    user_txt = driver.find_element_by_id('email')
    user_pass = driver.find_element_by_id('password')
    login = driver.find_element_by_id('submit-button')
        

    user_txt.send_keys(user)
    user_pass.send_keys(pwd)

    login.click()
    driver.implicitly_wait(3)
    amount = driver.find_element_by_class_name('pay-amount').text

    
    pay = driver.find_element_by_class_name('payment')

    pay.click()
    print(amount)
    amount = '.01'

    pay_txt_box = driver.find_element_by_id('pay-amount')

    pay_txt_box.send_keys(amount)
    click_elem = driver.find_element_by_class_name('pay-steps')
    click_elem.click()

    
    payment_method = wait.until(EC.element_to_be_clickable((By.ID, '1119452')))
    payment_method.click()

    agree_radio = driver.find_element_by_id('agree-terms')
    driver.execute_script("arguments[0].click();", agree_radio)

    submit_payment = driver.find_element_by_id('submitPayment')
    time.sleep(1)
    driver.execute_script("arguments[0].click();", submit_payment)

pay_rent(driver)