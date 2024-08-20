import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import os
import time
import shutil

@pytest.fixture
def browser():
    chrome_options = webdriver.ChromeOptions()
    prefs = {
        'download.default_directory': os.path.join(os.getcwd(), "downloads"),
        'safebrowsing.enabled': 'false'  # Отключение защиты от небезопасных загрузок
    }
    chrome_options.add_experimental_option('prefs', prefs)
    chrome_options.add_argument('--safebrowsing-disable-download-protection')
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

def test_download_plugin(browser):
    # Шаг 1: Перейти на https://sbis.ru/
    browser.get("https://sbis.ru/")

    # Шаг 2: В Footer'e найти и перейти "Скачать локальные версии"
    download_link = WebDriverWait(browser, 60).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,
                                    "#container > div.sbisru-Footer.sbisru-Footer__scheme--default > div.sbis_ru-container > div.sbisru-Footer__container > div:nth-child(3) > ul > li:nth-child(8) > a"))
    )
    download_link.click()

    # Шаг 3: Скачать СБИС Плагин для windows, веб-установщик в папку с данным тестом
    download_button = WebDriverWait(browser, 60).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Скачать (Exe 11.05 МБ)')]"))
    )
    download_button.click()

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