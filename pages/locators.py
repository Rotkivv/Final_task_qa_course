from selenium.webdriver.common.by import By

class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini>span>a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")

class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form") 
    REGISTRATION_FORM = (By.CSS_SELECTOR, '#register_form')

    REGISTRATION_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTRATION_PASS1 = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTRATION_PASS2 = (By.CSS_SELECTOR, '#id_registration-password2')
    BTN_REGISTER = (By.CSS_SELECTOR, 'button[name="registration_submit"]')

class ProductPageLocators(object):
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main>h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main>.price_color')
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form > button.btn-add-to-basket")

    ALERT_SUCCESS_ADD_TO_BASKET = (By.CSS_SELECTOR, '#messages>.alert-success:nth-child(1)>.alertinner > strong')
    ALERT_INFO_TOTAL_BACKET = (By.CSS_SELECTOR, '#messages > .alert-info strong')

class BasketPageLocators(object):
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner>p")
    BASKET_SUMMARY = (By.CSS_SELECTOR,".basket_summary")