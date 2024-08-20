import pytest
from pages.sbis_page import SBISPage
from pages.tensor_page import TensorPage

@pytest.fixture
def sbis_page(browser):
    page = SBISPage(browser)
    browser.get("https://sbis.ru/")
    return page

@pytest.fixture
def tensor_page(browser):
    return TensorPage(browser)

def test_tensor_scenario(sbis_page, tensor_page):
    sbis_page.navigate_to_contacts()
    sbis_page.click_tensor_banner()
    assert "https://tensor.ru/" in tensor_page.browser.current_url
    tensor_page.verify_strength_in_people_block()
    tensor_page.click_more_details()
    assert "https://tensor.ru/about" in tensor_page.browser.current_url
    tensor_page.verify_photos_dimensions()
    #assert "Tensor" in tensor_page.browser.title  # Дополнительная проверка