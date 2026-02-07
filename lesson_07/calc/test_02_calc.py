
from selenium import webdriver
from page.CalcPage import CalcPage


def test_calculator():
    driver = webdriver.Chrome()
    calc_page = CalcPage(driver)
    calc_page.open()
    calc_page.set_delay("45")
    calc_page.click_button('7')
    calc_page.click_button('+')
    calc_page.click_button('8')
    calc_page.click_button('=')
    calc_page.wait_spinner()

    assert calc_page.get_result() == str(calc_page.calculate())
    driver.quit()
