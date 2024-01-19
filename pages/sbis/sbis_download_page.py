from locators.sbis.sbis_download_page_locators import SbisDownloadPageLocators
from pages.base_page import BasePage
from os import stat, getcwd
from loguru import logger
from time import sleep
from re import search


class SbisDownloadPage(BasePage):
    """Класс с методами действий на главной странице сайта СБИС."""

    URL_ELEPORT = "https://sbis.ru/download?tab=ereport&innerTab=ereport25"
    URL_PLUGIN = "https://sbis.ru/download?tab=plugin&innerTab=default"
    FILE_NAME_WEB_PLUGIN_FOR_WIN = "sbisplugin-setup-web.exe"

    file_size_on_page: float
    download_file_size: float

    def __init__(self, driver):
        """Конструктор класса SbisDownloadPage.

        - driver - Окно браузера.
        """
        super().__init__(driver)

    def open_plugin_page(self):
        """Нажимает на кнопку 'СБИС Плагин'."""
        self.open_page(self.URL_PLUGIN)
        return self

    def click_download_web(self):
        """Нажимает кнопку скачать Веб-установщик."""
        self.file_size_on_page = float(search(r'\d+\.\d+', self.find(SbisDownloadPageLocators.XPATH_DOWNLOAD_WEB)
                                              .text).group())
        self.click_element(SbisDownloadPageLocators.XPATH_DOWNLOAD_WEB)
        return self

    def is_plugin_for_win_download(self, time_out: int = 1):
        """Проверяет, скачался ли файл.

        - time_out - Время в секундах между проверками на завершенность скачивания файла.
        По умолчания time_out равняется 1 секунде.
        """
        try:
            self.download_file_size = stat(fr'{getcwd()}\{self.FILE_NAME_WEB_PLUGIN_FOR_WIN}').st_size
            logger.info(f"Файл: {self.FILE_NAME_WEB_PLUGIN_FOR_WIN} - скачался.")
            return self
        except FileNotFoundError:
            logger.info(f"Файл: {self.FILE_NAME_WEB_PLUGIN_FOR_WIN} - не скачался.")
            sleep(time_out)
            return self.is_plugin_for_win_download()

    def is_size_file_equals(self):
        """Проверяет, совпадает ли размер скаченного файла с размером указанном на странице."""
        if round(self.download_file_size / 1024 ** 2, 2) == self.file_size_on_page:
            logger.info("Размер скаченного файла равняет размеру указанном на сайте.")
        else:
            logger.info("Размер скаченного файла не равняет размеру указанном на сайте.")

        return self
