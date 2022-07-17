# Test case: 003_Click_Login_Link

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

HOME_LINK = 'https://jupiter.cloud.planittesting.com/#/'

driver = webdriver.Chrome(service=Service('./chromedriver'))
driver.get(HOME_LINK)

# Locate login link
login_link = driver.find_element(By.ID, 'nav-login')
login_link.click()

# Check whether login popup modal is present
popup_modal = driver.find_element(By.CLASS_NAME, 'modal')

if popup_modal.is_displayed():
    print('TC_003: PASS')
else:
    print('TC_003: FAIL')

time.sleep(2)
driver.quit()
