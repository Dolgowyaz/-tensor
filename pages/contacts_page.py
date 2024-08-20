from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import logging

class ContactsPage(BasePage):
    REGION_CHOOSER = (By.CSS_SELECTOR, 'span.sbis_ru-Region-Chooser__text.sbis_ru-link')
    PARTNER_LIST = (By.ID, 'city-id-2')

    def __init__(self, browser):
        super().__init__(browser)
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch = logging.StreamHandler()
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

    def verify_region(self, region_name):
        region_text = self.wait.until(EC.visibility_of_element_located(self.REGION_CHOOSER)).text
        self.logger.info(f"Текст региона: {region_text}")
        assert region_text == region_name, f"Ожидаемый регион: {region_name}, но найден: {region_text}"

    def verify_partner_list(self, city_name):
        partner_list_text = self.wait.until(EC.visibility_of_element_located(self.PARTNER_LIST)).text
        self.logger.info(f"Текст списка партнеров: {partner_list_text}")
        assert city_name in partner_list_text, f"Ожидаемый город: {city_name}, но он не найден в списке партнеров: {partner_list_text}"

    def change_region(self, new_region):
        self.logger.info("Изменение региона")
        self.wait.until(EC.element_to_be_clickable(self.REGION_CHOOSER)).click()
        new_region_option = (By.XPATH, f'//span[text()="41 Камчатский край"]')
        self.wait.until(EC.element_to_be_clickable(new_region_option)).click()
        self.wait.until(EC.text_to_be_present_in_element(self.REGION_CHOOSER, new_region))

    def verify_url_and_title(self, region_name):
        self.logger.info(f"Текущий URL: {self.browser.current_url}")
        self.logger.info(f"Текущий заголовок: {self.browser.title}")
        assert region_name in self.browser.current_url, f"Ожидаемый регион: {region_name}, но он не найден в URL: {self.browser.current_url}"
        assert region_name in self.browser.title, f"Ожидаемый регион: {region_name}, но он не найден в заголовке: {self.browser.title}"
