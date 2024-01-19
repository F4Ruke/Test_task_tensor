from selenium.webdriver.common.by import By


class SbisDownloadPageLocators(object):
    """Класс для локаторов главной страницы"""

    XPATH_SBIS_PLUGIN = (By.XPATH, "//div[text()='СБИС Плагин']")

    XPATH_WINDOWS = (By.XPATH, "//span[text()='Windows']")

    XPATH_DOWNLOAD_WEB = (By.XPATH, "//a[@href='https://update.sbis.ru/Sbis3Plugin/master/win32/"
                                    "sbisplugin-setup-web.exe']")