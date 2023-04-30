from page_objects.adminpage import AdminPage
from page_objects.dashboardpage import DashboardPage
from page_objects.customerspage import CustomersPage
from page_objects.alert import Alert
import time


def test_delete_user(browser, url):
    url_builder = f"{url}/admin"
    browser.get(url_builder)

    AdminPage.login_to_admin(browser)

    DashboardPage.customer_list_open(browser)

    CustomersPage.check_added_customer(browser)

    CustomersPage.select_customer(browser)

    CustomersPage.delete_selected_customer(browser)

    Alert.confirm_alert(browser)

    Alert.verify_success_customer_update(browser)
