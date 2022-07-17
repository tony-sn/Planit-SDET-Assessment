# Test case: 007_Navigate_Checkout_Page

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

SHOP_LINK = 'https://jupiter.cloud.planittesting.com/#/shop'
CHECKOUT_LINK = 'https://jupiter.cloud.planittesting.com/#/checkout'

driver = webdriver.Chrome(service=Service('./chromedriver'))
driver.get(SHOP_LINK)

driver.implicitly_wait(3)

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

if (driver.current_url == CHECKOUT_LINK):
    print('TC_007: PASS')
else:
    print('TC_007: FAIL')

time.sleep(2)
driver.quit()