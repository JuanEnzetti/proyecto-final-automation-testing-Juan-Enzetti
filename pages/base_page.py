from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils.logger import get_logger


class BasePage:
    """Base class with shared Selenium actions for every page object."""

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.logger = get_logger(self.__class__.__name__)

    def open_url(self, url):
        self.logger.info("Navigating to URL: %s", url)
        self.driver.get(url)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_all(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click(self, locator):
        self.logger.info("Clicking element: %s", locator)
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type_text(self, locator, text, clear=True):
        self.logger.info("Typing text into element: %s", locator)
        element = self.wait.until(EC.visibility_of_element_located(locator))
        if clear:
            element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def is_visible(self, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()
        except TimeoutException:
            return False

    def get_current_url(self):
        return self.driver.current_url

    def wait_for_url_contains(self, text):
        self.logger.info("Waiting for URL to contain: %s", text)
        return self.wait.until(EC.url_contains(text))
