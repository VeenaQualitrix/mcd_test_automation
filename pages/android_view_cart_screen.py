from pages.base_page import BasePage
from pages.android_view_screen import AndroidViewScreen
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
import time

locators = {
        "YOUR_ORDER": (AppiumBy.XPATH, "//android.widget.TextView[@text='Your Order']"),
        "ADD_BUTTON": (AppiumBy.XPATH, "//android.widget.Image[@text='ic-add']"),
        "ADD_TO_CART_BUTTON": (AppiumBy.XPATH, "//android.widget.Button[@text='Add to Cart']"),
        "VIEW_CART": (AppiumBy.XPATH, "//android.widget.TextView[@text='View Cart']"),
        "LOGIN_FROM_CHECKOUT_PAGE": (AppiumBy.XPATH, "//android.widget.Button[@text='Log In / Sign Up to Continue']"),
        "CANCEL_FROM_LOGIN_PROMPT": (AppiumBy.XPATH, "//android.widget.Image[@text='ic-close']"),
    

         }

class AndroidViewCartScreen(BasePage):
    
    def Click_login_prompt_from_checkout(self):
        self.actions.is_element_displayed(*locators['LOGIN_FROM_CHECKOUT_PAGE'])
        self.actions.click_button(*locators['LOGIN_FROM_CHECKOUT_PAGE'])
        time.sleep(2)
    
    def click_cancel_to_login_or_signup_page(self):
        self.actions.is_element_displayed(*locators['CANCEL_FROM_LOGIN_PROMPT'])
        self.actions.click_button(*locators['CANCEL_FROM_LOGIN_PROMPT'])
        time.sleep(2)

    def verify_login_page_navigation_from_checkout(self):
        time.sleep(5)
        return self.actions.is_element_displayed(*locators['LOGIN_PAGE_HEADER_FROM_CHECKOUT'])
    
    def verify_redirect_to_checkout_page(self):
        time.sleep(5)
        return self.actions.is_element_displayed(*locators['YOUR_ORDER'])