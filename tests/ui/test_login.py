import pytest

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.data_reader import read_json
from utils.logger import get_logger


logger = get_logger(__name__)
login_data = read_json("data/login_data.json")


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.parametrize("credentials", [login_data["valid_user"]])
def test_successful_login(driver, base_url, credentials):
    logger.info("Starting test_successful_login")
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.load(base_url)
    login_page.login(credentials["username"], credentials["password"])

    assert inventory_page.is_loaded(), "Inventory page should be displayed"
    assert "inventory.html" in inventory_page.get_current_url()
    assert inventory_page.get_title() == "Products"
    logger.info("Finished test_successful_login")


@pytest.mark.ui
@pytest.mark.negative
@pytest.mark.parametrize("credentials", [login_data["invalid_user"]])
def test_invalid_login_shows_error(driver, base_url, credentials):
    logger.info("Starting test_invalid_login_shows_error")
    login_page = LoginPage(driver)

    login_page.load(base_url)
    login_page.login(credentials["username"], credentials["password"])

    assert login_page.is_error_displayed(), "Error message should be visible"
    assert "Username and password do not match" in login_page.get_error_message()
    assert driver.current_url == base_url + "/"
    logger.info("Finished test_invalid_login_shows_error")
