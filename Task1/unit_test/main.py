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

    def test_001_Navigate_Shop_Page(self):
        homePage = page.HomePage(self.driver)
        homePage.click_shopping_button()
        assert self.driver.current_url == SHOP_LINK

    def test_002_Buy_Shop_Page(self):
        self.driver.get(SHOP_LINK)
        shopPage = page.ShopPage(self.driver)
        shopPage.click_buy_button()
        cart_count = int(shopPage.check_cart().text)
        assert (cart_count > 0)

    def test_003_Click_Login_Link(self):
        homePage = page.HomePage(self.driver)
        homePage.click_login_button()
        assert homePage.check_login_modal().is_displayed()

    def test_004_Navigate_Cart_Page(self):
        self.driver.get(SHOP_LINK)
        shopPage = page.ShopPage(self.driver)
        shopPage.click_cart_button()
        assert self.driver.current_url == CART_LINK

    def test_005_Edit_Item_Cart_Page(self):
        self.driver.get(SHOP_LINK)
        shopPage = page.ShopPage(self.driver)
        shopPage.navigate_cart_page()
        cartPage = page.CartPage(self.driver)
        cartPage.edit_cart()
        assert (int(cartPage.check_cart().text) == 2)

    def test_006_Empty_Cart(self):
        self.driver.get(SHOP_LINK)
        shopPage = page.ShopPage(self.driver)
        shopPage.navigate_cart_page()
        cartPage = page.CartPage(self.driver)
        cartPage.confirm_empty_cart()
        assert(cartPage.check_cart_empty().is_displayed())

    def test_007_Navigate_Checkout_Page(self):
        self.driver.get(SHOP_LINK)
        shopPage = page.ShopPage(self.driver)
        shopPage.navigate_cart_page()
        cartPage = page.CartPage(self.driver)
        cartPage.click_checkout_button()
        assert(self.driver.current_url == CHECKOUT_LINK)

    def test_008_Form_Checkout_Page(self):
        self.driver.get(SHOP_LINK)
        shopPage = page.ShopPage(self.driver)
        shopPage.navigate_cart_page()
        cartPage = page.CartPage(self.driver)
        cartPage.click_checkout_button()
        checkoutPage = page.CheckoutPage(self.driver)
        checkoutPage.fill_form_fields()

    def test_009_Navigate_Contact_Page(self):
        homePage = page.HomePage(self.driver)
        homePage.click_contact_button()
        assert self.driver.current_url == CONTACT_LINK

    def test_010_Form_Contact_Page(self):
        homePage = page.HomePage(self.driver)
        homePage.click_contact_button()
        contactPage = page.ContactPage(self.driver)
        contactPage.fill_form_fields()

    def tearDown(self):
        time.sleep(1)
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
