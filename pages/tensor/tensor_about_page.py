from locators.tensor.tensor_about_page_locators import TensorAboutPageLocators
from pages.base_page import BasePage
from loguru import logger
import pytest

class TensorAboutPage(BasePage):
    """Класс с методами действий на главной странице"""

    URL = "https://tensor.ru/about"

    def __init__(self, driver):
        """Конструктор класса TensorAboutPage.

        - driver - Окно браузера.
        """
        super().__init__(driver)

    def is_all_img_same_size(self):
        """Проверяет все ли изображения в блоке 'Работаем' одинакового размера."""
        self.move_to_element(TensorAboutPageLocators.XPATH_DIV_LEARNING)

        size = [[element.get_attribute("width"), element.get_attribute("height")]
                for element in self.find_all(TensorAboutPageLocators.XPATH_IMG_WORKING)]

        if size.count(size[0]) == len(size):
            logger.info("Все изображения одинакового размера.")
            return self

        logger.error("Одно или более изображений другого размера.")
        self.driver.close()
        pytest.fail()
