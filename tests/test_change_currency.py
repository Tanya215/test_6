import time

from page_objects.firstpage import FirstPage


def test_change_currency(browser, url):
    browser.get(url)

    FirstPage.open_currency_dropdown(browser)
    time.sleep(2)
    # FirstPage.select_euro(browser)
    # FirstPage.check_selected_currency_euro(browser)
    #
    # FirstPage.open_currency_dropdown(browser)
    # FirstPage.select_pound(browser)
    # FirstPage.check_selected_currency_pound(browser)
    #
    # FirstPage.open_currency_dropdown(browser)
    # FirstPage.select_US_dollar(browser)
    # FirstPage.check_selected_currency_US_dollar(browser)
