from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.basepage import BasePage
import time


class AdminPage:
    # def __init__(self, browser):
    #     self.browser, self.url = browser
    #     self.driver = self.browser
    #     self.browser.get(self.url + '/admin')

    def enter_username(self, username):
        self.find_element(By.ID, "input-username").send_keys(username)
        # self.check_by_id("input-username").send_keys(username)

    def enter_password(self, password):
        self.check_by_id("input-password").send_keys(password)

    def login_to_admin(self):
        self.find_element(By.ID, "input-username").send_keys("user")
        self.find_element(By.ID, "input-password").send_keys("bitnami")
        self.find_element(By.XPATH, "//button[text()=' Login']").click()

        # self.enter_username("user")
        # self.enter_password("bitnami")
        # self.check_by_css("#input[value=Login]]").click()

    # def catalog_selection(self):
    #     self.find_element(By.XPATH, "//a[text()=' Catalog']").click()
    #
    #
    # def products_selection(self):
    #     self.find_element(By.XPATH, "//a[text()='Products']").click()

    # def product_list_open(self):
    #     self.find_element(By.XPATH, "//a[text()=' Catalog']").click()
    #     WebDriverWait(self, 1).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Products']"))).click()
    #     # self.find_element(By.XPATH, "//a[text()='Products']").click()

    # def add_new_product(self):
    #     self.find_element(By.CSS_SELECTOR, "a[data-original-title='Add New']").click()
    #     time.sleep(1)
    #     self.find_element(By.ID, "input-name1").send_keys("1Product_test")
    #     time.sleep(1)
    #     self.find_element(By.ID, "input-meta-title1").send_keys("Product_meta_tag")
    #     time.sleep(1)
    #     self.find_element(By.LINK_TEXT, "Data").click()
    #     time.sleep(1)
    #     self.find_element(By.ID, "input-model").send_keys("Product_model")
    #     time.sleep(1)
    #     self.find_element(By.CSS_SELECTOR, "button[data-original-title='Save']").click()
    #
    # def check_added_product(self):
    #     WebDriverWait(self, 1).until(EC.visibility_of_element_located((By.XPATH, "//td[text()='1Product_test']")))