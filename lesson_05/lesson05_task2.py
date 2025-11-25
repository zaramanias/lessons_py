from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://uitestingplayground.com/dynamicid')

search_button = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary')
search_button.click()

sleep(10)
