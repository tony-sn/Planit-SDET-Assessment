# Test case: 009_Navigate_Contact_Page

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

HOME = 'https://jupiter.cloud.planittesting.com/#/'
CONTACT = 'https://jupiter.cloud.planittesting.com/#/contact'

driver = webdriver.Chrome(service=Service('./chromedriver'))
driver.get(HOME)

# Locate Contact link
contact_link = driver.find_element(By.XPATH, "//a[text()='Contact']")
# Navigate to Contact page
contact_link.click()

if (driver.current_url == CONTACT):
    print('TC_009: PASS')
else:
    print('TC_009: FAIL')

time.sleep(2)
driver.quit()