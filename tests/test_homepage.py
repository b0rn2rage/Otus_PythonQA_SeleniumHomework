import allure

from pages.HomePage import HomePage


@allure.title("Проверка наличия элементов на домашней странице")
def test_homepage(remote):
    home_page = HomePage(remote)
    home_page.open_home_page()
    home_page.check_elements_on_home_page()
