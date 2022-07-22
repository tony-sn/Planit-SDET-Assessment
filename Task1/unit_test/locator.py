# File to locate page elements by CSS Selector, HTML attributes...

from selenium.webdriver.common.by import By


class HomePageLocators(object):
    SHOPPING_BUTTON = (By.PARTIAL_LINK_TEXT, 'Shopping')
    CONTACT_BUTTON = (By.XPATH, "//a[text()='Contact']")
    LOGIN_BUTTON = (By.ID, "nav-login")
    LOGIN_MODAL = (By.XPATH, "//div[@class='popup modal hide ng-scope in']")


class ShopPageLocators(object):
    BUY_BUTTON = (By.XPATH, '//a[text()="Buy"]')
    CART = (By.ID, 'nav-cart')
    CART_COUNT = (By.XPATH, '//span[@class=\'cart-count ng-binding\']')


class CartPageLocators(object):
    CART_QUANTITY = (By.CLASS_NAME, 'input-mini')
    CART_COUNT = (By.XPATH, '//span[@class=\'cart-count ng-binding\']')
    CART_EMPTY = (By.XPATH, '//a[@class=\'btn btn-danger ng-scope\']')
    CART_YES_OPTION = (By.XPATH, "//a[@class='btn btn-success']")
    CART_SHOPPING_BUTTON = (By.PARTIAL_LINK_TEXT, 'Shopping')
    CHECKOUT_BUTTON = (
        By.XPATH, "//a[@class='btn-checkout btn btn-success  ng-scope']")


class CheckoutPageLocators(object):
    FORENAME = (By.ID, 'forename')
    EMAIL = (By.ID, 'email')
    ADDRESS = (By.ID, 'address')
    CARD_TYPE = (By.ID, 'cardType')
    CARD = (By.ID, 'card')
    SUBMIT_BUTTON = (By.ID, 'checkout-submit-btn')


class ContactPageLocators(object):
    FORENAME = (By.ID, 'forename')
    EMAIL = (By.ID, 'email')
    MESSAGE = (By.ID, 'message')
    SUBMIT_BUTTON = (By.XPATH, "//a[text()='Submit']")
