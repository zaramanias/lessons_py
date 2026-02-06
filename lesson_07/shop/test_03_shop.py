
from selenium import webdriver
from page.ShopPage import ShopPage
from page.CartPage import CartPage


def test_shop_total():
    driver = webdriver.Firefox()
    shop_page = ShopPage(driver)
    cart_page = CartPage(driver)
    shop_page.open()
    shop_page.login("standard_user", "secret_sauce")
    shop_page.add_to_cart()
    cart_page.go_to_cart()
    cart_page.checkout()
    cart_page.fill_checkout_info("Иван", "Петров", "123456")
    value = cart_page.get_result()
    driver.quit()
    assert value == "Total: $58.29"
