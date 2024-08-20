import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="module")
def browser():
    try:
        # Настройки для веб-драйвера
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')  # Максимизировать окно
        # options.add_argument('--headless')  # Запуск в headless режиме (опционально)

        # Используйте ChromeDriverManager для установки драйвера и передайте options
        driver = webdriver.Chrome(service=webdriver.chrome.service.Service(ChromeDriverManager().install()), options=options)
        yield driver
    except Exception as e:
        print(f"Error initializing webdriver: {e}")
    finally:
        if 'driver' in locals() and driver is not None:
            driver.quit()