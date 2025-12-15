import logging
from selenium.webdriver.support.ui import WebDriverWait
from .locators import Locators

logger = logging.getLogger(__name__)

class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        logger.info("CartPage initialized.")

    def open_cart(self):
        logger.info("Open cart page")
        self.driver.find_element(*Locators.cart_icon).click()

    def get_cart_items(self):
        logger.info("Fetching cart item")
        return self.driver.find_elements(*Locators.cart_item)

    def click_checkout(self):
        logger.info("Clicking checkout button")
        self.driver.find_element(*Locators.checkout_button).click()
        logger.info("CHeckout button clicked")