from locator import *
from element import BasePageElement

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class HomePage(BasePage):

    def is_url_matches(self):
        return "home" in self.driver.current_url

    def click_shopping_button(self):
        # '*' is passed as args to define an element
        element = self.driver.find_element(*HomePageLocators.SHOPPING_BUTTON)
        element.click()

class ShopPage(BasePage):

    def is_url_matches(self):
        return "shop" in self.driver.current_url
    
    def click_buy_button(self):
        element = self.driver.find_element(ShopPageLocators.TEDDY_BEAR) # first item
        buy_button = element.find_element(*ShopPageLocators.BUY_BUTTON)

        buy_button.click()
    
    def check_cart(self):
        cart = self.driver.find_element(*ShopPageLocators.CART)
        cart_count = cart.find_element(*ShopPageLocators.CART_COUNT)
        print(cart_count)