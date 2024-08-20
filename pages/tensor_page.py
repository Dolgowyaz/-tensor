from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import logging

class TensorPage(BasePage):
    STRENGTH_IN_PEOPLE_BLOCK = (By.CSS_SELECTOR, 'div.tensor_ru-Index__block4-content.tensor_ru-Index__card')
    MORE_DETAILS_LINK = (By.CSS_SELECTOR, 'a.tensor_ru-link.tensor_ru-Index__link[href="/about"]')
    PHOTOS_BLOCK = (By.CSS_SELECTOR, 'div.tensor_ru-container.tensor_ru-section.tensor_ru-About__block3')
    PHOTOS = (By.CSS_SELECTOR, 'div.tensor_ru-container.tensor_ru-section.tensor_ru-About__block3 img')

    def __init__(self, browser):
        super().__init__(browser)
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch = logging.StreamHandler()
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

    def verify_strength_in_people_block(self):
        self.logger.info("Проверка наличия блока 'Сила в людях'")
        assert self.is_element_present(self.STRENGTH_IN_PEOPLE_BLOCK), "Блок 'Сила в людях' не найден"

    def click_more_details(self):
        self.logger.info("Клик по ссылке 'Подробнее'")
        more_details_link = self.wait.until(EC.visibility_of_element_located(self.MORE_DETAILS_LINK))
        self.browser.execute_script("arguments[0].scrollIntoView();", more_details_link)
        more_details_link.click()

    def verify_about_page(self):
        self.logger.info("Проверка URL страницы 'О компании'")
        assert 'https://tensor.ru/about' in self.browser.current_url, "Страница 'О компании' не открыта"

    def verify_photos_dimensions(self):
        self.logger.info("Проверка размеров фотографий в блоке")
        try:
            photos_block = self.wait.until(EC.presence_of_element_located(self.PHOTOS_BLOCK))
            photos = photos_block.find_elements(*self.PHOTOS)

            if not photos:
                self.logger.error("Фотографии в блоке не найдены")
                assert False, "Фотографии в блоке не найдены"

            dimensions = set()
            for photo in photos:
                height = photo.size['height']
                width = photo.size['width']
                dimensions.add((height, width))
                self.logger.info(f"Размеры фото: {height}x{width}")

            if len(dimensions) != 1:
                self.logger.error(f"Не все фотографии имеют одинаковые размеры. Найденные размеры: {dimensions}")

            assert len(dimensions) == 1, "Не все фотографии имеют одинаковые размеры"
        except Exception as e:
            self.logger.error(f"Ошибка при проверке размеров фотографий: {e}")
            raise