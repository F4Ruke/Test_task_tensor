from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.common import TimeoutException, WebDriverException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.webdriver import WebDriver
from loguru import logger
import pytest


class BasePage(object):
    """Базовый класс для инициализации базовой страницы, который будет вызываться во всех страницах."""
    def __init__(self, driver: WebDriver):
        """Конструктор класса BasePage.

        - driver - Окно браузера.
        """
        self.driver = driver

    def open_page(self, url: str):
        """Открывает страницу"""
        try:
            self.driver.get(url)
            logger.info(f"Открылся сайт: {url}.")
            return self
        except WebDriverException:
            logger.error(f"Сайт {url} не открылся.")
            self.driver.close()
            pytest.fail()

    def find(self, locator: tuple[str, str]) -> WebElement:
        """Проверяет наличия указанного локатора и находит его.

        - locator - Кортеж состоящий из типа локатора, и самого локатора.
        Пример: (By.XPATH, //img[@class='img'])
        """
        if self.is_display_element(locator):
            return self.driver.find_element(*locator)

    def find_all(self, locator: tuple[str, str]) -> list[WebElement]:
        """Проверяет наличия указанного локатора и находит все элементы.

        - locator - Кортеж состоящий из типа локатора, и самого локатора.
        Пример: (By.XPATH, //img[@class='img'])
        """
        if self.is_display_element(locator):
            return self.driver.find_elements(*locator)

    def click_element(self, locator: tuple[str, str]):
        """Нажимает на указанный элемент по локатору.

        - locator - Кортеж состоящий из типа локатора, и самого локатора.
        Пример: (By.XPATH, //img[@class='img'])
        """
        self.find(locator).click()
        logger.info(f"Нажали по элементу: {locator[0]} - {locator[1]}.")
        return self

    def switch_to_window_handles(self, number: int = 1):
        """Изменяет активную вкладку.

        - number - Номер вкладки (отчет начинает с 1).

        P.S. Если, количество вкладок равняется 1 или 1 >= number, или number > количества вкладок, то
        активной вкладкой станет первая.
        """
        if len(self.driver.window_handles) > 1 and 1 < number <= len(self.driver.window_handles):
            self.driver.switch_to.window(self.driver.window_handles[number - 1])
            logger.info(f"Выбрали вкладку под номером: {number}.")
        else:
            self.driver.switch_to.window(self.driver.window_handles[0])
            logger.info(f"Выбрали вкладку под номером: 1.")

        return self

    def move_to_element(self, locator: tuple[str, str]):
        """Проверяет наличия указанного локатора и перемещается к нему.

        - locator - Кортеж состоящий из типа локатора, и самого локатора.
        Пример: (By.XPATH, //img[@class='img'])
        """
        ActionChains(self.driver).move_to_element(self.find(locator)).perform()
        logger.info(f"Двигаемся к элементу: {locator[0]} - {locator[1]}.")
        return self

    def is_display_element(self, locator: tuple[str, str], time: int = 5):
        """Ожидает появление элемента по локатору, если находит, возвращает объект, если не находит,
        возвращает None.

        - locator - Кортеж состоящий из типа локатора, и самого локатора.
        Пример: (By.XPATH, //img[@class='img'])
        - time - Время ожидания появления элемента, по умолчанию 5 секунд.
        """
        try:
            WebDriverWait(self.driver, time).until(ec.presence_of_element_located(locator))
            logger.info(f"Локатор: {locator[0]} - {locator[1]} найден.")
            return self
        except TimeoutException:
            logger.error(f"Локатор: {locator[0]} - {locator[1]} не найден.")
            self.driver.close()
            pytest.fail()

    def is_text_in_element(self, locator: tuple[str, str], text: str, time: int = 5):
        """Ожидает появление текста в указанном локаторе, если находит, возвращает объект,
        если не находит, возвращает None.

        - locator - Кортеж состоящий из типа локатора, и самого локатора.
        Пример: (By.XPATH, //img[@class='img'])
        - text - Текст.
        - time - Время ожидания появления элемента, по умолчанию 5 секунд.
        """
        try:
            WebDriverWait(self.driver, time).until(ec.text_to_be_present_in_element(locator, text))
            logger.info(f"Локатор: {locator[0]} - {locator[1]} найден.")
            return self
        except TimeoutException:
            logger.error(f"Локатор: {locator[0]} - {locator[1]} не найден.")
            self.driver.close()
            pytest.fail()

    def is_current_url(self, url: str):
        """Проверяет совпадение URL.

        - url - Ссылка страницы.
        Пример: https://tensor.ru/
        """
        if self.driver.current_url == url:
            logger.info(f"Ссылка страницы: {url} - совпадает.")
        else:
            logger.info(f"Ссылка: {url} - изменилась на: {self.driver.current_url}.")
        return self
