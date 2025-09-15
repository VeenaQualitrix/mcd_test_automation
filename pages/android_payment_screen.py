from conftest import setup_platform
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.view_cart_page import ViewCartPage
import time

locators = {
        "PAYMENT_METHOD_SCREEN": (By.XPATH, "//img[@alt='juspay brand']"),
    }


class AndroidPaymentScreen(BasePage):

    def verify_juspay_page_is_reached(self):
        time.sleep(10)
        return self.actions.is_element_displayed(*locators['PAYMENT_METHOD_SCREEN'])
        
    