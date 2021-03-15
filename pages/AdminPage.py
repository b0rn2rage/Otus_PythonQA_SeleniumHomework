import allure

from pages.BasePage import BasePage
from locators.AdminPageLocators import AdminPageLocators
from locators.CommonLocators import CommonLocators
from selenium.common.exceptions import TimeoutException


class AdminPage(BasePage):
    path = "/admin"

    @allure.step("Открыть страницу администратора")
    def open_admin_page(self):
        self.browser.get(self.url + self.path)

    @allure.step("Залогиниться в админку")
    def login_to_admin_page(self, username, password):
        input_username = self._wait_element_to_be_clickable(AdminPageLocators.LoginToAdminPage.INPUT_USERNAME)
        self._input_text(input_username, username)
        input_pass = self._wait_element_to_be_clickable(AdminPageLocators.LoginToAdminPage.INPUT_PASS)
        self._input_text(input_pass, password)
        login_button = self._find_elements(AdminPageLocators.LoginToAdminPage.LOGIN_BUTTON)[0]
        login_button.click()
        self._wait_element_to_be_presence(CommonLocators.WAIT_CONTAINER_LOAD)

    @allure.step("Сделать логаут из админки")
    def logout_from_admin_page(self):
        logout_button = self._find_elements(CommonLocators.LOGOUT_BUTTON)[0]
        logout_button.click()
        self._wait_element_to_be_presence(AdminPageLocators.LoginToAdminPage.LOGIN_BUTTON)

    @allure.step("Перейти в карточку последнего заказа")
    def go_to_the_last_order_card(self):
        latest_orders = self._find_elements(AdminPageLocators.Dashboard.VIEW_LATEST_ORDERS)
        latest_orders[0].click()
        self._wait_element_to_be_presence(CommonLocators.WAIT_CONTAINER_LOAD)

    @allure.step("Открыть окно с накладной")
    def go_to_print_shipping_list(self):
        print_shipping_list = self._find_elements(AdminPageLocators.LastOrderCard.PRINT_SHIPPING_LIST)[0]
        window_before = self.browser.window_handles[0]  # Сохранить текущее окно
        print_shipping_list.click()
        window_after = self.browser.window_handles[1]  # Сохранить новое окно с открывшейся накладной
        self.browser.switch_to.window(window_after)  # Свичнуться на окно с накладной

    @allure.step("Проверить наличие накладной")
    def check_dispatch(self):
        try:
            self._wait_element_to_be_presence(AdminPageLocators.Dispatch.CONTAINER)
            self._wait_element_to_be_presence(AdminPageLocators.Dispatch.DISPATCH_NOTE)
        except TimeoutException:
            self.logger.error("Dispatch is not displayed")
            raise AssertionError("Накладная не загрузилась")

    @allure.step("Перейти на страницу заказов из раздела sales")
    def go_to_sales_orders(self):
        sale = self._find_elements(AdminPageLocators.Dashboard.SALES)[0]
        sale.click()
        self._wait_element_to_be_clickable(AdminPageLocators.Dashboard.SECTIONS_IN_SALES)
        orders = self._find_elements(AdminPageLocators.Dashboard.SECTIONS_IN_SALES)[0]
        orders.click()

    @allure.step("Нажатие кнопки добавления нового заказа")
    def add_new_order(self):
        self._wait_element_to_be_presence(CommonLocators.WAIT_CONTAINER_LOAD)
        add_new_order = self._find_elements(AdminPageLocators.Orders.ADD_NEW_ORDER)[0]
        add_new_order.click()

    @allure.step("Проверить, что открылась форма для создания нового заказа")
    def check_new_order_form(self):
        try:
            self._wait_element_to_be_presence(CommonLocators.WAIT_CONTAINER_LOAD)
            self._wait_element_to_be_presence(AdminPageLocators.NewOrderCard.CUSTOMER_FIELD)
        except TimeoutException:
            self.logger.error("customer field is not displayed")
            raise AssertionError("Поле customer отсутствует на форме создания нового заказа")

    @allure.step("Проверить наличие элементов на странице администратора")
    def check_elements_on_admin_page(self):
        self._find_element(AdminPageLocators.LoginToAdminPage.INPUT_USERNAME)
        self._find_element(AdminPageLocators.LoginToAdminPage.INPUT_PASS)
        self._find_element(AdminPageLocators.LoginToAdminPage.LOGIN_BUTTON)
        self._find_element(AdminPageLocators.LoginToAdminPage.FORGOTTEN_PASSWORD)
        self._find_element(CommonLocators.GO_TO_HOMEPAGE)

    @allure.step("Перейти в каталог товаров")
    def go_to_catalog_products(self):
        catalog = self._find_elements(AdminPageLocators.Dashboard.MENU_CATALOG)[0]
        catalog.click()
        self._wait_element_to_be_clickable(AdminPageLocators.Dashboard.SECTIONS_IN_CATALOG)
        products = self._find_elements(AdminPageLocators.Dashboard.SECTIONS_IN_CATALOG)[1]
        products.click()

    @allure.step("Подождать загрузки страницы с товарами")
    def check_products_page(self):
        try:
            self._wait_element_to_be_presence(AdminPageLocators.Catalog.TABLE_WITH_PRODUCT_LIST)
        except TimeoutException:
            self.logger.error("Page with products not displayed")
            raise AssertionError("Страница с товарами не прогрузилась")
