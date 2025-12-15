import random
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Saucedemo.pages.locators import Locators

logger = logging.getLogger(__name__)

class ProductsPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        logger.info("ProductsPage initialized.")

    def get_page_title(self):
        logger.info("Fetching product page title")
        title = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))
        logger.info(f"Fetching product page title: {title.text}")
        return title.text

    def is_cart_icon_visible(self):
        logger.info("Checking Cart icon is visible")
        return self.wait.until(EC.visibility_of_element_located(Locators.cart_icon))

    def get_all_products(self):
        logger.info("Fetching all products listed on page...")
        products =  self.driver.find_elements(*Locators.product_items)
        logger.info(f"Total products found: {len(products)}")
        return products


    def select_random_products(self, count=4):
        logger.info(f"Selecting {count} random products.")
        products = self.get_all_products()
        if len(products) < count:
            logger.warning(f"Requested {count} items but only {len(products)} available.")
        selected = random.sample(products, count)

        data = []
        for product in selected:
            name = product.find_element(*Locators.product_name).text
            price = product.find_element(*Locators.product_price).text
            logger.info(f"Adding product: {name} | {price}")
            btn = product.find_element(By.TAG_NAME, "button")
            btn.click()
            data.append((name, price))
            logger.info(f"Total {len(selected)} items added to cart.")
        return data

    def apply_sort(self, value):
        logger.info(f"Applying sort option: {value}")
        dropdown = self.driver.find_element(*Locators.sort_dropdown)
        dropdown.click()
        dropdown.find_element(By.XPATH, f"//option[@value='{value}']").click()
        logger.info(f"Sort is done: {value}")

    def logout(self):
        logger.info("Attempting logout via sidebar")
        # Click menu button
        menu = self.wait.until(
            EC.element_to_be_clickable(Locators.menu_button)
        )
        menu.click()
        logger.info("Menu button clicked")

        # Wait until menu animation completes
        self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".bm-menu"))
        )

        # Click Logout
        logout_btn = self.wait.until(
            EC.element_to_be_clickable(Locators.logout_link)
        )
        logout_btn.click()
        logger.info("Logout completed.")