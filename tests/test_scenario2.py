import pytest
from pages.sbis_page import SBISPage
from pages.contacts_page import ContactsPage

@pytest.fixture
def sbis_page(browser):
    page = SBISPage(browser)
    browser.get("https://sbis.ru/")
    return page

@pytest.fixture
def contacts_page(browser):
    return ContactsPage(browser)
#@pytest.mark.skip(reason="Skip this test")
def test_contacts_scenario_2(sbis_page, contacts_page):
    sbis_page.navigate_to_contacts()
    contacts_page.verify_region("Республика Башкортостан")
    contacts_page.verify_partner_list("Уфа")  # Передаем аргумент city_name
    contacts_page.change_region("Камчатский край")
    contacts_page.verify_region("Камчатский край")
    contacts_page.verify_partner_list("Петропавловск-Камчатский")  # Передаем аргумент city_name