from page_objects.firstpage import FirstPage
from page_objects.registerpage import RegisterPage

import time


def test_add_product(browser, url):
    browser.get(url)

    FirstPage.go_to_register(browser)


    RegisterPage.enter_user_data(browser)


    RegisterPage.submit_new_user(browser)


    RegisterPage.verify_user_creation(browser)
