import pytest

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.data_reader import read_json


login_data = read_json("data/login_data.json")
PRODUCT_NAME = "Sauce Labs Backpack"


@pytest.mark.ui
@pytest.mark.smoke
def test_add_product_to_cart(driver, base_url):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.load(base_url)
    login_page.login(
        login_data["valid_user"]["username"],
        login_data["valid_user"]["password"],
    )
    inventory_page.add_product_to_cart(PRODUCT_NAME)

    assert inventory_page.get_inventory_items_count() == 6
    assert inventory_page.get_cart_badge_count() == 1
