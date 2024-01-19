from locators.tensor.tensor_about_page_locators import TensorAboutPageLocators
from locators.tensor.tensor_main_page_locators import TensorMainPageLocators
from locators.sbis.sbis_contact_page_locators import SbisContactPageLocators
from locators.sbis.sbis_main_page_locators import SbisMainPageLocators
from pages.tensor.tensor_about_page import TensorAboutPage
from pages.sbis.sbis_contact_page import SbisContactPage
from pages.sbis.sbis_main_page import SbisMainPage
from config.conftest import browser
from loguru import logger


def test_case_1(browser):
    """Первый сценарий Тех. Задания."""
    logger.info(f"Запуск теста.")

    assert (
        SbisMainPage(browser)
        .open_main_page()
        .click_contact_button()
        .click_tensor_banner()
        .is_display_element(TensorMainPageLocators.XPATH_DIV_POWER_IN_PPL)
        .click_details_button()
        .is_current_url(TensorAboutPage.URL)
        .is_display_element(TensorAboutPageLocators.XPATH_DIV_WORKING)
        .is_all_img_same_size()
    )


def test_case_2(browser):
    """Второй сценарий Тех. Задания."""
    logger.info(f"Запуск теста: {test_case_2.__name__}")

    assert (
        SbisMainPage(browser)
        .open_main_page()
        .click_contact_button()
        .is_change_region()
        .is_list_partner()
        .click_change_region_button()
        .click_new_region_button(SbisContactPageLocators.XPATH_REGION_KAMCHATKA)
        .is_change_region()
        .is_text_in_element(SbisContactPageLocators.ID_CITY, SbisContactPage.KAMCHATKA_REGION)
        .is_change_list_partner()
        .is_region_in_url()
        .is_region_in_title()
    )


def test_case_3(browser):
    """Третий сценарий Тех. Задания."""
    logger.info(f"Запуск теста: {test_case_3.__name__}")

    assert (
        SbisMainPage(browser)
        .open_main_page()
        .move_to_element(SbisMainPageLocators.XPATH_UNDER_FOOTER)
        .click_download_button()
        .open_plugin_page()
        .click_download_web()
        .is_plugin_for_win_download()
        .is_size_file_equals()
    )
