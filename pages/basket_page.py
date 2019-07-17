from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasketPageLocators

class BasketPage(BasePage):
    
    def should_not_be_see_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_SUMMARY), \
            "Products is presented, but should not be"
    
    def should_be_message_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
            "No present empty basket message"