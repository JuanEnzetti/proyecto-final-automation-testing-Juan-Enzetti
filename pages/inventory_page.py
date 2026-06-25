from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class InventoryPage(BasePage):
    INVENTORY_CONTAINER = (By.ID, "inventory_container")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    TITLE = (By.CLASS_NAME, "title")

    @staticmethod
    def add_to_cart_button(product_name):
        slug = product_name.lower().replace(" ", "-")
        return By.ID, f"add-to-cart-{slug}"

    @staticmethod
    def remove_button(product_name):
        slug = product_name.lower().replace(" ", "-")
        return By.ID, f"remove-{slug}"

    def is_loaded(self):
        return self.is_visible(self.INVENTORY_CONTAINER)

    def get_title(self):
        return self.get_text(self.TITLE)

    def get_inventory_items_count(self):
        return len(self.find_all(self.INVENTORY_ITEMS))

    def add_product_to_cart(self, product_name):
        self.click(self.add_to_cart_button(product_name))

    def remove_product_from_inventory(self, product_name):
        self.click(self.remove_button(product_name))

    def get_cart_badge_count(self):
        if not self.is_visible(self.CART_BADGE):
            return 0
        return int(self.get_text(self.CART_BADGE))

    def go_to_cart(self):
        self.click(self.CART_LINK)
