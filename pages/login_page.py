from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Saucedemo.pages.locators import Locators
from configparser import ConfigParser
import logging
logger = logging.getLogger(__name__)

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

        # Configuring config.ini to use the OrangeHRM URLd
        config = ConfigParser()
        config.read("C:/Users/wndows/PyCharmMiscProject/Saucedemo/config.ini")
        self.link_to_open = config["HomepageURL"]["url"]
        logger.info(f"LoginPage initialized with URL: {self.link_to_open}")

    def login(self, username, password):

        self.driver.get(self.link_to_open)

        logger.info(f"Entering username: {username}")
        user = self.wait.until(EC.visibility_of_element_located(Locators.login_username))
        user.clear()
        user.send_keys(username)

        logger.info(f"Entering password: {password}")
        pwd = self.wait.until(EC.visibility_of_element_located(Locators.login_password))
        pwd.clear()
        pwd.send_keys(password)

        logger.info("Clicking login button")
        button = self.wait.until(EC.element_to_be_clickable(Locators.login_button))
        button.click()

        logger.info("Login action completed")

    def get_error_message(self):
        try:
            logger.info("Checking for login error message")
            return self.wait.until(EC.visibility_of_element_located(Locators.login_error)).text
            logger.info(f"Error message found: {error_msg}")
        except:
            logger.info("No error message found")
            return None