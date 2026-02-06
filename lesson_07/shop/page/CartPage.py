
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.waiter = WebDriverWait(self.driver, 10, 0.01)

    def go_to_cart(self):
        self.driver.get("https://www.saucedemo.com/cart.html")

    def checkout(self):
        self.waiter.until(EC.element_to_be_clickable((
            By.ID, "checkout"))).click()

    def fill_checkout_info(self, first_name, last_name, postal_code):
        self.waiter.until(EC.visibility_of_element_located((
            By.ID, "first-name"))).send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self.driver.find_element(By.ID, "continue").click()
        self.waiter.until(
            EC.visibility_of_element_located((
                By.CLASS_NAME, "summary_total_label")))

    def get_result(self):
        return self.driver.find_element(
            By.CLASS_NAME, "summary_total_label").text
