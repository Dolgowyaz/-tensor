from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class ContactsPage(BasePage):
    REGION_CHOOSER = (By.CSS_SELECTOR, 'span.sbis_ru-Region-Chooser__text.sbis_ru-link')
    PARTNER_LIST = (By.ID, 'city-id-2')

    def verify_region(self, region_name):
        region_text = self.wait.until(EC.visibility_of_element_located(self.REGION_CHOOSER)).text
        assert region_text == region_name

    def verify_partner_list(self, city_name):
        partner_list_text = self.wait.until(EC.visibility_of_element_located(self.PARTNER_LIST)).text
        print(f"Partner list text: {partner_list_text}")  # Добавьте эту строку для отладки
        assert city_name in partner_list_text

    def change_region(self, new_region):
        self.wait.until(EC.element_to_be_clickable(self.REGION_CHOOSER)).click()
        new_region_option = (By.XPATH, '//span[text()="41 Камчатский край"]')
        self.wait.until(EC.element_to_be_clickable(new_region_option)).click()
        self.wait.until(EC.text_to_be_present_in_element(self.REGION_CHOOSER, new_region))

    def verify_url_and_title(self, region_name):
        assert region_name in self.browser.current_url, f"Expected region: {region_name}, but it was not found in the URL: {self.browser.current_url}"
        assert region_name in self.browser.title, f"Expected region: {region_name}, but it was not found in the title: {self.browser.title}"
