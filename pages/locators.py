from selenium.webdriver.common.by import By

class Locators:

    # Login Page
    login_username = (By.ID, "user-name")
    login_password = (By.ID, "password")
    login_button = (By.ID, "login-button")
    login_error = (By.XPATH, "//h3[@data-test='error']")

    # Products Page
    cart_icon = (By.ID, "shopping_cart_container")
    product_items = (By.CLASS_NAME, "inventory_item")
    product_name = (By.CLASS_NAME, "inventory_item_name")
    product_price = (By.CLASS_NAME, "inventory_item_price")
    add_to_cart_buttons = (By.XPATH, "//button[contains(text(),'Add to cart')]")
    sort_dropdown = (By.CLASS_NAME, "product_sort_container")

    # Left Menu
    menu_button = (By.ID, "react-burger-menu-btn")
    logout_link = (By.ID, "logout_sidebar_link")
    reset_app_state = (By.ID, "reset_sidebar_link")

    # Cart Page
    cart_item = (By.CLASS_NAME, "cart_item")
    item_name_cart = (By.CLASS_NAME, "inventory_item_name")
    item_price_cart = (By.CLASS_NAME, "inventory_item_price")
    checkout_button = (By.ID, "checkout")

    # Checkout Page
    first_name = (By.ID, "first-name")
    last_name = (By.ID, "last-name")
    postal_code = (By.ID, "postal-code")
    continue_button = (By.ID, "continue")
    finish_button = (By.ID, "finish")
    summary_title = (By.CLASS_NAME, "summary_info")
    complete_header = (By.CLASS_NAME, "complete-header")