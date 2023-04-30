from page_objects.adminpage import AdminPage
from page_objects.dashboardpage import DashboardPage
from page_objects.productspage import ProductsPage
from page_objects.alert import Alert
import time


def test_add_product(browser, url):
    url_builder = f"{url}/admin"
    browser.get(url_builder)
    # AdminPage.check_by_id(browser, "input-username").send_keys('user')
    # AdminPage.check_by_id(browser, "input-password").send_keys('bitnami')
    # time.sleep(1)
    # AdminPage.enter_username(browser, 'user')

    AdminPage.login_to_admin(browser)
    # time.sleep(1)
    # AdminPage.catalog_selection(browser)
    # time.sleep(1)
    # AdminPage.products_selection(browser)
    # time.sleep(1)
    DashboardPage.product_list_open(browser)
    # time.sleep(1)
    ProductsPage.add_new_product(browser)
    # time.sleep(1)
    ProductsPage.check_added_product(browser)
    # time.sleep(1)

    # Verify message and add to adding_new_product
    time.sleep(1)
    Alert.verify_success_product_update(browser)
    time.sleep(2)
