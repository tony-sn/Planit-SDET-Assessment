# Test case: 001_Navigate_Shop_Page

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

HOME_LINK = 'https://jupiter.cloud.planittesting.com/#/'
SHOP_LINK = 'https://jupiter.cloud.planittesting.com/#/shop'

driver = webdriver.Chrome(service=Service('./chromedriver'))
driver.get(HOME_LINK)

# Start shopping button
start_shopping_button = driver.find_element(By.PARTIAL_LINK_TEXT, 'Shopping')
# fire click event
start_shopping_button.click()
# Result
if driver.current_url == SHOP_LINK:
    print('TC_001: PASS')
else:
    print('TC_001: FAIL')

time.sleep(2)
driver.quit()
