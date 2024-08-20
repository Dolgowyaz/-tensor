import pytest
from pages.sbis_page import SBISPage
from pages.contacts_page import ContactsPage

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
def contacts_page(browser):
    """
    Фикстура для инициализации страницы контактов.

    Параметры:
    browser (WebDriver): Экземпляр веб-драйвера.

    Возвращает:
    ContactsPage: Экземпляр страницы контактов.
    """
    return ContactsPage(browser)

#@pytest.mark.skip(reason="пропуск сценария")
def test_contacts_scenario_2(sbis_page, contacts_page):
    """
    Тестовый сценарий для проверки функциональности контактов.

    Параметры:
    sbis_page (SBISPage): Экземпляр страницы СБИС.
    contacts_page (ContactsPage): Экземпляр страницы контактов.
    """
    sbis_page.navigate_to_contacts()
    contacts_page.verify_region("Республика Башкортостан")
    contacts_page.verify_partner_list("Уфа")  # Передаем аргумент city_name
    contacts_page.change_region("Камчатский край")
    contacts_page.verify_region("Камчатский край")
    contacts_page.verify_partner_list("Петропавловск-Камчатский")  # Передаем аргумент city_name