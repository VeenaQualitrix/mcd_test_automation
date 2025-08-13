from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from actions.ios_actions import iOSActions
from selenium.webdriver.common.keys import Keys
import time
import allure
import pytest
import pyperclip


locators = {
    
"LOGOUT": (AppiumBy.ACCESSIBILITY_ID, "ic-logoutIconLogout ic-arrow-right"),

'ADD_ADDRESS_BUTTON': (AppiumBy.XPATH, '(//XCUIElementTypeImage[@name="ic-arrow-down"])[1]'),

"LOGIN_SCREEN_IDENTIFIER": (AppiumBy.ACCESSIBILITY_ID, "Log In / Sign Up to Continue"),

"POPUP_DO_LATER": (AppiumBy.ACCESSIBILITY_ID, "I'll Do It Later"),

'MENU_OPTION': (AppiumBy.ACCESSIBILITY_ID, "Menu"),

'ADD_ITEM': (AppiumBy.XPATH, '(//XCUIElementTypeImage[@name="ic-add"])[1]'),

'NEXT_BUTTON': (AppiumBy.ACCESSIBILITY_ID, "Next"),

'ADD_TO_CART_BUTTON': (AppiumBy.ACCESSIBILITY_ID, "Add to Cart"),

'VIEW_CART_BUTTON': (AppiumBy.ACCESSIBILITY_ID, "View Cart"),

'LOGIN_SCREEN_CLOSE_BUTTON': (AppiumBy.ACCESSIBILITY_ID, "ic-close"),

'CART_SCREEN_YOUR_ORDER': (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Your Order"]'),

}
class AddressScreenIos(BasePage):


    def navigate_to_checkout(self):
        try:
            print("Clicking the logout button")
            self.actions.click_button(*locators['LOGOUT'])
            self.actions.click_button(*locators['POPUP_DO_LATER'])
        except Exception as e:
            print(f"Exception occurred while navigating to checkout: {e}")
            


        
    def click_add_address(self):
        time.sleep(3)
        print("Attempting to click the Add Address button")
        self.actions.click_button(*locators['ADD_ADDRESS_BUTTON'])
        print("Clicked the Add Address button")

    def verify_login_signup_screen(self):
        time.sleep(3)
        is_displayed = self.actions.is_element_displayed(*locators['LOGIN_SCREEN_IDENTIFIER'])
        assert is_displayed, "Login screen is not displayed"
        print("Login screen is displayed")

    def tap_continue_button(self):
        time.sleep(3)
        print("Clicking the continue button on login screen")
        self.actions.click_button(*locators['LOGIN_SCREEN_IDENTIFIER'])
    
    def click_menu_option(self):
        time.sleep(3)
        print("Attempting to click on the Menu option")
        self.actions.click_button(*locators['MENU_OPTION'])
        print("Successfully clicked on the Menu option")

    def click_add_on_item(self):
        time.sleep(3)
        self.actions.click_button(*locators['ADD_ITEM'])
        print("Successfully clicked on Add")
    
    def click_next_button(self):
            self.actions.click_button(*locators['NEXT_BUTTON'])
            print("Successfully clicked on the Next button")

        
    def click_add_to_cart(self):
        time.sleep(3)
        self.actions.click_button(*locators['ADD_TO_CART_BUTTON'])
        print("Successfully clicked on Add to Cart")
    
       

    def click_view_cart(self):
        time.sleep(3)
        self.actions.click_button(*locators['VIEW_CART_BUTTON'])
        print("Successfully clicked on View Cart")
    

    def login_continue_button(self):
        time.sleep(3)
        self.actions.click_button(*locators['LOGIN_SCREEN_IDENTIFIER'])
        print("Successfully tapped on the login continue button")
    

    def close_login_screen(self):
        time.sleep(3)
        self.actions.click_button(*locators['LOGIN_SCREEN_CLOSE_BUTTON'])
        print("Login screen closed successfully")
    

    def verify_cart_or_checkout_screen_displayed(self):
        time.sleep(3)
        self.actions.is_element_displayed(*locators['CART_SCREEN_YOUR_ORDER'])
        print("User is redirected to the cart screen")
        
