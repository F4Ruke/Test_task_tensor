from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver
from loguru import logger
import inspect
import pytest
import os

logger.remove()
logger.add(f"../logs/debug.log", format="<level>[{level}]</level> {time:HH:mm:ss} {name}"
                                        " : {function} : {line} - <level>{message}</level>")


@pytest.fixture()
def browser() -> WebDriver:
    """Добавляет настройки и возвращает Хром драйвер."""
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": f"{os.getcwd()}",
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })
    chrome_driver = webdriver.Chrome(options=chrome_options)
    chrome_driver.maximize_window()
    chrome_driver.implicitly_wait(10)
    return chrome_driver
