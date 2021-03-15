import allure

from pages.BasePage import BasePage
from locators.HomePageLocators import HomePageLocators


class HomePage(BasePage):

    @allure.step("Открыть домашнюю страницу")
    def open_home_page(self):
        self.browser.get(self.url)

    @allure.step("Проверить наличие элементов на домашней странице")
    def check_elements_on_home_page(self):
        self._find_element(HomePageLocators.CHECKOUT)
        self._find_element(HomePageLocators.SHOPPING_CART)
        self._find_element(HomePageLocators.WISH_LIST)
        self._find_element(HomePageLocators.MY_ACCOUNT)
        self._find_element(HomePageLocators.CURRENCY)
