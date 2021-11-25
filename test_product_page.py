import time
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest
@pytest.mark.need_review
def test_user_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/'
    page = LoginPage(browser, link)
    page.open()
    login_page = page.go_to_login_page()
    email = str(time.time()) + "@fakemail.org"
    password = '123456qwertyuio'
    login_page.register_new_user(email, password)
    login_page.should_be_authorized_user()
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser, link)
    page.open()
    page.press_button_add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_message_about_adding()
    page.should_be_message_basket_total()
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = BasketPage(browser, link)
    page.open()
    page.press_to_button_basket()
    page.should_be_basket_content()
    page.should_be_basket_message()
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    login_page = page.go_to_login_page()
    login_page.should_be_login_link()





