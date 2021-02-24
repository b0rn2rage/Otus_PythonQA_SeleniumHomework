from pages.HomePage import HomePage


def test_homepage(browser):
    home_page = HomePage(browser)
    home_page.open_home_page()
    home_page.check_elements_on_home_page()
