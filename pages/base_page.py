import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Настройка логгирования для всего модуля
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class BasePage:
    """
    Базовый класс для всех страниц.
    Предоставляет общие методы для взаимодействия с элементами на странице.
    """

    def __init__(self, browser):
        """
        Инициализация базовой страницы.

        Параметры:
        browser (WebDriver): Экземпляр веб-драйвера.
        """
        self.browser = browser  # Сохраняем экземпляр веб-драйвера
        self.wait = WebDriverWait(self.browser, 10)  # Инициализация WebDriverWait с таймаутом 10 секунд
        self.logger = logging.getLogger(type(self).__name__)  # Инициализация логгера для текущего класса

    def find_element(self, locator):
        """
        Поиск элемента на странице по локатору.

        Параметры:
        locator (tuple): Кортеж с типом локатора и значением локатора.

        Возвращает:
        WebElement: Найденный элемент.
        """
        self.logger.info(f"Поиск элемента с локатором: {locator}")
        return self.browser.find_element(*locator)

    def click_element(self, locator):
        """
        Клик по элементу на странице по локатору.

        Параметры:
        locator (tuple): Кортеж с типом локатора и значением локатора.
        """
        self.logger.info(f"Клик по элементу с локатором: {locator}")
        self.find_element(locator).click()

    def is_element_present(self, locator):
        """
        Проверка наличия элемента на странице по локатору.

        Параметры:
        locator (tuple): Кортеж с типом локатора и значением локатора.

        Возвращает:
        bool: True, если элемент присутствует, иначе False.
        """
        try:
            self.logger.info(f"Проверка наличия элемента с локатором: {locator}")
            self.wait.until(EC.presence_of_element_located(locator))
            return True
        except:
            self.logger.warning(f"Элемент с локатором {locator} не найден")
            return False
