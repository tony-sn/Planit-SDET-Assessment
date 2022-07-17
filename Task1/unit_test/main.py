import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import page

HOME_LINK = 'https://jupiter.cloud.planittesting.com/#/'
SHOP_LINK = 'https://jupiter.cloud.planittesting.com/#/shop'
CONTACT_LINK = 'https://jupiter.cloud.planittesting.com/#/contact'
CART_LINK = 'https://jupiter.cloud.planittesting.com/#/cart'
CHECKOUT_LINK = 'https://jupiter.cloud.planittesting.com/#/checkout'


class JupiterToys (unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service('./chromedriver'))
        self.driver.get(HOME_LINK)

    def test_case_001(self):
        homePage = page.HomePage(self.driver)
        homePage.click_shopping_button()
        assert self.driver.current_url == SHOP_LINK

    def test_case_002(self):
        shopPage = page.ShopPage(self.driver.get(SHOP_LINK))
        time.sleep(5)
        shopPage.click_buy_button()
        shopPage.check_cart()

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
