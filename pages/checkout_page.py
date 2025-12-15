import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Saucedemo.pages.locators import Locators

logger = logging.getLogger(__name__)

class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        logger.info("CheckoutPage Initialized")

    def fill_details(self, fname, lname, zip):
        logger.info("Filling checkout information")
        self.driver.find_element(*Locators.first_name).send_keys(fname)
        self.driver.find_element(*Locators.last_name).send_keys(lname)
        self.driver.find_element(*Locators.postal_code).send_keys(zip)
        logger.info("Clicking Continue button")
        self.driver.find_element(*Locators.continue_button).click()

    def finish_order(self):
        logger.info("Finishing checkout process")
        self.driver.find_element(*Locators.finish_button).click()
        logger.info("Complete button clicked, Order should be placed")

    def get_confirmation_text(self):
        logger.info("Fetching order confirmation text")
        return self.wait.until(EC.visibility_of_element_located(Locators.complete_header)).text