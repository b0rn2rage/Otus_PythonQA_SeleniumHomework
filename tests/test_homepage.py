from locators.HomePage import HomePage


def test_homepage(browser, open_opencart_homepage):
    browser.get(open_opencart_homepage)
    browser.find_element(*HomePage.CURRENCY)
    browser.find_element(*HomePage.MY_ACCOUNT)
    browser.find_element(*HomePage.WISH_LIST)
    browser.find_element(*HomePage.SHOPPING_CART)
    browser.find_element(*HomePage.CHECKOUT)

