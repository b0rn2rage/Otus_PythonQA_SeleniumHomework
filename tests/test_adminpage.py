import allure

from pages.AdminPage import AdminPage


@allure.title("Проверка элементов на странице администратора")
def test_adminpage(remote):
    admin_page = AdminPage(remote)
    admin_page.open_admin_page()
    admin_page.check_elements_on_admin_page()


@allure.title("Проверка наличия накладной на товар")
def test_open_print_shipping_list(remote, config):
    admin_page = AdminPage(remote)
    admin_page.open_admin_page()
    admin_page.login_to_admin_page(username=config['admin-auth']['username'], password=config['admin-auth']['password'])
    admin_page.go_to_the_last_order_card()
    admin_page.go_to_print_shipping_list()
    admin_page.check_dispatch()


@allure.title("Открытие формы для создания нового заказа")
def test_open_add_new_order_form(remote, config):
    admin_page = AdminPage(remote)
    admin_page.open_admin_page()
    admin_page.login_to_admin_page(username=config['admin-auth']['username'], password=config['admin-auth']['password'])
    admin_page.go_to_sales_orders()
    admin_page.add_new_order()
    admin_page.check_new_order_form()


@allure.title("Логин/логаут со страницы администратора")
def test_login_logout(remote, config):
    admin_page = AdminPage(remote)
    admin_page.open_admin_page()
    admin_page.login_to_admin_page(username=config['admin-auth']['username'], password=config['admin-auth']['password'])
    admin_page.logout_from_admin_page()


@allure.title("Открытие страницы товаров")
def test_open_product_page(browser, config):
    admin_page = AdminPage(browser)
    admin_page.open_admin_page()
    admin_page.login_to_admin_page(username=config['admin-auth']['username'], password=config['admin-auth']['password'])
    admin_page.go_to_catalog_products()
    admin_page.check_products_page()
