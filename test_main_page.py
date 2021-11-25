from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/'
    page = BasketPage(browser, link)
    page.open()
    page.press_to_button_basket()
    page.should_be_basket_content()
    page.should_be_basket_message()

