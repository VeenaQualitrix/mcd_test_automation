from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time

locators = {
        "JUSPAY_PAGE_VERIFICATION": (By.XPATH, "//img[@alt='juspay brand']"),
        "COD_PAYMENT_MODE": (By.XPATH, "//article[text()='Cash On Delivery']"),
        "COD_PAYMENT_MODE_SELECTED": (By.XPATH, "(//article[text()='Cash On Delivery'])[4]"),
        "PROCEED_TO_PAY_BUTTON": (By.XPATH, "//article[text()='Proceed to Pay']"),
        "ORDER_PLACED_SUCCESS_MESSAGE": (By.XPATH, "//span[contains(text(), 'Yayy Your Order is  Placed!')]")
    }


class JuspayPage(BasePage):

    def verify_juspay_page_is_reached(self):
        time.sleep(5)
        return self.actions.is_element_displayed(*locators['JUSPAY_PAGE_VERIFICATION'])
        
    def select_payment_method(self):
        self.actions.click_button(*locators["COD_PAYMENT_MODE"])
        print("Clicked On Cash On Delivery Payment Method")

    def verify_selected_payment_method_is_displayed(self):
        return self.actions.is_element_displayed(*locators["COD_PAYMENT_MODE_SELECTED"])
    
    def click_on_proceed_to_pay(self):
        self.actions.click_button(*locators["PROCEED_TO_PAY_BUTTON"])
        print("Clicked On Proceed To Pay Button")
        time.sleep(10)

    def verify_order_placed_success_message(self):
        time.sleep(5)
        return self.actions.is_element_displayed(*locators["ORDER_PLACED_SUCCESS_MESSAGE"])
