from locators.sbis.sbis_contact_page_locators import SbisContactPageLocators
from pages.tensor.tensor_main_page import TensorMainPage
from pages.base_page import BasePage
from loguru import logger
from re import search
import pytest


class SbisContactPage(BasePage):
    """Класс с методами действий на странице контактов сайта СБИС"""

    MY_REGION = "Калининградская обл."
    KAMCHATKA_REGION = "Петропавловск-Камчатский"

    list_partner: list
    number_region: str

    def __init__(self, driver):
        """Конструктор класса SbisContactPage.

        - driver - Окно браузера.
        """
        super().__init__(driver)

    def click_tensor_banner(self):
        """Нажимает на банер 'Тензор' и переходит на сайт 'https://tensor.ru/'."""
        self.click_element(SbisContactPageLocators.XPATH_TENSOR_BANNER).switch_to_window_handles(2)
        return TensorMainPage(self.driver)

    def click_change_region_button(self):
        """Нажимает на кнопку смены региона."""
        self.click_element(SbisContactPageLocators.XPATH_CHANGE_CITY_BUTTON)
        return self

    def click_new_region_button(self, locator: tuple[str, str]):
        """Нажимает на выбранный регион по локатору, а также записывает номер региона
        в атрибут 'number_region' класса 'SbisContactPage'.

        - locator - Кортеж состоящий из типа локатора, и самого локатора.
        Пример: (By.XPATH, //img[@class='img'])
        """
        self.number_region = search(r'\d{2}', self.find(locator).text).group()
        self.click_element(locator)
        return self

    def is_change_region(self):
        """Проверяет, изменился ли регион."""
        region = self.find(SbisContactPageLocators.XPATH_CHANGE_CITY_BUTTON).text

        if region == self.MY_REGION:
            logger.info(f"Установлен домашний регион: {self.MY_REGION}")
        else:
            logger.info(f"Регион изменился c {self.MY_REGION} на {region}")
        return self

    def is_list_partner(self):
        """Проверяет наличие списка партнеров."""
        temp_list_partner = [element.text for element in self.find_all(SbisContactPageLocators.XPATH_LIST_PARTNER)]

        if len(temp_list_partner) > 1:
            self.list_partner = temp_list_partner
            logger.info(f"Список партнеров не пуст.")
        else:
            logger.info(f"Список партнеров пуст.")

        return self

    def is_change_list_partner(self):
        """Проверяет, изменился ли список партнеров."""
        temp_list_partner = [element.text for element in self.find_all(SbisContactPageLocators.XPATH_LIST_PARTNER)]

        if temp_list_partner != self.list_partner:
            logger.info("Список партнеров изменился.")
            return self

        logger.error("Список партнеров не изменился.")
        self.driver.close()
        pytest.fail()

    def is_region_in_url(self):
        """Проверяет, присутствует ли информация о регионе в ссылке страницы."""
        if self.number_region in self.driver.current_url:
            logger.info(f"В ссылке: {self.driver.current_url} есть информация о регионе.")
            return self

        logger.error(f"В ссылке: {self.driver.current_url} нет информации о регионе.")
        self.driver.close()
        pytest.fail()

    def is_region_in_title(self):
        """Проверяет, присутствует ли информация о регионе во вкладке страницы."""
        region = self.find(SbisContactPageLocators.XPATH_CHANGE_CITY_BUTTON).text

        if region in self.driver.title:
            logger.info(f"Во вкладке содержится информация о регионе: {region}.")
            return self

        logger.error(f"Во вкладке не содержится информация о регионе: {region}.")
        self.driver.close()
        pytest.fail()
