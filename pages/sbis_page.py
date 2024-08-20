from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SBISPage(BasePage):
    CONTACTS_LINK = (By.LINK_TEXT, "Контакты")
    TENSOR_BANNER = (By.CSS_SELECTOR, "img[alt='Разработчик системы СБИС — компания «Тензор»']")

    def navigate_to_contacts(self):
        self.click_element(self.CONTACTS_LINK)

    def click_tensor_banner(self):
        self.click_element(self.TENSOR_BANNER)
        self.browser.switch_to.window(self.browser.window_handles[-1])  # Переключение на новую вкладку