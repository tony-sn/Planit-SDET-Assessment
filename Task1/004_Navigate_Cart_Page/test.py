# Test case: 004_Navigate_Cart_Page

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

HOME_LINK = 'https://jupiter.cloud.planittesting.com/#/'
CART_LINK = 'https://jupiter.cloud.planittesting.com/#/cart'

driver = webdriver.Chrome(service=Service('./chromedriver'))
driver.get(HOME_LINK)

# Locate Cart link
cart = driver.find_element(By.ID, 'nav-cart')
# Navigate to Cart page
cart.click()

if (driver.current_url == CART_LINK):
    print('TC_004: PASS')
else:
    print('TC_004: FAIL')

time.sleep(2)
driver.quit()