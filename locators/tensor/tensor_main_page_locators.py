from selenium.webdriver.common.by import By


class TensorMainPageLocators(object):
    """Класс для локаторов главной страницы"""

    XPATH_DIV_POWER_IN_PPL = (By.XPATH, "//p[text()='Сила в людях']")

    XPATH_DIV_NEWS = (By.XPATH, "//div[@class='nl-LastCovers tensor_ru-Index__news']")

    XPATH_DETAILS_BUTTON = (By.XPATH, "(//a[@class='tensor_ru-link tensor_ru-Index__link'])[2]")