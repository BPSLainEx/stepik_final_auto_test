from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert (self.url.find('login') != -1), "Login is url not found"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        self.is_element_present(*LoginPageLocators.login_form), "Login form is not found"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.register_form), "Login register is not found"