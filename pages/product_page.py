from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):
    
    def should_be_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name is not presented"
    
    def should_be_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product price is not presented"
    
    def should_be_button_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.BTN_ADD_TO_BASKET), \
            "Button add-to-basket is not presented"

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
    
    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        
    def get_alert_info_total_basket(self):
        return self.browser.find_element(*ProductPageLocators.ALERT_INFO_TOTAL_BACKET).text

    def get_alert_success_add_to_basket(self):
        return self.browser.find_element(*ProductPageLocators.ALERT_SUCCESS_ADD_TO_BASKET).text

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ALERT_SUCCESS_ADD_TO_BASKET), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.ALERT_SUCCESS_ADD_TO_BASKET), \
            "Success message is presented, but should disappear"

    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        button.click()
        
    def should_be_message_added_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ALERT_SUCCESS_ADD_TO_BASKET), \
            "No success message added"
    
    def should_be_successful_message_conteins_product_name(self):
        assert self.get_product_name() == self.get_alert_success_add_to_basket(), \
            "Successful message not conteins product name "+str(self.browser.current_url)

    def should_be_alert_info_message_basket_total(self):
        assert self.is_element_present(*ProductPageLocators.ALERT_INFO_TOTAL_BACKET), \
            "No message info basket total"
    
    def should_be_basket_total_matches_product_price(self):
        assert self.get_product_price() ==  self.get_alert_info_total_basket(), \
            "Info message basket total does not mach product price"

