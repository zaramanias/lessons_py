from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge()
waiter = WebDriverWait(driver, 10, 0.01)

GREEN_FIELDS_IDS = [
    "first-name",
    "last-name",
    "address",
    "city",
    "country",
    "e-mail",
    "phone",
    "job-position",
    "company"
]

RED_FIELD_ID = "zip-code"


def test_form_field_colors():
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    driver.find_element(By.CSS_SELECTOR,
                        "input[name='first-name']").send_keys("Иван")
    driver.find_element(By.CSS_SELECTOR,
                        "input[name='last-name']").send_keys("Петров")
    driver.find_element(By.CSS_SELECTOR,
                        "input[name='address']").send_keys("Ленина, 55-3")
    driver.find_element(By.CSS_SELECTOR,
                        "input[name='zip-code']")
    driver.find_element(By.CSS_SELECTOR,
                        "input[name='city']").send_keys("Москва")
    driver.find_element(By.CSS_SELECTOR,
                        "input[name='country']").send_keys("Россия")
    driver.find_element(By.CSS_SELECTOR,
                        "input[name='e-mail']").send_keys("test@skypro.com")
    driver.find_element(By.CSS_SELECTOR,
                        "input[name='phone']").send_keys("+7985899998787")
    driver.find_element(By.CSS_SELECTOR,
                        "input[name='job-position']").send_keys("QA")
    driver.find_element(By.CSS_SELECTOR,
                        "input[name='company']").send_keys("SkyPro")
    driver.find_element(By.CSS_SELECTOR,
                        "button[type='submit']").click()

    waiter.until(
            EC.text_to_be_present_in_element_attribute(
                (By.ID, RED_FIELD_ID), "class", "alert-danger"
            )
        )

    assert "alert-danger" in driver.find_element(
        By.ID, RED_FIELD_ID).get_attribute("class")

    for field_id in GREEN_FIELDS_IDS:
        waiter.until(
            EC.text_to_be_present_in_element_attribute(
                    (By.ID, field_id), "class", "alert-success"
            )
        )
        assert "alert-success" in driver.find_element(
            By.ID, field_id).get_attribute("class")
    driver.quit()
