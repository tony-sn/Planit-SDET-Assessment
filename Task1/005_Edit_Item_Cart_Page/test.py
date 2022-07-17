# Test case: 005_Edit_Item_Cart_Page

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

SHOP_LINK = 'https://jupiter.cloud.planittesting.com/#/shop'

driver = webdriver.Chrome(service=Service('./chromedriver'))
# Start at Shop page
driver.get(SHOP_LINK)

# Wait for loading products
driver.implicitly_wait(3)
actions = ActionChains(driver)

products = driver.find_element(By.CLASS_NAME, 'products')
teddy_bear = products.find_element(By.ID, 'product-1')
buy_button = teddy_bear.find_element(By.CLASS_NAME, 'btn-success')
buy_button.click()

cart = driver.find_element(By.ID, 'nav-cart')
cart.click()

quantity = driver.find_element(By.CLASS_NAME, 'input-mini')
# action chains to update quantity
actions.click(quantity)
actions.send_keys(Keys.BACK_SPACE)
time.sleep(1)
actions.send_keys('2')
actions.send_keys(Keys.ENTER)
actions.perform()

cart_count = int(cart.find_element(By.CLASS_NAME, 'cart-count').text)

if cart_count == 2:
    print('TC_005: PASS')
else:
    print('TC_005: FAIL')


time.sleep(3)
driver.quit()
