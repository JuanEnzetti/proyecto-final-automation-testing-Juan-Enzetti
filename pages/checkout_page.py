from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    SUMMARY_TOTAL = (By.CLASS_NAME, "summary_total_label")
    TITLE = (By.CLASS_NAME, "title")

    def fill_customer_information(self, first_name, last_name, postal_code):
        self.type_text(self.FIRST_NAME_INPUT, first_name)
        self.type_text(self.LAST_NAME_INPUT, last_name)
        self.type_text(self.POSTAL_CODE_INPUT, postal_code)
        self.click(self.CONTINUE_BUTTON)

    def finish_checkout(self):
        self.click(self.FINISH_BUTTON)

    def complete_checkout(self, first_name, last_name, postal_code):
        self.fill_customer_information(first_name, last_name, postal_code)
        self.finish_checkout()

    def get_title(self):
        return self.get_text(self.TITLE)

    def get_summary_total(self):
        return self.get_text(self.SUMMARY_TOTAL)

    def get_complete_message(self):
        return self.get_text(self.COMPLETE_HEADER)
