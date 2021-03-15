import allure

from pages.BasePage import BasePage
from locators.CatalogPageLocators import CatalogPageLocators


class CatalogPage(BasePage):
    path = "/index.php?route=product/category&path=20"

    @allure.step("Открыть страницу с каталогом")
    def open_catalog_page(self):
        self.browser.get(self.url + self.path)

    @allure.step("Проверить наличие элементов на странице с каталогом")
    def check_elements_on_catalog_page(self):
        self._find_element(CatalogPageLocators.MENU_SOFTWARE)
        self._find_element(CatalogPageLocators.MENU_TABLETS)
        self._find_element(CatalogPageLocators.MENU_COMPONENTS)
        self._find_element(CatalogPageLocators.MENU_LAPTOPS_AND_NOTEBOOKS)
        self._find_element(CatalogPageLocators.MENU_DESKTOPS)
