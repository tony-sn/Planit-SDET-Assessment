# Test case: 006_Empty_Cart

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

SHOP_LINK = 'https://jupiter.cloud.planittesting.com/#/shop'

driver = webdriver.Chrome(service=Service('./chromedriver'))
# Start at Shop page
driver.get(SHOP_LINK)

driver.implicitly_wait(3)

products = driver.find_element(By.CLASS_NAME, 'products')
stuff_frog = products.find_element(By.ID, 'product-2')
buy_button = stuff_frog.find_element(By.CLASS_NAME, 'btn-success')
buy_button.click()

cart = driver.find_element(By.ID, 'nav-cart')
cart.click()

empty_cart_button = driver.find_element(By.CLASS_NAME, 'btn-danger')
empty_cart_button.click()

# when modal appears, click Yes option
modal_footer = driver.find_element(By.CLASS_NAME, 'modal-footer')
time.sleep(1)
yes_option = modal_footer.find_element(By.CLASS_NAME, 'btn-success')
yes_option.click()

cart_count = int(cart.find_element(By.CLASS_NAME, 'cart-count').text)

# start shopping button appears when cart is empty
start_shopping_button = driver.find_element(By.PARTIAL_LINK_TEXT, 'Shopping')
assert start_shopping_button.is_displayed()
if cart_count == 0:
    print('TC_006: PASS')
else:
    print('TC_006: FAIL')

time.sleep(2)
driver.quit()