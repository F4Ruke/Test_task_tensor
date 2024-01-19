from locators.tensor.tensor_main_page_locators import TensorMainPageLocators
from pages.tensor.tensor_about_page import TensorAboutPage
from pages.base_page import BasePage


class TensorMainPage(BasePage):
    """Класс с методами действий на главной странице сайта 'Тензор'."""

    URL = "https://tensor.ru/"

    def __init__(self, driver):
        """Конструктор класса TensorMainPage.

        - driver - Окно браузера.
        """
        super().__init__(driver)

    def click_details_button(self):
        """Проверяет есть ли блок описания и если есть, то переходит на страницу подробного описания."""
        self.move_to_element(TensorMainPageLocators.XPATH_DIV_NEWS)
        self.click_element(TensorMainPageLocators.XPATH_DETAILS_BUTTON)
        return TensorAboutPage(self.driver)
