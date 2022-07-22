import unittest
import time
import page
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


HOME_LINK = 'https://jupiter.cloud.planittesting.com/#/'
SHOP_LINK = 'https://jupiter.cloud.planittesting.com/#/shop'
CONTACT_LINK = 'https://jupiter.cloud.planittesting.com/#/contact'
CART_LINK = 'https://jupiter.cloud.planittesting.com/#/cart'
CHECKOUT_LINK = 'https://jupiter.cloud.planittesting.com/#/checkout'


class JupiterToys (unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()))
        self.driver.get(HOME_LINK)
        self.driver.implicitly_wait(2)
        self.driver.maximize_window()

    # def test_001_Navigate_Shop_Page(self):
    #     homePage = page.HomePage(self.driver)
    #     homePage.click_shopping_button()
    #     assert self.driver.current_url == SHOP_LINK

    # def test_002_Buy_Shop_Page(self):
    #     self.driver.get(SHOP_LINK)
    #     shopPage = page.ShopPage(self.driver)
    #     shopPage.click_buy_button()
    #     cart_count = int(shopPage.check_cart().text)
    #     assert (cart_count > 0)

    # def test_003_Click_Login_Link(self):
    #     homePage = page.HomePage(self.driver)
    #     homePage.click_login_button()
    #     login_modal = homePage.check_login_modal()
    #     assert login_modal.is_displayed()

    # def test_004_Navigate_Cart_Page(self):
    #     self.driver.get(SHOP_LINK)
    #     shopPage = page.ShopPage(self.driver)
    #     shopPage.click_cart_button()
    #     assert self.driver.current_url == CART_LINK

    # def test_005_Edit_Item_Cart_Page(self):
    #     self.driver.get(SHOP_LINK)
    #     shopPage = page.ShopPage(self.driver)
    #     shopPage.click_buy_button()
    #     shopPage.click_cart_button()
    #     cartPage = page.CartPage(self.driver)
    #     cartPage.edit_cart()
    #     cart_count = int(cartPage.check_cart().text)
    #     assert (cart_count == 2)
        
    
    def test_006_Empty_Cart(self):
        self.driver.get(SHOP_LINK)
        shopPage = page.ShopPage(self.driver)
        shopPage.click_buy_button()
        shopPage.click_cart_button()
        cartPage = page.CartPage(self.driver)
        cartPage.click_empty_cart()
        cartPage.confirm_empty_cart()
        cart_shopping_button = cartPage.check_cart_empty()
        assert(cart_shopping_button.is_displayed())


    def test_009_Navigate_Contact_Page(self):
        homePage = page.HomePage(self.driver)
        homePage.click_contact_button()
        assert self.driver.current_url == CONTACT_LINK

    def tearDown(self):
        time.sleep(2)
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
