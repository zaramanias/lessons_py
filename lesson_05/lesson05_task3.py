from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://the-internet.herokuapp.com/inputs')

search_input = driver.find_element(By.CSS_SELECTOR, 'input')
driver.execute_script("arguments[0].setAttribute('type', 'text');",
                      search_input)

search_input.click()
search_input.send_keys('Sky')
sleep(2)
search_input.clear()
sleep(2)
search_input.send_keys('Pro')

sleep(10)

driver.quit()
