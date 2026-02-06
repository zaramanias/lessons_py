
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:
    def __init__(self, driver):
        self.driver = driver
        self.waiter = WebDriverWait(self.driver, 50, 0.01)
        self.first_number = None
        self.operator = None
        self.second_number = None

    def open(self):
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html")

    def set_delay(self, delay):
        self.driver.find_element(By.ID, "delay").clear()
        self.driver.find_element(By.ID, "delay").send_keys(delay)

    def click_button(self, symbol):
        keys = self.driver.find_element(By.CSS_SELECTOR, "div.keys")
        buttons = keys.find_elements(By.TAG_NAME, "span")
        for button in buttons:
            if button.text == symbol:
                button.click()
                if symbol.isdigit():
                    if self.first_number is None:
                        self.first_number = symbol
                    else:
                        self.second_number = symbol
                if symbol in ['+', '-', 'x', '÷']:
                    self.operator = symbol

                return
        raise Exception(f"Button with symbol {symbol} not found")

    def wait_spinner(self):
        self.waiter.until(
            EC.invisibility_of_element_located((By.ID, "spinner")))

    def get_result(self):
        return self.driver.find_element(By.CLASS_NAME, "screen").text

    def calculate(self):
        a = int(self.first_number)
        b = int(self.second_number)
        if self.operator == '+':
            return a + b
        elif self.operator == '-':
            return a - b
        elif self.operator == 'x':
            return a * b
        elif self.operator == '÷':
            return a // b

        raise Exception(f"Unknown operator {self.operator}")
