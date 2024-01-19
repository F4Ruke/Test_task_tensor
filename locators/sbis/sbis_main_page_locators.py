from selenium.webdriver.common.by import By


class SbisMainPageLocators(object):
    """Класс для локаторов главной страницы"""

    XPATH_CONTACT_BUTTON = (By.XPATH, "//li[@class='sbisru-Header__menu-item sbisru-Header__menu-item-1 mh-8  s-Grid--"
                                      "hide-sm']")

    XPATH_DOWNLOAD_SBIS_BUTTON = (By.XPATH, "//a[text()='Скачать СБИС']")

    XPATH_UNDER_FOOTER = (By.XPATH, "//div[@class='pt-40 pt-md-16 pt-sm-20']")
