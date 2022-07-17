# Test case: 008_Form_Checkout_Page

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

SHOP_LINK = 'https://jupiter.cloud.planittesting.com/#/shop'

driver = webdriver.Chrome(service=Service('./chromedriver'))
driver.get(SHOP_LINK)

driver.implicitly_wait(3)
actions = ActionChains(driver)

# Need a product to navigate to Checkout page
products = driver.find_element(By.CLASS_NAME, 'products')
stuff_frog = products.find_element(By.ID, 'product-2')
buy_button = stuff_frog.find_element(By.CLASS_NAME, 'btn-success')
buy_button.click()

# Navigate to Cart page
cart = driver.find_element(By.ID, 'nav-cart')
cart.click()

checkout_button = driver.find_element(By.CLASS_NAME, 'btn-checkout')
checkout_button.click()

# Form fill part
form = driver.find_element(By.NAME, 'form')

# Form required fields
forename = driver.find_element(By.ID, 'forename')
email = driver.find_element(By.ID, 'email')
address = driver.find_element(By.ID, 'address')
card_type = Select(driver.find_element(By.ID, 'cardType'))
visa_option = card_type.select_by_value('Visa')
card = driver.find_element(By.ID, 'card')

submit_button = driver.find_element(By.ID, 'checkout-submit-btn')

# Filling form
try:
    actions.send_keys_to_element(forename, 'John')
    actions.send_keys_to_element(email, 'john@gmail.com')
    actions.send_keys_to_element(address, '2/13 Joy St')
    actions.click(visa_option)
    actions.send_keys_to_element(card, '1234 5678 9988')
    actions.click(submit_button)
    actions.perform()

    shop_again_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Shopping Again')))
    

finally:
    if shop_again_button.is_displayed():
        print('TC_008: PASS')
    else:
        print('TC_008: FAIL')

time.sleep(2)
driver.quit()
