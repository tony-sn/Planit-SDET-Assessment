# Test case: 002_Buy_Shop_Page

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

SHOP_LINK = 'https://jupiter.cloud.planittesting.com/#/shop'

driver = webdriver.Chrome(service=Service('./chromedriver'))
# Start at Shop page
driver.get(SHOP_LINK)

try:
    products = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'products'))
    )
# locate buy button
    teddy_bear = products.find_element(By.ID, 'product-1')
    buy_button = teddy_bear.find_element(By.CLASS_NAME, 'btn-success')
    buy_button.click()
# locate cart element
    cart = driver.find_element(By.ID, 'nav-cart')
    cart_count = int(cart.find_element(By.CLASS_NAME, 'cart-count').text)

# cart is not empty
    if (cart_count > 0):
        print('TC_002: PASS')
    else:
        print('TC_002: FAIL')
finally:
    time.sleep(2)
    driver.quit()
