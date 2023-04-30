from page_objects.basepage import BasePage
from selenium.webdriver.common.by import By
import time


class FirstPage(BasePage):

    def open_currency_dropdown(self):

        self.check_by_xpath("//span[text()='Currency']").click()
        # self.find_element(By.XPATH, "//span[text()='Currency']").click()

    def select_euro(self):
        self.find_element(By.CSS_SELECTOR, "button[name='EUR']").click()

    def check_selected_currency_euro(self):
        self.find_element(By.XPATH, "//strong[text()='€']")

    def select_pound(self):
        self.find_element(By.CSS_SELECTOR, "button[name='GBP']").click()

    def check_selected_currency_pound(self):
        self.find_element(By.XPATH, "//strong[text()='£']")

    def select_US_dollar(self):
        self.find_element(By.CSS_SELECTOR, "button[name='USD']").click()

    def check_selected_currency_US_dollar(self):
        self.find_element(By.XPATH, "//strong[text()='$']")