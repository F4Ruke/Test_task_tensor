from selenium.webdriver.common.by import By


class TensorAboutPageLocators(object):
    """Класс для локаторов страницы описания."""

    XPATH_DIV_WORKING = (By.XPATH, "//div[@class='tensor_ru-container tensor_ru-section tensor_ru-About__block3']")

    XPATH_DIV_LEARNING = (By.XPATH, "//div[@class='tensor_ru-About__block-bg tensor_ru-About__block4-bg']")

    XPATH_IMG_WORKING = (By.XPATH, "//img[@class='tensor_ru-About__block3-image new_lazy loaded']")

