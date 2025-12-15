import logging
import os
import pytest
import allure
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# Logging Setup
def pytest_configure():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        log_dir = os.path.join(os.path.dirname(__file__), "logs")
        os.makedirs(log_dir, exist_ok=True)

        file_path = os.path.join(log_dir, "test_logs.log")
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

        file_handler = logging.FileHandler(file_path)
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

# Command-line browser option
def pytest_addoption(parser):
    parser.addoption("--browser-name", default="firefox", help="Choose browser")

# Driver Fixture
@pytest.fixture()
def setup_driver(request):
    browser_name = request.config.getoption("--browser-name").lower()

    if browser_name == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    elif browser_name == "edge":
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

    else:
        raise ValueError(f"Browser '{browser_name}' not supported.")

    driver.maximize_window()
    yield driver

    try:
        driver.quit()
    except Exception:
        print("Error quitting driver")

# Screenshot for EVERY Test Case (Pass + Fail)
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when != "call":
        return

    driver = item.funcargs.get("setup_driver", None)
    if not driver:
        return

    # Choose file name based on status
    status = "passed" if report.passed else "failed"

    screenshot_dir = os.path.join(os.path.dirname(__file__), "screenshots")
    os.makedirs(screenshot_dir, exist_ok=True)

    file_name = f"{item.name}_{status}.png"
    file_path = os.path.join(screenshot_dir, file_name)

    # Save screenshot file
    try:
        driver.save_screenshot(file_path)
    except Exception:
        pass

    # Attach in Allure
    try:
        png = driver.get_screenshot_as_png()
        allure.attach(
            png,
            name=f"{item.name} - {status}",
            attachment_type=allure.attachment_type.PNG,
        )
    except Exception:
        pass