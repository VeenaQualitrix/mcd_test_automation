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
    
"MCDELIVERY_ICON":(AppiumBy.XPATH, '//XCUIElementTypeImage[@name="ic-bm-delivery-active"]'),

"DINEIN_ICON":(AppiumBy.ACCESSIBILITY_ID, "ic-bm-dine-in"),

"ONTHEGO_ICON":(AppiumBy.XPATH, '//XCUIElementTypeImage[@name="ic-bm-otg"]'),

"TAKEAWAY_ICON":(AppiumBy.XPATH, '//XCUIElementTypeImage[@name="ic-bm-delivery"]'),

"VERIFY_DINE_IN":(AppiumBy.ACCESSIBILITY_ID, 'No store selected'),

"LOCATION_PERMISSION_PROMPT":(AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Store based on your Current Location"]'),

}
class SwitchScreenIos(BasePage):

    def click_business_model_dropdown(self):
        time.sleep(3)  # Consider replacing with explicit waits for better reliability
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
