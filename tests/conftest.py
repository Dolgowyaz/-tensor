import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import logging

# Настройка логгирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@pytest.fixture(scope="module")
def browser():
    """
    Фикстура для инициализации и завершения работы веб-драйвера.

    Возвращает:
    WebDriver: Экземпляр веб-драйвера.
    """
    try:
        # Настройки для веб-драйвера
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')  # Максимизировать окно
        # options.add_argument('--headless')  # Запуск в headless режиме (опционально)

        # Используйте ChromeDriverManager для установки драйвера и передайте options
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        logger.info("WebDriver инициализирован успешно")
        yield driver
    except Exception as e:
        logger.error(f"Ошибка при инициализации webdriver: {e}")
    finally:
        if 'driver' in locals() and driver is not None:
            logger.info("Завершение работы WebDriver")
            driver.quit()
