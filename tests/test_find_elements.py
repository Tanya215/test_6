from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.basepage import BasePage
from page_objects.firstpage import FirstPage


# def test_main_page_title(browser, url):
#     browser.get(url)
#
    # assert browser.title == "Your Store"

    # WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.NAME, "search")))
    # BasePage.check_by_name(browser, "search")

    # # WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.XPATH, "//h3[text()='Featured']")))
    # BasePage.check_by_xpath(browser, "//h3[text()='Featured']")
    #
    # # WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[data-original-title"
    # #                                                                                    "='Add to Wish List']")))
    # BasePage.check_by_css(browser, "button[data-original-title='Add to Wish List']")
    #
    # # WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[data-original-title"
    # #                                                                                    "='Compare this Product']")))
    # BasePage.check_by_css(browser, "button[data-original-title='Compare this Product']")
    #
    # WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.ID, "logo")))
    # BasePage.check_by_id(browser, "logo")


def test_catalog_title(browser, url):
    url_builder = f"{url}/desktops"
    browser.get(url_builder)
#     assert browser.title == "Desktops"
#     # WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.ID, "list-view")))
#     BasePage.check_by_id(browser, "list-view")
#     # WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.ID, "grid-view")))
#     BasePage.check_by_id(browser, "grid-view")
#     # WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.LINK_TEXT, "Product Compare (0)")))
#     BasePage.check_by_link(browser, "Product Compare (0)")
#     # WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.XPATH, "//label[text()='Sort By:']")))
#     BasePage.check_by_xpath(browser, "//label[text()='Sort By:']")
#     # WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.XPATH, "//label[text()='Show:']")))
    BasePage.check_by_xpath(browser, "//label[text()='Show:']")
# #
#
# def test_product_card_title(browser, url):
#     url_builder = f"{url}/macbook"
#     browser.get(url_builder)
#     assert browser.title == "MacBook"
#     # WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.XPATH, "//*[@data-original-title='Add to Wish List']")))
#     BasePage.check_by_xpath(browser, "//*[@data-original-title='Add to Wish List']")
#     # WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.XPATH, "//*[@data-original-title='Compare this Product']")))
#     BasePage.check_by_xpath(browser, "//*[@data-original-title='Compare this Product']")
#     # WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.XPATH, "//label[text()='Qty']")))
#     BasePage.check_by_xpath(browser, "//label[text()='Qty']")
#     # WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.ID, "button-cart")))
#     BasePage.check_by_id(browser, "button-cart")
#     # WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.NAME, "quantity")))
#     BasePage.check_by_name(browser, "quantity")
#
#
# def test_admin_page_title(browser, url):
#     url_builder = f"{url}/admin"
#     browser.get(url_builder)
#     assert browser.title == "Administration"
#     # WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.LINK_TEXT, "OpenCart")))
#     BasePage.check_by_link(browser, "OpenCart")
#     # WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.LINK_TEXT, "Forgotten Password")))
#     BasePage.check_by_link(browser, "Forgotten Password")
#     # WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.XPATH, "//label[text()='Username']")))
#     BasePage.check_by_xpath(browser, "//label[text()='Username']")
#     # WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.XPATH, "//label[text()='Password']")))
#     BasePage.check_by_xpath(browser, "//label[text()='Password']")
#     # WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.XPATH, "//h1[text()=' Please enter your login details.']")))
#     BasePage.check_by_xpath(browser, "//h1[text()=' Please enter your login details.']")
#
#
# def test_register_page_title(browser, url):
#     url_builder = f"{url}/index.php?route=account/register"
#     browser.get(url_builder)
#     assert browser.title == "Register Account"
#     # WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[value='Continue']")))
#     BasePage.check_by_css(browser, "input[value='Continue']")
#     # WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.LINK_TEXT, "Privacy Policy")))
#     BasePage.check_by_link(browser, "Privacy Policy")
#     # WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.LINK_TEXT, "login page")))
#     BasePage.check_by_link(browser, "login page")
#     # WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='firstname']")))
#     BasePage.check_by_css(browser, "input[name='firstname']")
#     # WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.ID, "input-lastname")))
#     BasePage.check_by_id(browser, "input-lastname")
#