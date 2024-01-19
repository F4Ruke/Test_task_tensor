from locators.sbis.sbis_main_page_locators import SbisMainPageLocators
from pages.sbis.sbis_download_page import SbisDownloadPage
from pages.sbis.sbis_contact_page import SbisContactPage
from selenium.common import WebDriverException
from pages.base_page import BasePage


class SbisMainPage(BasePage):
    """Класс с методами действий на главной странице сайта СБИС."""

    URL = "https://sbis.ru/"

    def __init__(self, driver):
        """Конструктор класса SbisMainPage.

        - driver - Окно браузера.
        """
        super().__init__(driver)

    def open_main_page(self):
        """Открывает главную страницу сайта 'СБИС'."""
        self.open_page(self.URL)
        return self

    def click_contact_button(self):
        """Нажимает на кнопку 'Контакты.'"""
        self.click_element(SbisMainPageLocators.XPATH_CONTACT_BUTTON)
        return SbisContactPage(self.driver)

    def click_download_button(self):
        """Нажимает на кнопку 'Скачать СБИС'."""
        self.click_element(SbisMainPageLocators.XPATH_DOWNLOAD_SBIS_BUTTON)
        return SbisDownloadPage(self.driver)
