import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 10)
        self.logger = logging.getLogger(type(self).__name__)

    def find_element(self, locator):
        self.logger.info(f"Finding element with locator: {locator}")
        return self.browser.find_element(*locator)

    def click_element(self, locator):
        self.logger.info(f"Clicking element with locator: {locator}")
        self.find_element(locator).click()

    def is_element_present(self, locator):
        try:
            self.logger.info(f"Checking if element is present with locator: {locator}")
            self.wait.until(EC.presence_of_element_located(locator))
            return True
        except:
            self.logger.warning(f"Element with locator {locator} is not present")
            return False
