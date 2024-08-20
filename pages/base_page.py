import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 10)
        self.logger = logging.getLogger(type(self).__name__)

    def find_element(self, locator):
        self.logger.info(f"Поиск элемента с локатором: {locator}")
        return self.browser.find_element(*locator)

    def click_element(self, locator):
        self.logger.info(f"Клик по элементу с локатором: {locator}")
        self.find_element(locator).click()

    def is_element_present(self, locator):
        try:
            self.logger.info(f"Проверка наличия элемента с локатором: {locator}")
            self.wait.until(EC.presence_of_element_located(locator))
            return True
        except:
            self.logger.warning(f"Элемент с локатором {locator} не найден")
            return False
