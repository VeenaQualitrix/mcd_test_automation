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
    
"MCDELIVERY_ICON":(AppiumBy.ACCESSIBILITY_ID, "ic-bm-delivery-active"),

"MCDELIVERY_ICON_DISABLED":(AppiumBy.XPATH, '(//XCUIElementTypeImage[@name="ic-bm-delivery"])[1]'),

"DINEIN_ICON":(AppiumBy.ACCESSIBILITY_ID, "ic-bm-dine-in"),

"ONTHEGO_ICON":(AppiumBy.XPATH, '//XCUIElementTypeImage[@name="ic-bm-otg"]'),

"TAKEAWAY_ICON":(AppiumBy.XPATH, '//XCUIElementTypeImage[@name="ic-bm-delivery"]'),

"VERIFY_DINE_IN":(AppiumBy.ACCESSIBILITY_ID, 'No store selected'),

"LOCATION_PERMISSION_PROMPT":(AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Store based on your Current Location"]'),

'FLAT_NO': (AppiumBy.XPATH, '//XCUIElementTypeTextField[@value="*House / Flat No."]'),

'FLOOR': (AppiumBy.XPATH, '//XCUIElementTypeTextField[@value="Floor no / Wing name"]'),

'SERVICE_UNAVAILABLE_MESSAGE': (AppiumBy.ACCESSIBILITY_ID, '_banner1_img'),

'SEARCH_AREA': (AppiumBy.ACCESSIBILITY_ID, 'Search for area, street name..'),

'CURRENT_LOCATION_DINE': (AppiumBy.ACCESSIBILITY_ID, 'Current location'),

'RESTAURANTS_AVAILABILITY': (AppiumBy.ACCESSIBILITY_ID, 'Mantri Mall'),

'PROFILE_TAB': (AppiumBy.ACCESSIBILITY_ID, 'ic-bottom-tab-mymcd'),

'PROFILE_NAME': (AppiumBy.ACCESSIBILITY_ID, 'Testuser01'),

'PROFILE_PHONENUMBER': (AppiumBy.ACCESSIBILITY_ID, '+917777777777'),

'HOME_TAB': (AppiumBy.ACCESSIBILITY_ID, 'ic-bottom-tab-home'),


}
class SwitchScreenIos(BasePage):

    def click_business_model_dropdown(self):
        time.sleep(1)  # Consider replacing with explicit waits for better reliability
        print("Clicking on MCDELIVERY icon...")
        if self.actions.is_element_displayed(*locators['MCDELIVERY_ICON']):
            self.actions.click_button(*locators['MCDELIVERY_ICON'])
        else:
            print("MCDELIVERY icon not visible.")
        print("Clicking on DINEIN icon...")
        if self.actions.is_element_displayed(*locators['DINEIN_ICON']):
            self.actions.click_button(*locators['DINEIN_ICON'])
        else:
            print("DINEIN icon not visible.")
        print("Clicking on ONTHEGO icon...")
        if self.actions.is_element_displayed(*locators['ONTHEGO_ICON']):
            self.actions.click_button(*locators['ONTHEGO_ICON'])
        else:
            print("ONTHEGO icon not visible.")

        print("Clicking on TAKEAWAY icon...")
        if self.actions.is_element_displayed(*locators['TAKEAWAY_ICON']):
            self.actions.click_button(*locators['TAKEAWAY_ICON'])
        else:
            print("TAKEAWAY icon not visible.")
       

    def select_dine_in(self):
        time.sleep(3)
        self.actions.click_button(*locators["DINEIN_ICON"])
           
    
        
    def verify_dine_in_selected(self):
        if self.actions.is_element_displayed(*locators["VERIFY_DINE_IN"]):
            print("Dine-In option is currently selected and visible.")
        else:
            print("Dine-In option is not selected or not visible.")
            raise AssertionError("Dine-In is not selected or not visible.")


    def verify_default_business_model(self):
        if self.actions.is_element_displayed(*locators["MCDELIVERY_ICON"]):
            print("McDelivery is selected by default.")
        else:
            raise AssertionError("Default business model is not set to McDelivery.")

    def select_on_the_go(self):
        time.sleep(2) 
        print("Selecting the 'On the Go' option.")
        self.actions.click_button(*locators["ONTHEGO_ICON"])

    def verify_location_permission_prompt(self):
        if self.actions.is_element_displayed(*locators["LOCATION_PERMISSION_PROMPT"]):
            print("Location permission prompt is displayed.")
        else:
            raise AssertionError("Location permission prompt was not displayed.")

    def enter_unsupported_address(self):
        time.sleep(2)  
        self.actions.send_keys(*locators['FLAT_NO'], "Gurugram Sector 99")
        self.actions.send_keys(*locators['FLOOR'], "3rd Floor")
        
    def verify_service_unavailable_message(self):
        if self.actions.is_element_displayed(*locators["SERVICE_UNAVAILABLE_MESSAGE"]):
            print("Service not available message is correctly displayed.")
        else:
            raise AssertionError("Service not available message was not displayed.")


    def verify_dine_in_restaurant_listings(self):
        self.actions.click_button(*locators["SEARCH_AREA"])
        self.actions.click_button(*locators["CURRENT_LOCATION_DINE"])
        self.actions.is_element_displayed(*locators["RESTAURANTS_AVAILABILITY"])
           

    def verify_visual_feedback_on_model_options(self):
        visual_feedback_elements = [
            locators["MCDELIVERY_ICON"],
            locators["DINEIN_ICON"],
            locators["ONTHEGO_ICON"],
            locators["TAKEAWAY_ICON"]
        ]

        for element in visual_feedback_elements:
            if self.actions.is_element_displayed(*element):
                print(f"Visual feedback displayed for: {element}")
            else:
                raise AssertionError(f"Visual feedback not displayed for: {element}")


    def note_profile_details(self):
        self.actions.click_button(*locators["PROFILE_TAB"])
        time.sleep(2) 
        name = self.actions.get_text(*locators["PROFILE_NAME"])
        phonenumber = self.actions.get_text(*locators["PROFILE_PHONENUMBER"])
        self.profile_snapshot = {
            "name": name,
            "phonenumber": phonenumber
        }
        print(f"Captured profile details: Name = {name}, Email = {phonenumber}")

    def click_homepage(self):
        self.actions.click_button(*locators["HOME_TAB"])
        print("Clicked on the homepage tab.")


    def select_mc_delivery(self):
        print("Selecting McDelivery...")
        if self.actions.is_element_displayed(*locators["MCDELIVERY_ICON_DISABLED"]):
            self.actions.click_button(*locators["MCDELIVERY_ICON_DISABLED"])
            print("Clicked McDelivery icon.")
        else:
            raise AssertionError("McDelivery icon not found on screen.")

    def verify_profile_details_unchanged(self):
        self.actions.click_button(*locators["PROFILE_TAB"])
        assert self.actions.is_element_displayed(*locators["PROFILE_NAME"]), "Profile name is not displayed."
        assert self.actions.is_element_displayed(*locators["PROFILE_PHONENUMBER"]), "Profile phone number is not displayed."
        print(" Verified that the profile details are displayed and unchanged.")

    
    
        
        
