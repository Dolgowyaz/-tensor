import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os
import time
from pages.download_page import DownloadPage
from pages.main_page import MainPage

@pytest.fixture
def browser():
    """
    Фикстура для инициализации и завершения работы веб-драйвера.

    Возвращает:
    WebDriver: Экземпляр веб-драйвера.
    """
    chrome_options = webdriver.ChromeOptions()
    prefs = {
        'download.default_directory': os.path.join(os.getcwd(), "downloads"),
        'safebrowsing.enabled': 'false'  # Отключение защиты от небезопасных загрузок
    }
    chrome_options.add_experimental_option('prefs', prefs)
    chrome_options.add_argument('--safebrowsing-disable-download-protection')
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)
    yield driver
    driver.quit()

#@pytest.mark.skip(reason="пропуск сценария")
def test_download_plugin(browser):
    """
    Тестовый сценарий для проверки загрузки плагина.

    Параметры:
    browser (WebDriver): Экземпляр веб-драйвера.
    """
    main_page = MainPage(browser)
    download_page = DownloadPage(browser)

    # Шаг 1: Перейти на https://sbis.ru/
    browser.get("https://sbis.ru/")

    # Шаг 2: В Footer'e найти и перейти "Скачать локальные версии"
    main_page.click_download_link()

    # Шаг 3: Скачать СБИС Плагин для windows, веб-установщик в папку с данным тестом
    download_page.click_download_button()

    # Шаг 4: Убедиться, что плагин скачался
    download_dir = os.path.join(os.getcwd(), "downloads")
    os.makedirs(download_dir, exist_ok=True)

    # Ожидание завершения скачивания
    time.sleep(20)  # Увеличенное время ожидания

    # Шаг 5: Сравнить размер скачанного файла в мегабайтах. Он должен совпадать с указанным на сайте
    downloaded_files = os.listdir(download_dir)
    assert len(downloaded_files) == 1
    downloaded_file = os.path.join(download_dir, downloaded_files[0])
    file_size = os.path.getsize(downloaded_file) / (1024 * 1024)  # Размер в мегабайтах
    expected_size = 11.05  # Ожидаемый размер в мегабайтах
    assert abs(file_size - expected_size) < 0.1  # Допустимая погрешность

    # Удаление скачанного файла перед закрытием браузера
    os.remove(downloaded_file)

    # Закрытие браузера после завершения скачивания
    browser.quit()