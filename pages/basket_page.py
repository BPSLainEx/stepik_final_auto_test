from .base_page import BasePage
from .locators import BasketPageLocators
import pytest
class BasketPage(BasePage):
    def press_to_button_basket(self):
        basket = self.browser.find_element(*BasketPageLocators.BASKET_PAGE)
        basket.click()
    @pytest.mark.xfail
    def should_be_basket_content(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_CONTENT), 'Success content is presented, but should not be'
    @pytest.mark.xfail
    def should_be_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_MESSAGE), 'message is not presented'
