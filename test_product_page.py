from .pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

    product_page = ProductPage(browser, link)
    product_page.open()

    product_page.should_be_product_name()
    product_page.should_be_product_price()
    product_page.should_be_button_add_to_basket()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_message_added_to_basket()
    product_page.should_be_successful_message_conteins_product_name()
    product_page.should_be_alert_info_message_basket_total()
    product_page.should_be_basket_total_matches_product_price()