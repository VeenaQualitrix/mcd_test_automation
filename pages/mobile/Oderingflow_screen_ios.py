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
    
"ADD_ITEM_BUTTON": (AppiumBy.ACCESSIBILITY_ID, "Add"),

'BREAKFAST_CATEGORY_BUTTON': (AppiumBy.XPATH, '(//XCUIElementTypeStaticText[@name="McBreakfast"])[2]'),

'VEG_MCMUFFIN_ITEM': (AppiumBy.XPATH, '//XCUIElementTypeOther[@name="Veg McMuffin with protein plus Meal"]'),

"SELECT_LOCATION_BUTTON": (AppiumBy.ACCESSIBILITY_ID, "Please select location"),

'LOCATION_IN_POPUP': (AppiumBy.XPATH, '(//XCUIElementTypeStaticText[@name="Gurugram Sector 99, 3rd Floor,"])[1]'),

'YOUR_ORDER_HEADER': (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Your Order"]'),

}
class OderingScreenIos(BasePage):


     
    def select_breakfast_category(self):
        time.sleep(3)
        print("Attempting to select the Breakfast category")
        self.actions.is_element_displayed(*locators['BREAKFAST_CATEGORY_BUTTON'])
        print("Selected the Breakfast category")

    def select_veg_mcmuffin_protein_plus_meal(self):
        time.sleep(2)
        print("Attempting to select Veg McMuffin item")
        self.actions.click_button(*locators['VEG_MCMUFFIN_ITEM'])
        print("Selected Veg McMuffin")

    
    def click_add_item(self):
        time.sleep(2)
        print("Attempting to click the Add Item button")
        self.actions.click_button(*locators['ADD_ITEM_BUTTON'])
        print("Clicked the Add Item button")

    def click_select_location(self):
        time.sleep(2)
        print("Attempting to click on 'Please select location'")
        self.actions.click_button(*locators['SELECT_LOCATION_BUTTON'])
        print("Clicked on 'Please select location'")

    def select_location_in_popup(self):
        time.sleep(2)
        print("Attempting to select a location from the popup")
        self.actions.click_button(*locators['LOCATION_IN_POPUP'])
        print("Selected the location from the popup")

    def verify_your_order_displayed(self):
        time.sleep(2)
        print("Verifying the 'Your Order' screen is displayed")
        order_header = self.actions.is_element_displayed(*locators['YOUR_ORDER_HEADER'])
        assert order_header is not None, "Your Order screen is not displayed"
        print("'Your Order' screen verified successfully")
