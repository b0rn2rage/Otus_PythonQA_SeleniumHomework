def test_first(browser, open_opencart_homepage):
    browser.get(open_opencart_homepage)
    assert browser.current_url == open_opencart_homepage, \
        f"В браузере открылась страница != {open_opencart_homepage}"
