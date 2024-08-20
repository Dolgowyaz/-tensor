from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import logging

class TensorPage(BasePage):
    STRENGTH_IN_PEOPLE_BLOCK = (By.CSS_SELECTOR, 'div.tensor_ru-Index__block4-content.tensor_ru-Index__card')
    MORE_DETAILS_LINK = (By.CSS_SELECTOR, 'a.tensor_ru-link.tensor_ru-Index__link[href="/about"]')
    PHOTOS_BLOCK = (By.CSS_SELECTOR, 'div.tensor_ru-container.tensor_ru-section.tensor_ru-About__block3')
    PHOTOS = (By.CSS_SELECTOR, 'div.tensor_ru-container.tensor_ru-section.tensor_ru-About__block3 img')

    def verify_strength_in_people_block(self):
        assert self.is_element_present(self.STRENGTH_IN_PEOPLE_BLOCK)

    def click_more_details(self):
        more_details_link = self.wait.until(EC.visibility_of_element_located(self.MORE_DETAILS_LINK))
        self.browser.execute_script("arguments[0].scrollIntoView();", more_details_link)
        more_details_link.click()

    def verify_about_page(self):
        assert 'https://tensor.ru/about' in self.browser.current_url

    def verify_photos_dimensions(self):
        try:
            photos_block = self.wait.until(EC.presence_of_element_located(self.PHOTOS_BLOCK))
            photos = photos_block.find_elements(*self.PHOTOS)

            if not photos:
                self.logger.error("No photos found in the block")
                assert False, "No photos found in the block"

            dimensions = set()
            for photo in photos:
                height = photo.size['height']
                width = photo.size['width']
                dimensions.add((height, width))
                self.logger.info(f"Photo dimensions: {height}x{width}")

            if len(dimensions) != 1:
                self.logger.error(f"Not all photos have the same dimensions. Found dimensions: {dimensions}")

            assert len(dimensions) == 1, "Not all photos have the same dimensions"
        except Exception as e:
            self.logger.error(f"Error verifying photos dimensions: {e}")
            raise