from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")
    TITLE = (By.CLASS_NAME, "title")

    @staticmethod
    def remove_button(product_name):
        slug = product_name.lower().replace(" ", "-")
        return By.ID, f"remove-{slug}"

    def get_title(self):
        return self.get_text(self.TITLE)

    def get_cart_items_count(self):
        return len(self.driver.find_elements(*self.CART_ITEMS))

    def remove_product(self, product_name):
        self.click(self.remove_button(product_name))

    def checkout(self):
        self.click(self.CHECKOUT_BUTTON)
