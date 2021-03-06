from pages.LoginPage import LoginPage


def test_loginpage(remote):
    login_page = LoginPage(remote)
    login_page.open_login_page()
    login_page.check_elements_on_login_page()
