import pytest

from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.data_reader import read_json


login_data = read_json("data/login_data.json")
PRODUCT_NAME = "Sauce Labs Backpack"


@pytest.mark.ui
@pytest.mark.regression
def test_remove_product_from_cart(driver, base_url):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    login_page.load(base_url)
    login_page.login(
        login_data["valid_user"]["username"],
        login_data["valid_user"]["password"],
    )
    inventory_page.add_product_to_cart(PRODUCT_NAME)
    inventory_page.go_to_cart()

    assert cart_page.get_title() == "Your Cart"
    assert cart_page.get_cart_items_count() == 1

    cart_page.remove_product(PRODUCT_NAME)

    assert cart_page.get_cart_items_count() == 0
