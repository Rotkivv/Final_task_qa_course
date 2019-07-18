from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        #проверка, что корректный url адрес
        assert "login" in self.browser.current_url , "Not correct url " + str(self.browser.current_url) 

    def should_be_login_form(self):
        #проверка, что есть форма логина на странице
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        #проверка, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"

    def register_new_user(self, email, password):
        email_element = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        email_element.send_keys(email)

        pass1 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASS1)
        pass1.send_keys(password)

        pass2 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASS2)
        pass2.send_keys(password)

        button = self.browser.find_element(*LoginPageLocators.BTN_REGISTER)
        button.click()