import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Saucedemo.pages.locators import Locators

logger = logging.getLogger(__name__)

class LoginKeywords:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        logger.info("LoginKeywords initialized")

    def input_text(self, locator, value):
        logger.info("Input Text fetched from keyword driven excel")
        loc = getattr(Locators, locator)
        try:
            ele = self.wait.until(EC.visibility_of_element_located(loc))
            ele.clear()
            ele.send_keys(value)
            logger.info(f"Successfully entered text into {locator}")
        except Exception as e:
            logger.error(f"Failed to enter text into {locator} → {e}")
            raise

    def click(self, locator):
        logger.info("Click action")
        loc = getattr(Locators, locator)
        try:
            ele = self.wait.until(EC.element_to_be_clickable(loc))
            ele.click()
            logger.info("Successfully clicked")
        except Exception as e:
            logger.error(f"Failed to click {e}")
            raise

    def verify_text(self, locator, expected):
        logger.info(f"Verify Text  Locator: {locator}, Expected: {expected}")
        loc = getattr(Locators, locator)
        try:
            ele = self.wait.until(EC.visibility_of_element_located(loc))
            actual = ele.text
            assert expected in actual, f"Expected '{expected}', got '{actual}'"
            logger.info("Text verification successful.")
        except AssertionError as a:
            logger.error(f"Text verification failed {a}")
            raise
        except Exception as e:
            logger.error(f"Error occurs during test verification {e}")
            raise