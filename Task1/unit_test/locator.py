# File to locate page elements by CSS Selector, HTML attributes...

from selenium.webdriver.common.by import By


class HomePageLocators(object):
    SHOPPING_BUTTON = (By.PARTIAL_LINK_TEXT, 'Shopping')


class ShopPageLocators(object):
    TEDDY_BEAR = (By.ID, 'product-1')
    BUY_BUTTON = (By.XPATH, '//a[text()="Buy"]')
    CART = (By.ID, 'nav-cart')
    CART_COUNT = (By.CLASS_NAME, 'cart-count')

