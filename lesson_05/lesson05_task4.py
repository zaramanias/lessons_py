from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get('http://the-internet.herokuapp.com/login')

search_username = driver.find_element(By.CSS_SELECTOR, 'input#username')
search_username.send_keys('tomsmith')

sleep(2)

search_pass = driver.find_element(By.CSS_SELECTOR, 'input#password')
search_pass.send_keys('SuperSecretPassword!')

sleep(2)

search_button = driver.find_element(By.CSS_SELECTOR, 'i')
search_button.click()

sleep(2)

search_text = driver.find_element(By.CSS_SELECTOR, 'div#flash').text

print(search_text)

driver.quit()
