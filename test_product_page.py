from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import  LoginPage
import time
import pytest

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_cart(browser, link):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    #link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    
    product_page = ProductPage(browser, link)
    product_page.open()

    product_page.should_be_product_name()
    product_page.should_be_product_price()
    product_page.should_be_button_add_to_basket()
    product_page.should_not_be_success_message()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_message_added_to_basket()
    product_page.should_be_successful_message_conteins_product_name()
    product_page.should_be_alert_info_message_basket_total()
    product_page.should_be_basket_total_matches_product_price()

def test_guest_cant_see_success_message_after_adding_product_to_cart(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    
    product_page = ProductPage(browser, link)
    product_page.open()

    product_page.should_be_button_add_to_basket()
    product_page.add_to_basket()
    product_page.should_not_be_success_message()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'

    product_page = ProductPage(browser, link)
    product_page.open()
    
    product_page.should_not_be_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_message_disappeared_after_adding_product_to_cart(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'

    product_page = ProductPage(browser, link)
    product_page.open()

    product_page.should_be_button_add_to_basket()
    product_page.add_to_basket()
    time.sleep(1)
    product_page.should_disappear_success_message()

def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'

    page = BasketPage(browser, link)
    page.open()

    page.go_to_basket_page()
    page.should_not_be_see_product_in_basket()
    page.should_be_message_basket_is_empty()

class TestUserAddToCartFromProductPage(object):
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        
        page = LoginPage(browser, link)
        page.open()

        page.register_new_user('test'+str(time.time()) + "@fakemail.org", 'Qqwertyuiop')
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'

        product_page = ProductPage(browser, link)
        product_page.open()
        
        product_page.should_not_be_success_message()

    def test_user_can_add_product_to_cart(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    
        product_page = ProductPage(browser, link)
        product_page.open()

        product_page.should_be_product_name()
        product_page.should_be_product_price()
        product_page.should_be_button_add_to_basket()
        product_page.should_not_be_success_message()
        product_page.add_to_basket()
        product_page.solve_quiz_and_get_code()
        product_page.should_be_message_added_to_basket()
        product_page.should_be_successful_message_conteins_product_name()
        product_page.should_be_alert_info_message_basket_total()
        product_page.should_be_basket_total_matches_product_price()
