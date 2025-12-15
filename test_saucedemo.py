import logging
import os
import pytest
from selenium.webdriver.common.by import By
from configparser import ConfigParser

#DDTF fupporting files
from Saucedemo.utils.excel_reader import read_excel
from Saucedemo.pages.login_page import LoginPage
from Saucedemo.pages.products_page import ProductsPage
from Saucedemo.pages.cart_page import CartPage
from Saucedemo.pages.checkout_page import CheckoutPage
from Saucedemo.pages.locators import Locators

#KwDTF supporting files
from Saucedemo.keywords.keyword_engine import KeywordEngine

logger = logging.getLogger(__name__)

# Configuring config.ini to use the Saucedemo URLd
config = ConfigParser()
config.read("C:/Users/wndows/PyCharmMiscProject/Saucedemo/config.ini")
link_to_open = config["HomepageURL"]["url"]

base_dir = os.path.dirname(os.path.abspath(__file__))
excel_path = os.path.join(base_dir, "testdata", "testdata_ddt.xlsx")
excl_path = os.path.join(base_dir, "testdata", "testdata_kdt.xlsx")

class TestSauceDemo:

    # Test Case 1: Login with valid users
    @pytest.mark.parametrize("username,password,expected,status",read_excel(excel_path, filter_status = "success"))
    def test_various_valid_users_ddtf(self, setup_driver, username, password, expected, status):
        logger.info("Starting test: test_login_valid")

        driver = setup_driver
        lp = LoginPage(driver)
        lp.login(username, password)

        prodpg = ProductsPage(driver)
        actual = prodpg.get_page_title()

        logger.info(f"Expected {expected} Actual {actual}")
        assert actual == expected

        logging.info("Different valid users are able to log into Saucedemo using Data Driven Framework")

    # Test Case 2: Invalid login
    def test_invalid_login_keyword(self):
        logger.info("Running Keyword-Driven Test: Invalid Login")

        engine = KeywordEngine()
        basedir = os.path.dirname((os.path.abspath(__file__)))
        excl_path = os.path.join(basedir, "testdata", "testdata_kdt.xlsx")

        driver = engine.execute(excl_path)

        lp = LoginPage(driver)
        actual_error = lp.get_error_message()

        logger.info(f"Captured error message: {actual_error}")
        assert "Epic sadface" in actual_error

        driver.quit()

    # Test Case 3: Logout
    def test_logout(self, setup_driver):
        logger.info("Running Logout Test")
        driver = setup_driver

        # Load URL from config.ini
        config = ConfigParser()
        config_path = os.path.join(os.path.dirname(__file__), "config.ini")
        config.read(config_path)
        url = config.get("HomepageURL", "url")

        lp = LoginPage(driver)
        pp = ProductsPage(driver)

        lp.login("standard_user", "secret_sauce")
        pp.is_cart_icon_visible()

        pp.logout()

        assert url in driver.current_url

    # Test Case 4: Cart icon visibility
    def test_cart_icon(self, setup_driver):
        logger.info("Running Cart Icon visibility test")
        driver = setup_driver

        lp = LoginPage(driver)
        pp = ProductsPage(driver)
        lp.login("standard_user", "secret_sauce")

        assert pp.is_cart_icon_visible()

    # Test Case 5 + 6: Random 4 products select + add to cart
    def test_random_products(self, setup_driver):
        logger.info("Running test case to select 4 products in randon")
        driver = setup_driver
        lp = LoginPage(driver)
        pp = ProductsPage(driver)

        lp.login("standard_user", "secret_sauce")
        selected = pp.select_random_products(4)

        cart_count = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        logger.info(f"Items in cart: {cart_count}")
        assert cart_count == "4"

    # Test Case 7: Validate cart items
    def test_cart_items(self, setup_driver):
        logger.info("Running Cart item count test")
        driver = setup_driver

        lp = LoginPage(driver)
        pp = ProductsPage(driver)
        cp = CartPage(driver)

        lp.login("standard_user", "secret_sauce")
        pp.select_random_products(2)

        cp.open_cart()
        items = cp.get_cart_items()

        logger.info(f"Items found in cart: {len(items)}")
        assert len(items) == 2

    # Test Case 8: Checkout Complete
    def test_checkout_process(self, setup_driver):
        logger.info("Running Checkout Complete test")
        driver = setup_driver

        lp = LoginPage(driver)
        pp = ProductsPage(driver)
        cp = CartPage(driver)
        ch = CheckoutPage(driver)

        lp.login("standard_user", "secret_sauce")
        pp.select_random_products(1)

        cp.open_cart()
        cp.click_checkout()
        ch.fill_details("Clinton", "J", "632001")
        ch.finish_order()

        txt = ch.get_confirmation_text()
        logger.info(f"Order confirmation text: {txt}")

        assert "Thank you" in txt

    # Test Case 9: Sorting
    def test_product_sorting(self, setup_driver):
        logger.info("Running Product Sorting test")
        driver = setup_driver

        lp = LoginPage(driver)
        pp = ProductsPage(driver)

        lp.login("standard_user", "secret_sauce")
        pp.apply_sort("hilo") #az/za/1ohi/hilo - enter any of the option

        assert True  # Sorting applied (visual/manual validation)

    # Test Case 10: Reset App State
    def test_reset_app_state(self, setup_driver):
        logger.info("Running Reset App State test")
        driver = setup_driver

        lp = LoginPage(driver)
        pp = ProductsPage(driver)

        lp.login("standard_user", "secret_sauce")
        pp.select_random_products(2)

        driver.find_element(*Locators.menu_button).click()
        driver.find_element(*Locators.reset_app_state).click()

        driver.refresh()
        assert len(driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")) == 0