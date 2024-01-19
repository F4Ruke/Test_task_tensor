from selenium.webdriver.common.by import By


class SbisContactPageLocators(object):
    """Класс для локаторов страницы контактов"""

    ID_CITY = (By.ID, "city-id-2")

    XPATH_TENSOR_BANNER = (By.XPATH, "//a[@class='sbisru-Contacts__logo-tensor mb-12']")

    XPATH_LIST_PARTNER = (By.XPATH, "//div[@class='sbisru-Contacts-List__name sbisru-Contacts-List--ellipsis sbisru-"
                                    "Contacts__text--md pb-4 pb-xm-12 pr-xm-32']")

    XPATH_CHANGE_CITY_BUTTON = (By.XPATH, "//span[@class='sbis_ru-Region-Chooser ml-16 ml-xm-0']"
                                          "//span[@class='sbis_ru-Region-Chooser__text sbis_ru-link']")

    XPATH_REGION_KAMCHATKA = (By.XPATH, "//span[@title='Камчатский край']")
