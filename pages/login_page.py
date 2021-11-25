from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import BasePageLocators
class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()
    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()
        return LoginPage(browser=self.browser, url=self.browser.current_url)
    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert (self.url.find('login') != -1), "Login is url not found"
    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        self.is_element_present(*LoginPageLocators.login_form), "Login form is not found"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.register_form), "Login register is not found"
    def register_new_user(self, email, password):
        new_email = self.browser.find_element(*LoginPageLocators.register_email)
        new_email.send_keys(email)
        new_password1 = self.browser.find_element(*LoginPageLocators.register_password1)
        new_password1.send_keys(password)
        new_password2 = self.browser.find_element(*LoginPageLocators.register_password2)
        new_password2.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.register_button)
        button.click()
