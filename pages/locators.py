from selenium.webdriver.common.by import By

class ProductPageLocators(object):
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, "div.alertinner ")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div.alertinner ')
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
class BasketPageLocators():
    BASKET_PAGE = (By.CSS_SELECTOR, 'span.btn-group')
    BASKET_CONTENT = (By.CSS_SELECTOR, 'div.basket-title hidden-xs')
    BASKET_MESSAGE = (By.CSS_SELECTOR, 'div#content_inner p')
class LoginPageLocators():
    login_form = (By.CSS_SELECTOR, '#login_form')
    register_form = (By.CSS_SELECTOR, '#register_form')
    register_email = (By.NAME, 'registration-email')
    register_password1 = (By.NAME, 'registration-password1')
    register_password2 = (By.NAME, 'registration-password2')
    register_button = (By.NAME, 'registration_submit')
