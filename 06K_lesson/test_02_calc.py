
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
waiter = WebDriverWait(driver, 50, 0.01)


def test_calculator():
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    driver.find_element(By.ID, "delay").clear()
    driver.find_element(By.ID, "delay").send_keys("45")
    keys = driver.find_element(By.CLASS_NAME, "keys")
    buttons = keys.find_elements(By.TAG_NAME, "span")
    buttons[0].click()
    buttons[3].click()
    buttons[1].click()
    buttons[14].click()
    waiter.until(
        EC.invisibility_of_element_located((By.ID, "spinner")))

    assert driver.find_element(By.CLASS_NAME, "screen").text == "15"
    driver.quit()
