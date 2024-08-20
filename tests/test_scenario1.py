import pytest
from pages.sbis_page import SBISPage
from pages.tensor_page import TensorPage

@pytest.fixture
def sbis_page(browser):
    """
    Фикстура для инициализации страницы СБИС.

    Параметры:
    browser (WebDriver): Экземпляр веб-драйвера.

    Возвращает:
    SBISPage: Экземпляр страницы СБИС.
    """
    page = SBISPage(browser)
    browser.get("https://sbis.ru/")
    return page

@pytest.fixture
def tensor_page(browser):
    """
    Фикстура для инициализации страницы Tensor.

    Параметры:
    browser (WebDriver): Экземпляр веб-драйвера.

    Возвращает:
    TensorPage: Экземпляр страницы Tensor.
    """
    return TensorPage(browser)

#@pytest.mark.skip(reason="пропуск сценария")
def test_tensor_scenario(sbis_page, tensor_page):
    """
    Тестовый сценарий для проверки функциональности Tensor.

    Параметры:
    sbis_page (SBISPage): Экземпляр страницы СБИС.
    tensor_page (TensorPage): Экземпляр страницы Tensor.
    """
    sbis_page.navigate_to_contacts()
    sbis_page.click_tensor_banner()
    assert "https://tensor.ru/" in tensor_page.browser.current_url
    tensor_page.verify_strength_in_people_block()
    tensor_page.click_more_details()
    assert "https://tensor.ru/about" in tensor_page.browser.current_url
    tensor_page.verify_photos_dimensions()
    #assert "Tensor" in tensor_page.browser.title  # Дополнительная проверка