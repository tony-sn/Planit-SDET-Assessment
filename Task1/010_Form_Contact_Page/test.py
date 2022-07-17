# Test case: 010_Form_Contact_Page

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

CONTACT = 'https://jupiter.cloud.planittesting.com/#/contact'

driver = webdriver.Chrome(service=Service('./chromedriver'))
driver.get(CONTACT)
actions = ActionChains(driver)

forename = driver.find_element(By.ID, 'forename')
email = driver.find_element(By.ID, 'email')
message = driver.find_element(By.ID, 'message')

submit_button = driver.find_element(By.XPATH, "//a[text()='Submit']")

try:
    actions.send_keys_to_element(forename, 'John')
    actions.send_keys_to_element(email, 'john@gmail.com')
    actions.send_keys_to_element(message, 'This is a message to Jupiter Toys')
    actions.click(submit_button)
    actions.perform()

    alert_success = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'alert-success')))
    if alert_success.is_displayed():
        print('TC_010: PASS')
    else:
        print('TC_010: FAIL')
finally:
    time.sleep(2)
    driver.quit()
