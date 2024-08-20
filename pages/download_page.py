from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class DownloadPage(BasePage):
    """
    Класс для работы со страницей загрузки.
    """

    DOWNLOAD_BUTTON = (By.XPATH, "//a[contains(text(), 'Скачать (Exe 11.05 МБ)')]")

    def click_download_button(self):
        """
        Нажатие кнопки загрузки.
        """
        self.logger.info("Нажатие кнопки загрузки")
        self.wait.until(EC.element_to_be_clickable(self.DOWNLOAD_BUTTON)).click()