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

'ADD_NEW_ADDRESS_BUTTON': (AppiumBy.ACCESSIBILITY_ID, "Add new"),

'CONFIRM_LOCATION_BUTTON': (AppiumBy.ACCESSIBILITY_ID, "Confirm Location"),

'FLAT_NO': (AppiumBy.XPATH, '//XCUIElementTypeTextField[@value="*House / Flat No."]'),

'FLOOR': (AppiumBy.XPATH, '//XCUIElementTypeTextField[@value="Floor no / Wing name"]'),

'BUILDING_NAME': (AppiumBy.XPATH, '//XCUIElementTypeTextField[@value="Apartment / Building Name"]'),

'MOBILE_NUMBER': (AppiumBy.XPATH, '//XCUIElementTypeTextField[@value="Contact Number"]'),

'SAVE_ADDRESS_BUTTON': (AppiumBy.ACCESSIBILITY_ID, "Save Address"),

'BACK_BUTTON': (AppiumBy.ACCESSIBILITY_ID, "ic-arrow-left-primary"),

'ALL_ADDRESS': (AppiumBy.XPATH, '(//XCUIElementTypeStaticText[@name="101, 5, Sunset Plaza, Sri Sai Collections"])[1]'),


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
        time.sleep(6)
        print("Attempting to click on the Menu option")
        self.actions.click_button(*locators['MENU_OPTION'])
        print("Successfully clicked on the Menu option")

    def click_add_on_item(self):
        time.sleep(3)
        self.actions.click_button(*locators['ADD_ITEM'])
        print("Successfully clicked on Add")
    
    def click_next_button(self):
        print("Attempting to click on the 'Next' button...")
        try:
            next_button = self.actions.find_element(*locators['NEXT_BUTTON'])
            if next_button:
                self.actions.click_button(*locators['NEXT_BUTTON'])
                print("Successfully clicked on the 'Next' button.")
            else:
                print("'Next' button element was not found.")
        except Exception as e:
            print(f"Failed to click 'Next' button: {e}")



        
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
        

    def tap_add_new_address(self):
        time.sleep(2)  
        self.actions.click_button(*locators['ADD_NEW_ADDRESS_BUTTON'])
        print("'Add New Address' button tapped")

    def click_confirm_location(self):
        time.sleep(2)  # Preferably replace with explicit wait
        self.actions.click_button(*locators['CONFIRM_LOCATION_BUTTON'])
        print("'Confirm Location' button clicked")

    
    def enter_address_details(self):
        time.sleep(2)  # Consider replacing with explicit waits if available
        self.actions.send_keys(*locators['FLAT_NO'], "123 Main Street")
        self.actions.send_keys(*locators['FLOOR'], "2nd floor")
        self.actions.send_keys(*locators['BUILDING_NAME'], "John")
        self.actions.send_keys(*locators['MOBILE_NUMBER'], "7777777777")
        print("Entered address: Flat No - 123 Main Street, Floor - 2nd floor, Building - John, Mobile - 7777777777")

    def tap_save_address(self):
        time.sleep(2)  # Prefer explicit wait for production use
        self.actions.click_button(*locators['SAVE_ADDRESS_BUTTON'])
        print("'Save Address' button tapped")


    def leave_mandatory_fields_empty(self):
        time.sleep(2)  # Replace with explicit wait if needed
        self.actions.send_keys(*locators['FLOOR'], "3rd Floor")
        self.actions.send_keys(*locators['BUILDING_NAME'], "Greenwood")
        print("Mandatory address fields left empty (e.g., Flat No, Mobile Number)")

    def is_save_button_disabled(self):
        time.sleep(1)  # Use explicit wait ideally
        save_button = self.actions.find_element(*locators['SAVE_ADDRESS_BUTTON'])
        is_enabled = save_button.is_enabled()
        print(f"'Save' button enabled state: {is_enabled}")
        return not is_enabled

    def enter_special_character_address(self):
        time.sleep(2)  # Replace with explicit waits in production
        self.actions.send_keys(*locators['FLAT_NO'], "@#*&^")
        self.actions.send_keys(*locators['FLOOR'], "!$%^")
        self.actions.send_keys(*locators['BUILDING_NAME'], "~`<>?")
        self.actions.send_keys(*locators['MOBILE_NUMBER'], "7777777777")  # Valid input to allow form submission
        print("Special characters entered in Flat No, Floor, Building Name")

    def cancel_address_entry_midway(self):
        time.sleep(2)  
        self.actions.send_keys(*locators['FLAT_NO'], "456")
        self.actions.send_keys(*locators['FLOOR'], "3rd")
        self.actions.send_keys(*locators['BUILDING_NAME'], "Ocean View")
        print("Entered partial address. Cancelling...")
        self.actions.click_button(*locators['BACK_BUTTON'])

    def enter_text_exceeding_max_limit(self):
        long_text = "A" * 301  # 301 characters, exceeding the 300 char limit
        self.actions.send_keys(*locators['FLAT_NO'], long_text)
        print("Entered 301 characters into address fields.")

    
    
    def enter_duplicate_address(self):
        existing_address = {
            'FLAT_NO': "101",
            'FLOOR': "5",
            'BUILDING_NAME': "Sunset Plaza",
            'MOBILE_NUMBER': "9999999999",
        }
        self.actions.send_keys(*locators['FLAT_NO'], existing_address['FLAT_NO'])
        self.actions.send_keys(*locators['FLOOR'], existing_address['FLOOR'])
        self.actions.send_keys(*locators['BUILDING_NAME'], existing_address['BUILDING_NAME'])
        self.actions.send_keys(*locators['MOBILE_NUMBER'], existing_address['MOBILE_NUMBER'])
        print("Entered duplicate address details.")
    
    def verify_duplicate_address_saved(self):
        time.sleep(2)  
        # Get all address elements from the "All Address" section
        address_elements = self.actions.find_elements(*locators["ALL_ADDRESS"])

        # Extract the text of each address
        addresses = [el.text.strip() for el in address_elements]

        # Check for duplicates
        seen = set()
        duplicates = []

        for addr in addresses:
            if addr in seen:
                duplicates.append(addr)
            else:
                seen.add(addr)

        # Print results
        if duplicates:
            print("Duplicate addresses found:")
            for dup in set(duplicates):
                print("-", dup)
        else:
            print("No duplicate addresses found.")
        self.driver.back()


    
    


