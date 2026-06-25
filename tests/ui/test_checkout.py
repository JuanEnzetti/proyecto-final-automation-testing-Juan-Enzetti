import pytest

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.data_reader import read_json


login_data = read_json("data/login_data.json")
PRODUCT_NAME = "Sauce Labs Backpack"


@pytest.mark.ui
@pytest.mark.regression
def test_complete_checkout(driver, base_url):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.load(base_url)
    login_page.login(
        login_data["valid_user"]["username"],
        login_data["valid_user"]["password"],
    )
    inventory_page.add_product_to_cart(PRODUCT_NAME)
    inventory_page.go_to_cart()
    cart_page.checkout()

    checkout_page.fill_customer_information("Juan", "Tester", "1407")

    assert checkout_page.get_title() == "Checkout: Overview"
    assert "Total:" in checkout_page.get_summary_total()

    checkout_page.finish_checkout()

    assert checkout_page.get_title() == "Checkout: Complete!"
    assert checkout_page.get_complete_message() == "Thank you for your order!"
