
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShopPage:
    def __init__(self, driver):
        self.driver = driver
        self.waiter = WebDriverWait(self.driver, 10, 0.01)

    def open(self):
        self.driver.get("https://www.saucedemo.com")

    def login(self, username, password):
        self.waiter.until(EC.visibility_of_element_located((
            By.ID, "user-name"))).send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

    def add_to_cart(self):
        self.waiter.until(EC.element_to_be_clickable((
            By.ID, "add-to-cart-sauce-labs-backpack"))).click()
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-onesie").click()
