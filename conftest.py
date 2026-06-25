import base64
import datetime
import os
import pathlib

import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from utils.api_client import ReqresClient
from utils.logger import get_logger


logger = get_logger("pytest")


@pytest.fixture(scope="session")
def base_url():
    return "https://www.saucedemo.com"


@pytest.fixture(scope="session")
def api_url():
    return "https://reqres.in"


@pytest.fixture(scope="session")
def api_client(api_url):
    return ReqresClient(api_url)


@pytest.fixture
def driver():
    logger.info("Starting Chrome WebDriver")
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    if os.getenv("CI") == "true":
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")

    if os.getenv("CI") == "true":
        browser = webdriver.Chrome(options=options)
    else:
        service = Service(ChromeDriverManager().install())
        browser = webdriver.Chrome(service=service, options=options)
    browser.implicitly_wait(0)

    yield browser

    logger.info("Closing Chrome WebDriver")
    browser.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver_instance = item.funcargs.get("driver")

        if driver_instance:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            target = pathlib.Path("reports/screenshots")
            target.mkdir(parents=True, exist_ok=True)
            file_name = target / f"{item.name}_{timestamp}.png"

            driver_instance.save_screenshot(str(file_name))
            logger.error("Screenshot saved for failed test: %s", file_name)

            encoded_screenshot = base64.b64encode(file_name.read_bytes()).decode("utf-8")
            extras = getattr(report, "extras", [])
            extras.append(pytest_html.extras.png(encoded_screenshot, name="screenshot"))
            report.extras = extras
