from locator import *
from element import BasePageElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class HomePage(BasePage):

    def click_shopping_button(self):
        # '*' is passed as args to define an element
        element = self.driver.find_element(*HomePageLocators.SHOPPING_BUTTON)
        element.click()

    def click_contact_button(self):
        contact_button = self.driver.find_element(
            *HomePageLocators.CONTACT_BUTTON)
        contact_button.click()

    def click_login_button(self):
        login_button = self.driver.find_element(*HomePageLocators.LOGIN_BUTTON)
        login_button.click()

    def check_login_modal(self):
        login_modal = self.driver.find_element(*HomePageLocators.LOGIN_MODAL)
        return login_modal


class ShopPage(BasePage):
    def click_buy_button(self):
        buy_button = self.driver.find_element(*ShopPageLocators.BUY_BUTTON)
        buy_button.click()

    def click_cart_button(self):
        cart_button = self.driver.find_element(*ShopPageLocators.CART)
        cart_button.click()

    def check_cart(self):
        cart_count_element = self.driver.find_element(
            *ShopPageLocators.CART_COUNT)
        return cart_count_element


class CartPage(BasePage):
    def edit_cart(self):
        item_quantity_element = self.driver.find_element(
            *CartPageLocators.CART_QUANTITY)
        actions = ActionChains(self.driver)
        actions.click(item_quantity_element)
        actions.send_keys(Keys.BACK_SPACE)
        time.sleep(1)
        actions.send_keys('2')
        actions.send_keys(Keys.ENTER)
        actions.perform()

    def check_cart(self):
        cart_count_element = self.driver.find_element(
            *CartPageLocators.CART_COUNT)
        return cart_count_element

    def click_empty_cart(self):
        cart_empty_button = self.driver.find_element(
            *CartPageLocators.CART_EMPTY)
        cart_empty_button.click()

    def confirm_empty_cart(self):
        cart_confirm = self.driver.find_element(
            *CartPageLocators.CART_YES_OPTION)
        cart_confirm.click()

    def check_cart_empty(self):
        cart_shopping_button = self.driver.find_element(
            *CartPageLocators.CART_SHOPPING_BUTTON)
        return cart_shopping_button
