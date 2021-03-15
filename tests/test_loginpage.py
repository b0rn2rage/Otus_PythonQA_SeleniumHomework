import allure

from pages.LoginPage import LoginPage


@allure.title("Проверка наличия элементов на странице логина")
def test_loginpage(remote):
    login_page = LoginPage(remote)
    login_page.open_login_page()
    login_page.check_elements_on_login_page()
