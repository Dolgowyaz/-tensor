from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
class MainPage(BasePage):
    DOWNLOAD_LINK = (By.CSS_SELECTOR, "#container > div.sbisru-Footer.sbisru-Footer__scheme--default > div.sbis_ru-container > div.sbisru-Footer__container > div:nth-child(3) > ul > li:nth-child(8) > a")

    def click_download_link(self):
        self.logger.info("Клик по ссылке 'Скачать локальные версии'")
        self.wait.until(EC.element_to_be_clickable(self.DOWNLOAD_LINK)).click()