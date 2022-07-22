from email import message
from locator import *
from element import BasePageElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

    def navigate_cart_page(self):
        buy_button = self.driver.find_element(*ShopPageLocators.BUY_BUTTON)
        buy_button.click()
        cart_button = self.driver.find_element(*ShopPageLocators.CART)
        cart_button.click()


class CartPage(ShopPage):
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

    def confirm_empty_cart(self):
        cart_empty_button = self.driver.find_element(
            *CartPageLocators.CART_EMPTY)
        cart_empty_button.click()
        cart_confirm = self.driver.find_element(
            *CartPageLocators.CART_YES_OPTION)
        cart_confirm.click()

    def check_cart_empty(self):
        cart_shopping_button = self.driver.find_element(
            *CartPageLocators.CART_SHOPPING_BUTTON)
        return cart_shopping_button

    def click_checkout_button(self):
        checkout_button = self.driver.find_element(
            *CartPageLocators.CHECKOUT_BUTTON)
        checkout_button.click()


class CheckoutPage(BasePage):
    def fill_form_fields(self):
        forename = self.driver.find_element(*CheckoutPageLocators.FORENAME)
        email = self.driver.find_element(*CheckoutPageLocators.EMAIL)
        address = self.driver.find_element(*CheckoutPageLocators.ADDRESS)
        card_type = Select(self.driver.find_element(
            *CheckoutPageLocators.CARD_TYPE))
        visa_option = card_type.select_by_value('Visa')
        card = self.driver.find_element(*CheckoutPageLocators.CARD)
        submit_button = self.driver.find_element(
            *CheckoutPageLocators.SUBMIT_BUTTON)
        actions = ActionChains(self.driver)
        try:
            actions.send_keys_to_element(forename, 'John')
            actions.send_keys_to_element(email, 'john@gmail.com')
            actions.send_keys_to_element(address, '2/13 Joy St')
            actions.click(visa_option)
            actions.send_keys_to_element(card, '1234 5678 9988')
            actions.click(submit_button)
            actions.perform()
            shop_again_button = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Shopping Again')))
            assert shop_again_button.is_displayed()

        finally:
            time.sleep(1)


class ContactPage(BasePage):
    def fill_form_fields(self):
        forename = self.driver.find_element(*ContactPageLocators.FORENAME)
        email = self.driver.find_element(*ContactPageLocators.EMAIL)
        message = self.driver.find_element(*ContactPageLocators.MESSAGE)
        submit_button = self.driver.find_element(
            *ContactPageLocators.SUBMIT_BUTTON)
        actions = ActionChains(self.driver)
        try:
            actions.send_keys_to_element(forename, 'John')
            actions.send_keys_to_element(email, 'john@gmail.com')
            actions.send_keys_to_element(
                message, 'This is a message to Jupiter Toys')
            actions.click(submit_button)
            actions.perform()

            alert_success = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'alert-success')))
            assert alert_success.is_displayed()

        finally:
            time.sleep(1)
